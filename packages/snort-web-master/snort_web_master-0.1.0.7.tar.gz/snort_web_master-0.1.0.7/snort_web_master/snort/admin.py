import os
import time

from django import forms
from .models import SnortRule
from django.utils.html import format_html
from urllib.parse import quote as urlquote
from .snort_templates import snort_type_to_template, types_list, EMPTY_TYPES
from .parser import Parser
from django.contrib import messages
from django.utils.translation import gettext
# Register your models here.
from django.contrib import admin
from django_object_actions import DjangoObjectActions
import subprocess

from pcaps.admin import verify_legal_pcap


# todo: fix the sig structure: assitent needed
# todo: upload unmanaged rule file

class SnortRuleAdminForm(forms.ModelForm):
    class Meta:
        model = SnortRule
        fields = "__all__"

    def clean_group(self):
        return self.current_user.groups.name or "unassinged group"

    def clean_user(self):
        return getattr(self.current_user, self.current_user.USERNAME_FIELD)

    def clean_date(self):
        return self.cleaned_data["date"]


    def clean_type(self):
        if not dict(types_list).get(self.cleaned_data.get("type")):
            raise forms.ValidationError("cant find type, did you forgot it? or forgot to add type to db")
        return self.cleaned_data.get("type")

    def clean_content(self):
        if not (self.cleaned_data.get("type")):
            return self.clean_type()
        if self.cleaned_data.get("type") in EMPTY_TYPES:
            if self.cleaned_data["content"] != "":
                raise forms.ValidationError("rule cannot contain content in the current chosen type")
        else:
            if self.cleaned_data["content"] == "":
                raise forms.ValidationError("rule cannot be empty in the current chosen type")
            else:
                try:
                    rule_template = snort_type_to_template[dict(types_list)[self.cleaned_data.get("type")]]().get_rule("Test",
                                                                                                   sig_name="Test",
                                                                                                   sig_content=self.cleaned_data["content"],
                                                                                                   writer_team="Test",
                                                                                                   sig_writer="test",
                                                                                                   main_doc="0",
                                                                                                   cur_date=time.time(),
                                                                                                   sig_ref="0",
                                                                                                   sig_desc="Test",
                                                                                                   sid=self.current_user.id)
                    parser = Parser(rule_template)
                    parser.parse_header()
                    parser.parse_options()
                except Exception as e:
                    raise forms.ValidationError(e)

        return self.cleaned_data["content"]

    def clean_location(self):
        try:
            if os.path.dirname(self.cleaned_data["location"]) != "":
                os.makedirs(os.path.dirname(self.cleaned_data["location"]), exist_ok=True)
            os.makedirs(os.path.dirname(self.cleaned_data["location"]), exist_ok=True)
            with open(self.cleaned_data["location"], "w") as rule_file:
                rule_file.write(self.cleaned_data["content"])
        except Exception as e:
            forms.ValidationError(e)
        return self.cleaned_data["location"]

    def clean_pcap_validation(self):
        # return self.cleaned_data.get("pcap_validation")
        if not self.cleaned_data.get("pcap_validation"):
            raise forms.ValidationError("pcap validateion cannot be empty, please find a pcap that aggre with your rule")
        cur_rule = SnortRule()
        cur_rule.content = self.data.get("content")
        cur_rule.location = self.data.get("location")
        cur_rule.group = self.data.get("group")
        cur_rule.id = self.data.get("id")
        cur_rule.main_ref = self.data.get("main_ref")
        cur_rule.name = self.data.get("name")
        cur_rule.type = self.data.get("type")
        cur_rule.user = self.data.get("user")
        cur_rule.request_ref = self.data.get("request_ref")

        validate_pcap_snort(self.cleaned_data.get("pcap_validation"), cur_rule)
        return self.cleaned_data["pcap_validation"]


def validate_pcap_snort(pcaps, rule):
    rule_template = snort_type_to_template[dict(types_list)[rule.type]]().get_rule(rule.group, sig_name=rule.name, sig_content=rule.content, writer_team=rule.group, sig_writer=rule.user, main_doc=rule.main_ref, cur_date=time.time(), sig_ref=rule.request_ref, sig_desc=rule.description)
    stdout = b""
    if not rule.location:
        import re
        rule.location = re.sub(r'[-\s]+', '-',re.sub(r'[^\w\s-]', '',
                                 rule.name)
                          .strip()
                          .lower())

    with open(rule.location + ".tmp", "w") as rule_file:
        rule_file.write(rule_template)
    failed = True
    for pcap in pcaps:
        try:
            if not verify_legal_pcap("/app/{pcap.pcap_file}"):
                raise Exception(f"illegal pcap file")
            if not os.path.exists(f"/app/{pcap.pcap_file}"):
                raise Exception(f"cant find file /app/{pcap.pcap_file}")
            stdout, stderr = subprocess.Popen(["/home/snorty/snort3/bin/snort", "-R", rule.location + ".tmp", "-r", f"/app/{pcap.pcap_file}", "-A", "fast"], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE).communicate()
            if stdout and not stderr:
                if "total_alerts: " in stdout:
                    return "alert matched"
                else:
                    stderr = "alert did not matched rule"
            if stderr:
                raise forms.ValidationError(stderr + "<br>----------" + stdout.decode())
        except Exception as e:
            raise forms.ValidationError(f"could not validate rule on {pcap.pcap_file}: {e}")
    if failed:
        raise Exception("no rules was chosen")
    return stdout


@admin.register(SnortRule)
class SnortRuleAdmin(DjangoObjectActions, admin.ModelAdmin):
    # change_actions = ('validate',)
    # changelist_actions = ('validate',)
    filter_horizontal = ('pcap_validation',)
    list_display = ("name", "type", "description", "date", "main_ref")
    search_fields = ("name", "description", "content", "template", "type", "main_ref", "request_ref")
    form = SnortRuleAdminForm
    def get_form(self, request, *args, ** kwargs):
        form = super(SnortRuleAdmin, self).get_form(request, **kwargs)
        form.current_user = request.user
        return form

    def validate(self, request, obj:SnortRule):
        error = ""
        stdout = ""
        status = messages.ERROR
        try:
            snort_item = obj.first()
        except:
            snort_item = obj
        if os.name == "nt":
            error = f"cannot validate on windows"
            status = messages.ERROR
        else:
            try:
                stdout = validate_pcap_snort(snort_item.pcap_validation.all(), obj)

                stdout = stdout.decode().replace('\n', '<br>')
                status = messages.SUCCESS
                message = "The {name} “{obj}” run validation on {pcap} with results:<br>"+ f"{stdout}"
            except Exception as e:
                error = e
        if error:
            message = "The {name} “{obj}” failed validation on {pcap} due to ERROR:<b>{err}</b>"
        msg_dict = {
            "name": snort_item._meta.verbose_name,
            "obj": format_html('<a href="{}">{}</a>', urlquote(request.path), obj),
            "pcap": "all",
            "err": error
        }
        msg = format_html(
            gettext(message), **msg_dict
        )
        self.message_user(request, msg, status)
        return self.change_view(request, str(snort_item.id))
    # validate.label = "validate on pcaps"  # optional
    # validate.color = "green"
    readonly_fields = ('location', "user")
    # validate.short_description = "test rule on pcaps"  # optional



