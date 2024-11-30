import MySQLdb
import DBHandler as db
import DConstants
from UserDetails import UserDetails
from UserPassword import UserPassword

class UserAuthentication:
    def __init__(self):
        self.permission = 0
        self.user_full_name = None
        self.user_id = 0

    def check_credentials(self, user_name, password):
        user_detail = UserDetails()
        user_detail.user_name = user_name
        rc = DConstants.RC_CALL_SUCCESS
        rc = user_detail.load_user()
        if rc != DConstants.RC_CALL_SUCCESS:
            return rc
        if user_detail.user_password != password:
            return DConstants.RC_INVALID_PASSWORD

        #self.user_full_name = user_detail.user_full_name
        #self.user_id = user_detail.user_id 
        #self.permission = user_detail.permission
        
        return DConstants.RC_USER_LOGIN_SUCCESS

