import sys
import os
import urllib.parse
import requests
import configparser
from getopt import getopt
from UserCodeGenerator import UserCodeGenerator
from ComposeSMS import ComposeSMS
from SendSMS import SendSMS
import DConstants
from MessageTemplates import templates_type

class SendVisitorCode:
    def __init__(self):
        self.visitor_code = None
    def visitor_code_verification(self, student_id):
        cmp = ComposeSMS()
        vst = SendSMS()
        status_code, phone_numbers = cmp.validate_mobile_no(student_id)
        if status_code != DConstants.RC_CALL_SUCCESS:
            return
        code = UserCodeGenerator()
        self.visitor_code = code.generate_code()
        sms_type = "MESSAGE_TYPE_VISITOR_AUTH"
        sms_template = cmp.validate_sms(sms_type)

        if not sms_template:
            return

        message = cmp.compose_sms(sms_template, {"var": self.visitor_code})
        if not message:
            return
        selected_template_id = templates_type.get(sms_type)
        vst.set_template_id(selected_template_id)
        vst.send_sms(phone_numbers, message)
        print(f"Visitor code sent to the student's phone numbers.")
        
        return DConstants.RC_CALL_SUCCESS