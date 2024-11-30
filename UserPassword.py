import sys
import MySQLdb
import DBHandler as db
from UserDetails import UserDetails

class UserPassword:
    def __init__(self):
        self.user_detail = UserDetails()
        self.user_name = None
        self.user_password = None

    def check_user_name(self):
        rc = self.user_detail.load_user()
        if rc == False:
            return False
        return True
    
    def check_password(self):
        if self.user_detail.user_password == self.user_password:
            return True
        else:
            return False
'''
    def login(self):
        if self.check_user_name() == False:
            return False

        if self.check_password() == True:
            return True
        else:
            return False
'''



