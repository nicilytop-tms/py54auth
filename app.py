from auth_system.authentication_service import AuthSystem
from registration_system.registration_service import RegistrationSystem


class App:
    MENU = {
        "login": AuthSystem.auth,
        "register": RegistrationSystem.sign_up,
    }

    def run(self):
        command = input("Your choice please (login | register)")
        do = self.MENU[command]
        do()


app = App()
app.run()
