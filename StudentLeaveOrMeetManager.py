import os
import DBHandler as db
from StudentLeaveOrMeetInfo import StudentLeaveOrMeetInfo
from StudentLeaveOrMeetData import StudentLeaveOrMeetData

class StudentLeaveOrMeetManager:
    def __init__(self, student_id):
        self.student_id = student_id
        self.manager = StudentLeaveOrMeetData()
    def leave_or_meet_manager(self):
        while True:
            print("Menu:")
            print("Choose the option as required")
            print("1. Student Meeting")
            print("2. Student Leave after meeting")
            print("3. Student Leave")
            print("4. Student Join")
            print("5. Short Term Leave")
            print("6. Visitor Exit")
            print("0. Main Menu")
            choice = input("Enter your choice: ").strip()
            os.system('cls')

            if choice == "1":
                self.manager.student_meeting(self.student_id)
            elif choice == "2":
                self.manager.student_leave_after_meet(self.student_id)
            elif choice == "3":
                self.manager.student_leave(self.student_id)
            elif choice == "4":
                self.manager.student_join(self.student_id)
            elif choice == "5":
                self.manager.short_term_leave(self.student_id)
            elif choice == "6":
                self.manager.visitor_exit(self.student_id)
            elif choice == "0":
                db.commit_and_close_connection()
                break
            else:
                print("Invalid choice. Please try again.")