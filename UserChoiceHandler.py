from StudentDetails import StudentDetails
from StudentCode import StudentCode
import DConstants

class CodeVerification:
    def __init__(self):
        pass

    def verify_by_student_name(self,student_name):
        student_details = StudentDetails()
        student_details.student_name = student_name
        found, student = student_details.load_do_by_student_name()

        student_data_list = []
        
        if found == DConstants.RC_CALL_SUCCESS:
            for student in student:
                student_data = {
                    "Student ID": student.student_id,
                    "Name": student.student_name,
                    "Father's Name": student.father_name,
                    "Primary Contact No": student.primary_no,
                    "Status": student.student_status
                }
                student_data_list.append(student_data)

            return DConstants.RC_CALL_SUCCESS,student_data_list
        else:
            return DConstants.RC_INVALID_STUDENT_NAME, []
    
    def verify_by_student_id(self,student_id):
        student_details = StudentDetails()
        student_details.student_id = student_id
        found, students = student_details.load_do_by_student_id()

        student_data_list = []
        
        if found == DConstants.RC_CALL_SUCCESS:
            for student in students:
                student_data = {
                    "Student ID": student.student_id,
                    "Name": student.student_name,
                    "Father's Name": student.father_name,
                    "Primary Contact No": student.primary_no,
                    "Status": student.student_status
                }
                student_data_list.append(student_data)

            return DConstants.RC_CALL_SUCCESS,student_data_list
        else:
            return DConstants.RC_INVALID_STUDENT_ID, []


    def verify_by_father_name(self,father_name):
        student_details = StudentDetails()
        student_details.father_name = father_name
        found, students = student_details.load_do_by_father_name()
        
        student_data_list = []

        if found == DConstants.RC_CALL_SUCCESS:
            for student in students:
                student_data = {
                    "Student ID": student.student_id,
                    "Name": student.student_name,
                    "Father's Name": student.father_name,
                    "Primary Contact No": student.primary_no,
                    "Status": student.student_status
                }
                student_data_list.append(student_data)

            return DConstants.RC_CALL_SUCCESS,student_data_list
        else:
            return DConstants.RC_INVALID_FATHER_NAME, []

    def verify_by_primary_no(self,primary_no):
        student_details = StudentDetails()
        student_details.primary_no = primary_no
        found, students = student_details.load_do_by_primary_no()
        
        student_data_list = []
        if found == DConstants.RC_CALL_SUCCESS:
            for student in students:
                student_data = {
                    "Student ID": student.student_id,
                    "Name": student.student_name,
                    "Father's Name": student.father_name,
                    "Primary Contact No": student.primary_no,
                    "Status": student.student_status
                }
                student_data_list.append(student_data)
            
            return DConstants.RC_CALL_SUCCESS,student_data_list
        else:
            return DConstants.RC_INVALID_PRIMARY_NO, []

    def load_student_active_code(self,student_id):
        studentcode = StudentCode()
        studentcode.student_id = student_id
        found, student = studentcode.load_by_student_id()  # it's expecting a single object, not a list.

        if found == DConstants.RC_CALL_SUCCESS:
            return DConstants.RC_CALL_SUCCESS, student.student_code
        else:
            return DConstants.RC_INVALID_STUDENT_ID, None
