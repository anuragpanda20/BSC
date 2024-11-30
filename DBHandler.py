import DBConnection

dbhandler = DBConnection.DBConnect()
cursor = dbhandler.connect_and_get_cursor()

def commit():
    dbhandler.commit()

def commit_and_close_connection():
    dbhandler.commit_and_close_connection()

def rollback():
    dbhandler.rollback()
