import random
import string
import MySQLdb
import DBHandler as db

class StudentCodeGenerator:
    def __init__(self):
        self.existing_codes = set()  

    def generate_random_code(self):
        """Generate a unique 6-character random alphanumeric code."""
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return code

    def is_code_existing(self, code):
        """Check if the student_code already exists in the database."""
        sql = "SELECT COUNT(*) FROM bsc.student_code WHERE student_code = %s"
        try:
            db.cursor.execute(sql, (code,))
            result = db.cursor.fetchone()
            return result[0] > 0  
        except MySQLdb.Error as e:
            print("Error checking for existing code:", e)
            return True  

    def insert_student_code(self):
        """Generate a unique student_code for each student and insert into the table."""
        sql = "SELECT student_id FROM bsc.student_code WHERE student_code IS NULL"  
        try:
            db.cursor.execute(sql)
            students = db.cursor.fetchall()

            for student_record in students:
                student_id = student_record[0]
                student_code = self.generate_random_code()  

                while self.is_code_existing(student_code):
                    print(f"Code {student_code} already exists, generating a new one.")
                    student_code = self.generate_random_code() 

                update_sql = "UPDATE bsc.student_code SET student_code = %s WHERE student_id = %s"
                db.cursor.execute(update_sql, (student_code, student_id))
                db.commit()

                print(f"Inserted Student ID {student_id} with Code {student_code}")

        except MySQLdb.Error as e:
            print("Error fetching students:", e)

