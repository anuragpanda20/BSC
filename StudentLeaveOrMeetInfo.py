import os
import MySQLdb
import DBHandler as db
from tabulate import tabulate


class StudentLeaveOrMeetInfo:
    def __init__(self):
        self.student_id = None
        self.card_id = None
        self.reason = None
        self.leave_or_meet_date = None
        self.expected_return_date = None
        self.actual_return_date = None
        self.visitor_exit_time = None
        self.remark = None

    def display_record(self):
        #print(self.student_id,self.card_id)
        query = f"SELECT * FROM StudentLeaveOrMeetInfo WHERE student_id = '{self.student_id}' AND card_id = '{self.card_id}'"
        db.cursor.execute(query)
        rows = db.cursor.fetchall()

        if rows:
            headers = ["Student ID", "Card_ID", "Leave/Meet Reason", "Leave/Meet Date", "Expected Return Date", "Actual Return Date", "Visitor_Exit_Time", "Remarks"]
            table = tabulate(rows, headers, tablefmt="grid")
            print("Record Details:")
            print(table)
        else:
            print("No record found")

    def fetch_card_id(self, student_id):
        query = f"SELECT card_id FROM StudentLeaveOrMeetInfo WHERE student_id = '{student_id}'"
        db.cursor.execute(query)
        result = db.cursor.fetchone()

        if result:
            return result[0]
        else:
            print(f"No card_id found for student_id: {student_id}")
        return None
