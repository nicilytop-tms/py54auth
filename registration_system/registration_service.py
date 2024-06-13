from managers.user_manager import UserManager
from settings import JSON_STORAGE
from storage.json_storage import JsonStorage


class RegistrationSystem:
    storage = JsonStorage(JSON_STORAGE)
    user_manager = UserManager()

    @classmethod
    def sign_up(cls):
        email = input("Enter your email:")
        users = cls.user_manager.get_users(cls.storage)
        if cls.user_manager.find_by_email(users, email):
            # TODO: Create own exception
            raise ValueError

        password = input("Enter your password:")
        user = cls.user_manager.create_user(email, password)
        cls.storage.add_to_storage([user.dict_serialize()])
