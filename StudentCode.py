import MySQLdb
import DBHandler as db
import DConstants

class StudentCode:
    def __init__(self):
        self.student_id = None
        self.student_code = None
        self.student_status = 0

    def insert_record(self):
            sql = "insert into bsc.student_code(student_id,student_code,student_status) values ('%s','%s','%s')" %\
            (self.student_id,self.student_code,self.student_status)
            try:
                db.cursor.execute(sql)
                #db.commit()
                return True
            except MySQLdb.IntegrityError as e:
                errorcode = e.args[0]
                if errorcode == 1062:
                    print("Duplicate entry error.")
                    return False
            except MySQLdb.Error as e:
                print("Database error:", e)
                return False
            
            return True
    
    def load_by_student_id(self):

        sql = "select student_id, student_code, student_status from bsc.student_code where student_id='%s'" %(self.student_id)
              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_STUDENT_ID, None 
        
        record = db.cursor.fetchone()

        student = StudentCode()
        student.student_id = record[0]
        student.student_code = record[1]
        student.student_status = record[2]

        return DConstants.RC_CALL_SUCCESS, student