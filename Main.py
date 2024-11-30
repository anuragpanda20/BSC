from Landing import UserLogin
from UserMainMenuDisplay import ShowMenu
import DConstants

class Main:
    def run(self):
        print("Welcome to the Application")
        user = UserLogin()
        rc = user.user_login()
        if rc == DConstants.RC_USER_LOGIN_SUCCESS:
            show_menu = ShowMenu()
            show_menu.show_menu()
        else:
            print("Invalid username or password.")

if __name__ == "__main__":
    app = Main()
    app.run()