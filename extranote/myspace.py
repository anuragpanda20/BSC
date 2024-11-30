import os
import sys
import getpass
import urllib.parse
import requests
from getopt import getopt
import configparser


class SMSSender:
    def __init__(self):
        self.username = None
        self.password = None
        self.message = None
        self.numbers = None
        self.api_url = "https://textdigital.in/app/smsapi/index.php"
        self.ask_username = True
        self.ask_password = True
        self.ask_message = True
        self.ask_number = True

    def send_sms(self):
        os.system('cls')
        opts, args = getopt(
            sys.argv[1:], 
            "u:p:m:n:h", 
            ["username=", "password=", "message=", "number=", "help"]
        )

        for o, v in opts:
            if o in ("-h", "--help"):
                self.usage()
            elif o in ("-u", "--username"):
                self.username = v
                self.ask_username = False
            elif o in ("-p", "--password"):
                self.password = v
                self.ask_password = False
            elif o in ("-m", "--message"):
                self.message = v
                self.ask_message = False
            elif o in ("-n", "--number"):
                self.numbers = v
                self.ask_number = False

        self .message = '''Dear Parent, The Pass code for your child with Binayak Group of Institutions is {#var#}. Please keep the code secret and share with your known person if required. You have to share this code at college gate. Thanking you Binayak Group of Institutions.'''
        if self.ask_number:
            self.numbers = input("Enter Mobile numbers(comma-separated): ")

        encoded_message = urllib.parse.quote(self.message)

        config = configparser.ConfigParser()
        config.read("apiconfig.cnf")

        payload = {
            "username": config["credentials"]["username"],
            "password": config["credentials"]["password"],
            "key": config["api_settings"]["key"],
            "campaign": config["api_settings"]["campaign"],
            "routeid": config["api_settings"]["routeid"],
            "type": config["api_settings"]["type"],
            "msg": encoded_message,
            "contacts": self.numbers,
            "senderid": config["api_settings"]["senderid"],
            "time": "",
            "template_id": config["api_settings"]["template_id"],
            "pe_id": config["api_settings"]["pe_id"]
        }
        os.system('cls')
        try:
            response = requests.post(self.api_url, data=payload)
            if response.status_code == 200:
                print("SMS sent successfully!")
                print(f"Response: {response.text}")
            else:
                print(f"Failed to send SMS. HTTP Status: {response.status_code}")
                print(f"Response: {response.text}")
        except requests.RequestException as e:
            print("An error occurred while sending the SMS:", str(e))
            sys.exit(1)

    def usage(self):
        print("\t-h, --help:  View help")
        print("\t-u, --username: Username")
        print("\t-p, --password: Password")
        print("\t-n, --number: Numbers to send the SMS (comma-separated)")
        print("\t-m, --message: Message to send")
        sys.exit(1)



import os
import random
import string
from StudentDetails import StudentDetails
from SendSMS import SMSSender

class VisitorValidator:
    def generate_random_alphanumeric_code(self, length=6):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return code

    def fetch_student_details(self, search_value, search_by):
        student_details = StudentDetails()
        if search_by == "student_name":
            student_details.student_name = search_value
            status, student_list = student_details.load_do_by_student_name()
        elif search_by == "father_name":
            student_details.father_name = search_value
            status, student_list = student_details.load_do_by_father_name()
        else:
            print("Invalid search criteria.")
            return None

        if not student_list:
            print("No student found. Please try again.")
            return None
        return student_list[0]

    def send_sms(self, phone_numbers, student_name, code):
        sms_sender = SMSSender()
        message = (
            f"Dear Parent, The Pass code for your child {student_name} with Binayak Group of Institutions is {code}. "
            "Please keep the code secret and share it only with authorized persons. "
            "Thank you, Binayak Group of Institutions."
        )

        for phone_number in phone_numbers:
            sms_sender.numbers = phone_number
            sms_sender.message = message
            try:
                sms_sender.sms_sender()
                print(f"Code sent successfully to {phone_number}")
            except Exception as e:
                print(f"Failed to send the SMS to {phone_number}: {str(e)}")

    def process_visitor_request(self):
        os.system('cls')
        print("1. Search by Student Name")
        print("2. Search by Father's Name")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == "1":
            search_by = "student_name"
            search_value = input("Enter the name of the student you're looking for: ").strip()
        elif choice == "2":
            search_by = "father_name"
            search_value = input("Enter the name of the student's father: ").strip()
        else:
            print("Invalid choice. Please restart the process.")
            return

        student = self.fetch_student_details(search_value, search_by)

        if not student:
            return

        code = self.generate_random_alphanumeric_code()

        phone_numbers = []
        if student.primary_no:
            phone_numbers.append(student.primary_no)
        if student.secondary_no:
            phone_numbers.append(student.secondary_no)

        if not phone_numbers:
            print("No valid phone numbers found for the student.")
            return

        self.send_sms(phone_numbers, student.student_name, code)
