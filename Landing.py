import getpass
import DConstants
from UserAuthentication import UserAuthentication

class UserLogin:
    def user_login(self):
        authenticator = UserAuthentication()
        
        user_name = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        rc = authenticator.check_credentials(user_name, password)
        
        return rc
