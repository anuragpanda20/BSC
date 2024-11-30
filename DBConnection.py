import MySQLdb

class DBConnect:
    def __init__(self):
        self.db_connect = ''
        self.cursor = ''
    def connect_and_get_cursor(self):
        #print("Making one db connection")
        #db_connect = ''
        #try:
        db_connect = MySQLdb.connect(read_default_file=r"C:\Users\LENOVO\OneDrive\Documents\codes\BSC_Development\dbconf.cnf")
        #except MySQLdb.Error, e:
            #print "Error %d: %s" % (e.args[0], e.args[1])
            #exit
            #raise JConstants.DBConnectError
        self.cursor = db_connect.cursor()
        self.db_connect = db_connect
        return self.cursor

    def commit_and_close_connection(self):
        self.cursor.close()
        self.db_connect.commit()
        self.db_connect.close()
    def commit(self):
        self.db_connect.commit()
        return
    def rollback(self):
        self.db_connect.rollback()
        return
    
