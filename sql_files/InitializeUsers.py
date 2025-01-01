from src.User import User


def initialize_users():
    User.create_user("louise", "louise", "Louise")
    User.create_user("max", "max", "Max")


if __name__ == '__main__':
    initialize_users()
