import DConstants
from StudentDetails import StudentDetails
from StudentCode import StudentCode

class FetchStudentCode:
    def get_student_code(self, phone_number):
            try:
                student_details = StudentDetails()
                student_details.primary_no = phone_number

                status, student_list = student_details.load_do_by_primary_no()

                if status != DConstants.RC_CALL_SUCCESS or not student_list:
                    print(f"No student found for phone number: {phone_number}")
                    return None

                student_id = student_list[0].student_id

                student_code_obj = StudentCode()
                student_code_obj.student_id = student_id

                status, student = student_code_obj.load_by_student_id()

                if status != DConstants.RC_CALL_SUCCESS or not student:
                    print(f"No student_code found for student_id: {student_id}")
                    return None

                return student.student_code
            except Exception as e:
                print("An error occurred while fetching the student_code:", str(e))
                return None
            
            