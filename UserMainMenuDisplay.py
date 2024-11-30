import os
import MySQLdb
import DBHandler as db
import DConstants
from UserChoiceMenuDisplay import VerificationMenu
from FetchStudentCode import FetchStudentCode
from SendSMS import SendSMS
from SendVisitorCode import SendVisitorCode
from SendStudentInfo import SendStudentInfo

class ShowMenu:
    def show_menu(self):
        os.system('cls')
        while True:
            print("Main Menu:")
            print("1. Send New Code")
            print("2. Resend Code to Specific Student")
            print("3. Code Verification")
            print("0. Exit")
            choice = input("Enter Your Choice: ")
            
            if choice == "1":
                info = SendStudentInfo()
                info.send_info()
            elif choice == "2":
                print("Resending code")
                continue
            elif choice == "3":
                verification = VerificationMenu()
                verification.show_verification_menu()
            elif choice == "0":
                os.system('cls')
                break
            else:
                print("Invalid choice. Please try again.")

