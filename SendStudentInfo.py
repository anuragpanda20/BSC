import os
import DConstants
from ComposeSMS import ComposeSMS
from SendSMS import SendSMS
from StudentDetails import StudentDetails
from StudentCode import StudentCode
from MessageTemplates import templates_type

class SendStudentInfo:
    def __init__(self):
        self.composer = ComposeSMS()
        self.sender = SendSMS()
        self.student_details = StudentDetails()
        self.student_code = StudentCode()

    def send_info(self):
        os.system('cls')
        print("Choose a message template:")
        template_mapping = {
            "MESSAGE_TYPE_STUDENT_CODE": "Student Passcode",
            "MESSAGE_TYPE_VISITOR_AUTH": "Visitor Access Code",
            "MESSAGE_TYPE_MARK": "Test Result"
        }
        for idx, (template_type, display_name) in enumerate(template_mapping.items(), start=1):
            print(f"{idx}. {display_name}")

        try:
            template_choice = int(input("Enter your choice: ").strip())
            if template_choice < 1 or template_choice > len(template_mapping):
                os.system('cls')
                print("Invalid choice.")
                return

            selected_template_key = list(template_mapping.keys())[template_choice - 1]
            selected_template = self.composer.validate_sms(selected_template_key)
            if not selected_template:
                print(f"No valid template found for type {selected_template_key}.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        os.system('cls')
        input_numbers = input("Enter phone numbers (comma-separated): ").strip()
        phone_numbers = [num.strip() for num in input_numbers.split(",") if num.strip()]
        if not phone_numbers:
            print("No valid phone numbers entered.")
            return

        for phone_number in phone_numbers:
            self.student_details.primary_no = phone_number
            status_code, student_list = self.student_details.load_do_by_primary_no()

            if status_code != DConstants.RC_CALL_SUCCESS or not student_list:
                print(f"No valid student found for phone number {phone_number}.")
                continue

            student = student_list[0]  
            student_id = student.student_id

            rc, contact_numbers = self.composer.validate_mobile_no(student_id)

            if not contact_numbers:
                print(f"No contact numbers available for student_id {student_id}.")
                continue

            self.student_code.student_id = student_id
            status_code, student_code_data = self.student_code.load_by_student_id()

            if status_code != DConstants.RC_CALL_SUCCESS or not student_code_data:
                print(f"No valid student code found for student_id {student_id}.")
                continue

            composed_message = self.composer.compose_sms(
                selected_template, {"var": student_code_data.student_code}
            )
            if not composed_message:
                print("Failed to compose message.")
                continue
            selected_template_id = templates_type.get(selected_template_key)
            self.sender.set_template_id(selected_template_id)
            for contact_number in contact_numbers:
                self.sender.send_sms([contact_number], composed_message)
      
        input("Press any key to continue: ")
        os.system('cls')
