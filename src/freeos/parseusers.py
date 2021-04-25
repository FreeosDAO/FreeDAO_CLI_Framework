import json
import sys

from src.configs.config import USER_JSON
from src.configs.config_admin import PROTON


def parse_json(user_json):
    user_data = None
    try:
        with open(user_json, "r") as usf:
            print(dir(usf), type(usf))
            user_data = json.load(usf, strict=False)
    except Exception as exp:
        print(repr(exp))
        sys.exit()
    finally:
        return user_data


def create_unverified_user(username):
    print(f"Proton Path: {PROTON}")


class User(object):
    def __init__(self, username):
        self.username = username
        self.password = None
        self.walletfile = None

    def unlock_wallet(self):
        if not self.password:
            with open(f"{self.username}.psw", "r") as wpass:
                self.password = wpass.readline()
        print(f"Wallet Password: {self.password}")
        cmd = f"{PROTON} wallet unlock -n proton_{self.username} --password {self.password}"
        print(f"Unlock command: {cmd}")

    def create_unverified_user(self):
        with open(f"{self.username}.psw", "w") as psw:
            psw.write("Secret123!")


if __name__ == '__main__':
    euser = "moshamosha"
    print(f"Parsing {USER_JSON}")
    create_unverified_user(euser)
    user = User(euser)
    user.create_unverified_user()
    user.unlock_wallet()

    # with open(USER_JSON, "r") as usf:
    #    print(dir(usf), type(usf))
    #    data = json.load(usf, strict=False)
