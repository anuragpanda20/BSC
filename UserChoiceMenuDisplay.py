import os
from tabulate import tabulate
import DConstants
from StudentDetails import StudentDetails
from StudentCode import StudentCode
from UserChoiceHandler import CodeVerification
from SendSMS import SendSMS
from SendVisitorCode import SendVisitorCode
from StudentLeaveOrMeetManager import StudentLeaveOrMeetManager

class VerificationMenu:
    def __init__(self):
        student_details = StudentDetails()
        student_code = StudentCode()
        
    def show_verification_menu(self):
        os.system('cls')
        while True:
            print("How do you want to verify?")
            print("1 - Verify by Student Name")
            print("2 - Verify by Student ID")
            print("3 - Verify by Father Name")
            print("4 - Verify by Primary Phone Number")
            print("9 - Return to Main Menu")
            print("0 - Exit")
            
            choice = input("Enter your choice: ")
            os.system('cls')
            code_verification = CodeVerification()
            if choice == "1":
                user_choice_data = input("Enter the student's name: ")
                rc,student_list = code_verification.verify_by_student_name(user_choice_data)
                if rc == DConstants.RC_CALL_SUCCESS:
                    if len(student_list) == 1:
                        self.student_details = student_list[0]
                        for key, value in self.student_details.items():
                          print(f"{key}: {value}")
                    elif len(student_list) > 1:
                        headers = ["Serial No"] + list(student_list[0].keys())
                        rows = [[idx + 1] + list(student.values()) for idx, student in enumerate(student_list)]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                        
                        try:
                            user_record_no = int(input("Enter the record no: "))
                            if 1 <= user_record_no <= len(student_list):
                                self.student_details = student_list[user_record_no - 1]
                            else:
                                print("Invalid record number. Please try again.")
                                return
                        except ValueError:
                            print("Please enter a valid number.")
                            return
                        os.system('cls')
                        headers = self.student_details.keys()
                        rows = [self.student_details.values()]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                else:
                    print("No student found!")
                    break
            elif choice == "2":
                user_choice_data = input("Enter the student's ID: ")
                rc,student_list = code_verification.verify_by_student_id(user_choice_data)
                if rc == DConstants.RC_CALL_SUCCESS:
                    self.student_details = student_list[0]
                    for key, value in self.student_details.items():
                        print(f"{key}: {value}")       
                else:
                    print("No student found!")
                    break
            elif choice == "3":
                user_choice_data = input("Enter the student's father name: ")
                rc,student_list = code_verification.verify_by_father_name(user_choice_data)
                if rc == DConstants.RC_CALL_SUCCESS:
                    if len(student_list) == 1:
                        self.student_details = student_list[0]
                        for key, value in self.student_details.items():
                          print(f"{key}: {value}")
                    elif len(student_list) > 1:
                        headers = ["Serial No"] + list(student_list[0].keys())
                        rows = [[idx + 1] + list(student.values()) for idx, student in enumerate(student_list)]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                        
                        try:
                            user_record_no = int(input("Enter the record no: "))
                            if 1 <= user_record_no <= len(student_list):
                                self.student_details = student_list[user_record_no - 1]
                            else:
                                print("Invalid record number. Please try again.")
                                return
                        except ValueError:
                            print("Please enter a valid number.")
                            return
                        os.system('cls')
                        headers = self.student_details.keys()
                        rows = [self.student_details.values()]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                else:
                    print("No student found!")
                    break
            elif choice == "4":
                user_choice_data = input("Enter student's primary no: ")
                rc,student_list = code_verification.verify_by_primary_no(user_choice_data)
                if rc == DConstants.RC_CALL_SUCCESS:
                    if len(student_list) == 1:
                        self.student_details = student_list[0]
                        for key, value in self.student_details.items():
                          print(f"{key}: {value}")
                    elif len(student_list) > 1:
                        headers = ["Serial No"] + list(student_list[0].keys())
                        rows = [[idx + 1] + list(student.values()) for idx, student in enumerate(student_list)]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                        
                        try:
                            user_record_no = int(input("Enter the record no: "))
                            if 1 <= user_record_no <= len(student_list):
                                self.student_details = student_list[user_record_no - 1]
                            else:
                                print("Invalid record number. Please try again.")
                                return
                        except ValueError:
                            print("Please enter a valid number.")
                            return
                        os.system('cls')
                        headers = self.student_details.keys()
                        rows = [self.student_details.values()]
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                else:
                    print("No student found!")
                    break
            elif choice == "9":
                os.system('cls')
                break
            elif choice == "0":
                os.system('cls')
                exit()
            else:
                print("Invalid choice. Please try again.")
                
            confirm = input("Want to verify code (y/n): ").strip().lower()
            if confirm == 'y':
                os.system('cls')
                student_code = input("Enter student code: ").strip()
                rc, self.student_code = code_verification.load_student_active_code(self.student_details['Student ID'])
                os.system('cls')
                if self.student_code == student_code:
                    print("Code Validated successfully.")
                    input("Press any key for visitor verification option: ")
                    os.system('cls')
                    confirm = input("Do you want to verify the visitor code? (y/n): ").strip().lower()
                    if confirm == 'y':
                        os.system('cls')
                        visitor = SendVisitorCode()
                        rc = visitor.visitor_code_verification(self.student_details['Student ID'])
                        visitor_code = input("Enter the code provided by visitor: ")
                        if rc == DConstants.RC_CALL_SUCCESS:
                            if visitor_code == visitor.visitor_code:
                                os.system('cls')
                                print("Visitor code Validated successfully")
                                os.system('cls')
                                choice = input("Do you want to record the leave or meet details? (y/n): ").strip().lower()
                                if choice == 'y':
                                    os.system('cls')
                                    student_id = self.student_details['Student ID']
                                    student_leave_or_meet = StudentLeaveOrMeetManager(student_id)
                                    student_leave_or_meet.leave_or_meet_manager()
                                else:
                                    continue
                            else:
                                os.system('cls')
                                print("Sorry, code didn't match")
                                input("Press any key to continue: ")
                                os.system('cls') 
                                continue
                    else:
                        os.system('cls')
                        choice = input("Do you want to record the leave or meet details? (y/n): ").strip().lower()
                        if choice == 'y':
                            os.system('cls')
                            student_id = self.student_details['Student ID']
                            student_leave_or_meet = StudentLeaveOrMeetManager(student_id)
                            student_leave_or_meet.leave_or_meet_manager()
                        else:
                            os.system('cls')
                            continue  
                else:
                    print("Sorry, code didn't match")
                    input("Press any key to continue: ")
                    os.system('cls') 
                    continue
            else:
                os.system('cls')
                continue