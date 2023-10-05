"""Module to generate random users."""
from faker import Faker
import logging
from pathlib import Path

fake = Faker()
BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.INFO)


def get_user():
    """Generate once user
        :arg: None
        :return fake username
    """
    logging.debug("Generating user.")
    return f"{fake.unique.first_name()} {fake.unique.last_name()}"


def get_users(n):
    """Generate users
        :arg: Number of fake users
        :return fake users
    """
    logging.info(f"generating a list of {n} users.")
    return [fake.unique.name() for _ in range(n)]


if __name__ == "__main__":
    users = get_users(15)
    print(users)
