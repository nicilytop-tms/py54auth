from auth_system.authentication_service import AuthSystem
from registration_system.registration_service import RegistrationSystem


class App:
    MENU = {
        "login": AuthSystem.auth,
        "register": RegistrationSystem.sign_up,
        "exit": None,
    }

    def run(self):
        command = input("Your choice please (login | register | exit)")
        try:
            do = self.MENU[command]
            do()
        except KeyError:
            print("Unknown command try again next time")


app = App()
app.run()
