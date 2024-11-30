import MySQLdb
import DBHandler as db
import DConstants

class StudentDetails:
    def __init__(self):
        self.si_no = 0
        self.student_id = None
        self.student_name = None
        self.hostel_id = 0
        self.father_name = None
        self.mother_name = None
        self.primary_guardian = None
        self.primary_no = None
        self.secondary_no = None
        self.student_status = 0
        self.email_id = None

    def insert_record(self):
            sql = "insert into bsc.student_details(student_id,student_name,hostel_id,father_name,mother_name,primary_guardian,primary_no,secondary_no,student_status,email_id) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %\
            (self.student_id,self.student_name,self.hostel_id,self.father_name,self.mother_name,self.primary_guardian,self.primary_no,self.secondary_no,self.student_status,self.email_id)
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
    
    def load_do_by_student_name(self):

        sql = "select student_id, student_name, father_name, primary_no, student_status from bsc.student_details where student_name like '%s%%'" %(self.student_name)

              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_STUDENT_NAME,[]

        student_list = []
        data = db.cursor.fetchall()

        for record in data:
            st = StudentDetails()
            st.student_id = record[0]
            st.student_name = record[1]
            st.father_name = record[2]
            st.primary_no = record[3]
            st.student_status=record[4]
            student_list.append(st)
        return DConstants.RC_CALL_SUCCESS, student_list
    
    def load_do_by_student_id(self):

        sql = "select student_id, student_name, father_name, primary_no, student_status from bsc.student_details where student_id='%s' " %(self.student_id)
              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_STUDENT_ID, [] 
        student_list = []
        data = db.cursor.fetchone()
        st = StudentDetails()
        st.student_id = data[0]
        st.student_name = data[1]
        st.father_name = data[2]
        st.primary_no = data[3]
        st.student_status = data[4]

        student_list = [st]

        return DConstants.RC_CALL_SUCCESS, student_list
    
    def load_do_by_father_name(self):

        sql = "select student_id, student_name, father_name, primary_no, student_status from bsc.student_details where father_name like '%s%%'"  %(self.father_name)
              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_FATHER_NAME,[]

        student_list = []
        data = db.cursor.fetchall()

        for record in data:
            st = StudentDetails()
            st.student_id = record[0]
            st.student_name = record[1]
            st.father_name = record[2]
            st.primary_no = record[3]
            st.student_status=record[4]
            student_list.append(st)
        return DConstants.RC_CALL_SUCCESS, student_list
    
    def load_do_by_primary_no(self):

        sql = "select student_id, student_name, father_name, primary_no, secondary_no, student_status from bsc.student_details where primary_no='%s'" %(self.primary_no)
              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_PRIMARY_NO,[]

        student_list = []
        data = db.cursor.fetchall()

        for record in data:
            st = StudentDetails()
            st.student_id = record[0]
            st.student_name = record[1]
            st.father_name = record[2]
            st.primary_no = record[3]
            st.secondary_no = record[3]
            st.student_status=record[4]
            student_list.append(st)
        return DConstants.RC_CALL_SUCCESS, student_list
    
    def load_do_by_secondary_no(self):

        sql = """SELECT student_id, student_name, father_name, primary_no, secondary_no, student_status FROM bsc.student_details WHERE primary_no = '%s' OR secondary_no = '%s' """ % (self.primary_no, self.primary_no)
              
        try:
            db.cursor.execute(sql)
            #DBHandler.commit()
        except MySQLdb.Error as e:
            return False,[]

        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_PRIMARY_NO,[]

        student_list = []
        data = db.cursor.fetchall()

        for record in data:
            st = StudentDetails()
            st.student_id = record[0]
            st.student_name = record[1]
            st.father_name = record[2]
            st.secondary_no_no = record[3]
            st.student_status=record[4]
            student_list.append(st)
        return DConstants.RC_CALL_SUCCESS, student_list
    
    def fetch_phone_numbers(self, student_id):
    
        sql = "SELECT primary_no, secondary_no FROM student_details WHERE student_id = '%s'" % (student_id)
        
        try:
            db.cursor.execute(sql)
        except MySQLdb.Error as e:
            print(f"Database Error: {e}")
            return False, []
        
        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_STUDENT_ID, []

        data = db.cursor.fetchone()
        phone_numbers = []

        if data[0]:
            phone_numbers.append(data[0])
        if data[1]: 
            phone_numbers.append(data[1])

        return DConstants.RC_CALL_SUCCESS, phone_numbers

