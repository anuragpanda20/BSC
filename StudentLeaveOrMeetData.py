import os
import MySQLdb
import DBHandler as db
from datetime import datetime
from StudentLeaveOrMeetInfo import StudentLeaveOrMeetInfo

class StudentLeaveOrMeetData:
    def __init__(self):
        self.student = StudentLeaveOrMeetInfo()

    def student_meeting(self,student_id):
        self.student.student_id = student_id
        self.student.card_id = input("Enter the card_id: ")
        self.student.leave_or_meet_date = datetime.now()
        sql = """ INSERT INTO StudentLeaveOrMeetInfo 
        (student_id, card_id, leave_or_meet_date) VALUES ('%s', '%s', '%s') """ % (self.student.student_id, self.student.card_id, self.student.leave_or_meet_date)
        try:
            db.cursor.execute(sql)
            print(sql)
            db.commit()
            os.system('cls')
            print("Record inserted successfully!")
            self.student.display_record()
            return True
        except MySQLdb.IntegrityError as e:
            errorcode = e.args[0]
            if errorcode == 1062:
                print("Duplicate entry error.")
                return False
        except MySQLdb.Error as e:
            print("Database error:", e)
            return False
      
    def student_leave_after_meet(self,student_id):
        self.student.student_id = student_id
        card_id = input("Enter the card_id: ")
        self.leave_or_meet_date = datetime.now()
        self.reason = input("Enter the purpose of leave: ")
        expected_return_date = input("Enter the expected return date (YYYY-MM-DD): ")
        self.expected_return_date = datetime.strptime(expected_return_date, "%Y-%m-%d")
        card_id = input("Enter the card_id: ")
        if self.student.card_id == card_id:
            sql = """ 
            UPDATE StudentLeaveOrMeetInfo 
            SET reason = '%s', leave_or_meet_date = '%s', expected_return_date = '%s'
            WHERE student_id = '%s' AND card_id = '%s'
            """ % (self.reason, self.leave_or_meet_date, self.expected_return_date, self.student.student_id, card_id)

            try:
                db.cursor.execute(sql)
                db.commit()
                print("Leave record successfully updated.")
                self.student.display_record()
                return True

            except MySQLdb.IntegrityError as e:
                errorcode = e.args[0]
                if errorcode == 1062:
                    print("Duplicate entry error.")
                    return False
            except MySQLdb.Error as e:
                print("Database error:", e)
                return False
        else:
            print("Invalid card ID.")
            return 

    def student_leave(self,student_id):
        self.student.student_id = student_id
        self.reason = input("Enter the purpose of leave: ")
        self.leave_or_meet_date = datetime.now()
        expected_return_date = input("Enter the expected return date (YYYY-MM-DD): ")
        self.expected_return_date = datetime.strptime(expected_return_date, "%Y-%m-%d")
        card_id = input("Enter the card_id: ")
        self.student.card_id = card_id
        sql = """ INSERT INTO StudentLeaveOrMeetInfo 
            (student_id, card_id, reason, leave_or_meet_date, expected_return_date) 
            VALUES ('%s', '%s', '%s', '%s', '%s') """ % (self.student.student_id, self.student.card_id, self.reason, self.leave_or_meet_date, self.expected_return_date)
        try:
            db.cursor.execute(sql)
            db.commit()
            print("Leave record successfully updated.")
            self.student.display_record()
            return True

        except MySQLdb.IntegrityError as e:
            errorcode = e.args[0]
            if errorcode == 1062:
                print("Duplicate entry error.")
                return False
        except MySQLdb.Error as e:
            print("Database error:", e)
            return False
        
    def student_join(self, student_id):
        self.student.student_id = student_id
        self.student.card_id = self.student.fetch_card_id(self.student.student_id)

        query = f"""
        SELECT expected_return_date 
        FROM StudentLeaveOrMeetInfo 
        WHERE student_id = '{self.student.student_id}' AND actual_return_date IS NULL
        """
        db.cursor.execute(query)
        result = db.cursor.fetchone()
        if result:
            actual_return_date = input("Enter the expected return date (YYYY-MM-DD): ")
            self.actual_return_date = datetime.strptime(actual_return_date, "%Y-%m-%d")
            expected_return_date = result[0]
            current_datetime = datetime.now()
            update_query = f"""
            UPDATE StudentLeaveOrMeetInfo 
            SET actual_return_date = '{self.actual_return_date}' 
            WHERE student_id = '{self.student.student_id}' AND actual_return_date IS NULL
            """
            try:
                db.cursor.execute(update_query)
                db.commit()

                if expected_return_date:
                    difference = (self.actual_return_date.date() - expected_return_date.date()).days
                    if difference > 0:
                        remark = input("Enter the reason for the delay: ")
                    else:
                        remark = None

                    if remark:
                        update_remark_query = f"""
                        UPDATE StudentLeaveOrMeetInfo 
                        SET remark = '{remark}' 
                        WHERE student_id = '{self.student.student_id}' AND actual_return_date = '{self.actual_return_date}'
                        """
                        db.cursor.execute(update_remark_query)
                        db.commit()

                print("Record successfully updated with the actual return date")
                self.student.display_record()
            except Exception as e:
                print(f"Error while updating the record: {e}")
        else:
            print("No record found")


    def short_term_leave(self,student_id):
        pass

    def visitor_exit(self,student_id):
        self.student.student_id = student_id
        self.student.card_id = self.student.fetch_card_id(self.student.student_id)
        
        if not self.student.card_id:
            print("No card ID found for this student.")
            return False

        visitor_exit_time = datetime.now()
        update_query = f"""
        UPDATE StudentLeaveOrMeetInfo 
        SET visitor_exit_time = '{visitor_exit_time}'
        WHERE student_id = '{self.student.student_id}' AND card_id = '{self.student.card_id}' AND visitor_exit_time IS NULL
        """

        try:
            db.cursor.execute(update_query)
            db.commit()
            print(f"Visitor exit time successfully updated for student {self.student.student_id} and card {self.student.card_id}.")
            self.student.display_record()
            return True
        except Exception as e:
            print(f"Error while updating visitor exit time: {e}")
            return False

        