import sys
import os
import urllib.parse
import requests
import configparser
from getopt import getopt
from StudentDetails import StudentDetails
from StudentCode import StudentCode
from FetchStudentCode import FetchStudentCode
import DConstants 
from MessageTemplates import template, templates_type

class SendSMS:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r"C:\Users\LENOVO\OneDrive\Documents\codes\BSC_Development\apiconfig.cnf")
        try:
            self.api_url = self.config["api_settings"]["base_url"].strip('"').strip("'")
            self.username = self.config["credentials"]["username"].strip('"').strip("'")
            self.password = self.config["credentials"]["password"].strip('"').strip("'")
            self.api_key = self.config["api_settings"]["key"].strip('"').strip("'")
            self.campaign = self.config["api_settings"]["campaign"].strip('"').strip("'")
            self.routeid = self.config["api_settings"]["routeid"].strip('"').strip("'")
            self.message_type = self.config["api_settings"]["type"].strip('"').strip("'")
            self.sender_id = self.config["api_settings"]["senderid"].strip('"').strip("'")
            self.pe_id = self.config["api_settings"]["pe_id"].strip('"').strip("'")
        except KeyError as e:
            print(f"Error: Missing configuration for key: {e}")
            sys.exit(1)
        self.template_id = None  

    def set_template_id(self, selected_template_id):
        self.template_id = selected_template_id

    def send_sms(self, phone_numbers, message):
        if not self.template_id:
            print("Error: template_id not set.")
            return DConstants.RC_SMS_FAILED

        payload = {
            "username": self.username,
            "password": self.password,
            "key": self.api_key,
            "campaign": self.campaign,
            "routeid": self.routeid,
            "type": self.message_type,
            "senderid": self.sender_id,
            "pe_id": self.pe_id,
            "template_id": self.template_id,
            "time": "",  
            "msg": urllib.parse.quote(message),  
        }

        for phone_number in phone_numbers:
            payload["contacts"] = phone_number.strip()

            try:
                response = requests.post(self.api_url, data=payload)
                if response.status_code == 200:
                    print(f"Message sent successfully to {phone_number}")
                else:
                    print(f"Failed to send message to {phone_number}. Status Code: {response.status_code}")
                    print(f"Response: {response.text}")
            except requests.RequestException as e:
                print(f"Error occurred while sending SMS to {phone_number}: {e}")
                return DConstants.RC_SMS_FAILED

        return DConstants.RC_CALL_SUCCESS
