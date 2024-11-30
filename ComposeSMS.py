import urllib.parse
from StudentDetails import StudentDetails
from MessageTemplates import templates_type, template
import DConstants


class ComposeSMS:
    def validate_mobile_no(self, student_id):
        student_details = StudentDetails()
        status_code, phone_numbers = student_details.fetch_phone_numbers(student_id)

        if status_code != DConstants.RC_CALL_SUCCESS or not phone_numbers:
            print(f"Error: No valid phone numbers found for student_id {student_id}.")
            return DConstants.RC_INVALID_PRIMARY_NO, []
        
        return DConstants.RC_CALL_SUCCESS, phone_numbers

    def validate_sms(self, sms_type):
        template_id = templates_type.get(sms_type)
        if not template_id:
            print(f"Error: Invalid SMS type '{sms_type}'.")
            return None

        sms_template = template.get(template_id)
        if not sms_template:
            print(f"Error: No template found for template_id '{template_id}'.")
            return None

        return sms_template

    def compose_sms(self, sms_template, params):
        message = sms_template
        for key, value in params.items():
            placeholder = f"{{#{key}#}}"
            message = message.replace(placeholder, str(value))

        if "{#var#}" in message:
            print("Error: Missing parameters for placeholders in the SMS template.")
            return None

        return message