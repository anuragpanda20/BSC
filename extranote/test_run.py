from MessageTemplates import template, templates_type

class SendSMS:
    def __init__(self):
        """
        Initialize the SMSSender object with default values.
        """
        self.mobile_no = None
        self.message = None

    def compose_message(self, message_type, template_data):
        template_id = templates_type.get(message_type)
        if not template_id:
            raise ValueError(f"Invalid message type: {message_type}")

        message_template = template.get(template_id)
        if not message_template:
            raise ValueError(f"Template ID '{template_id}' not found.")

        message_content = message_template
        for key, value in template_data.items():
            message_content = message_content.replace(f"{{#{key}#}}", value)

        self.message = message_content

    def send_sms(self, message_type):
        if not self.mobile_no:
            raise ValueError("Mobile number is not set.")
        if not self.message:
            raise ValueError("Message content is not prepared.")
        print(f"Sending SMS to {self.mobile_no}:")
        print(self.message)

if __name__ == "__main__":
    sms_sender = SendSMS()

    mobile_no = "9876543210"
    sms_sender.mobile_no = mobile_no

    template_data = {"var": "123456"}
    sms_sender.prepare_message("MESSAGE_TYPE_VISITOR_AUTH", template_data)

    sms_sender.send_sms("MESSAGE_TYPE_VISITOR_AUTH")
