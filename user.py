from faker import Faker

fake = Faker()


def get_user():
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
    return [fake.name() for _ in range(n)]


if __name__ == "__main__":
    users = get_users(15)
    print(users)
