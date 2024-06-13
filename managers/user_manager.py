from instances.user import User


class UserManager:
    class_user = User

    def get_users(self, storage): ...

    def find_by_email(self, users, email): ...

    def create_user(self, email, password):
        return self.class_user(email, password)
