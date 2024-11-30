import MySQLdb
import DBHandler as db
import DConstants

class UserDetails:
    def __init__(self):
        self.user_id = 0
        self.user_name = None
        self.user_password = None
        self.permission = 0

    def insert_record(self):
            sql = "insert into bsc.user_details(user_id,user_name,user_status,user_password,permission) values ('%s','%s','%s','%s')" %\
            (self.user_id,self.user_name,self.user_password,self.permission)
            try:
                db.cursor.execute(sql)
                #db.commit()
                #return True
            except MySQLdb.IntegrityError as e:
                errorcode = e.args[0]
                if errorcode == 1062:
                    print("Duplicate entry error.")
                    return False
            except MySQLdb.Error as e:
                print("Database error:", e)
                return False
            
            return True
    
    def load_user(self):
        sql = "SELECT user_id, user_name, user_password, permission FROM bsc.user_details WHERE BINARY user_name = '%s'" %(self.user_name)
        try:
            db.cursor.execute(sql)
            user = db.cursor.fetchone()
                        
        except MySQLdb.Error as e:
            print(f"Database error: {e}")
            return False
        if db.cursor.rowcount == 0:
            return DConstants.RC_INVALID_USER_NAME
        self.user_id = user[0]
        self.user_name = user[1]
        self.user_password = user[2]
        self.permission = user[3]
        return True

