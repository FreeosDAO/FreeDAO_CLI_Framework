from src.utils.utils import run as run
from src.utils.base_logger import logger
#from src.configs.config_admin import PROTON, WALLET_DIR
from src.configs.config_admin import *
from src.configs.config import USER_JSON, called_by
from src.configs.airclaim_cmd import *

import json
import sys


class GetUsers(object):
    def __init__(self, user_file = USER_JSON):
        self.user_file = user_file
        self.users = dict()

    def parse_users(self):
        try:
            with open(self.user_file) as ufile:
                self.users = json.load(ufile, strict = False)
            logger.debug(f"Parsed User Json: {self.user_file}")
        except Exception as exp:
            logger.error(f"Exception in parsing {self.user_file}" + str(repr(exp)))
        finally:
            return self.users

class BaseUser(object):
    def __init__(self, account=None):
        self.account=account
        self.wallet_password = None
        self.wallet=dict()
        self.iteration=0
        self.resources={'xpr':0,'freeos':0}
        self.claims={}
        self.stateFile=None #TODO: Pickle file to save the state of the object when needed

    def __repr__(self):
        return (f'User:{self.account}')
        
    def run(self, cmd):
        #return status, output, and error messages
        s,o,e = run(cmd)
        logger.debug(f"Status:{s}, {o} {e}")
        logger.debug(f"{called_by()}")
        return (s,o,e)

    def is_unlocked(self, account=None):
        if not account:
            account = self.account
        flag = False
        cmd = f"{PROTON} wallet list"
        s, o, e = run(cmd)
        logger.debug(f"Status:{s}, {o} {e}")
        for line in o.split('\n'):
            if f"{account}" in line and '*' in line:
                flag = True
        logger.debug(f"Wallet unlocked: {account} : {flag}")
        return flag

    def unlock_wallet(self, account=None, password = None):
        if not account:
            account = self.account
            password = self.wallet_password
        try:
            if self.is_unlocked(account):
                return self
            with open(f"{WALLET_DIR}/{account}.psw") as psw:
                password = psw.readline().strip()
            cmd =f'{PROTON} wallet unlock -n proton_{account} --password {password}'
            s,o,e = self.run(cmd)
            logger.debug(f"{s}: {o} {e}")
        except Exception as exp:
            logger.error(repr(exp))
            print(repr(exp))
    
    def lock_wallet(self, account=None):
        if not account:
            account = self.account
        try:
            cmd = f'{PROTON} wallet lock -n proton_{account}'
            s, o, e = self.run(cmd)
            logger.debug(f"{s}: {o} {e}")
        except Exception as exp:
            logger.error(repr(exp))
            print(repr(exp))
    
    def tick(self):
        pass
    
    def get_iteration_details(self, iteration=0):
        pass

    def create_user(self, newuser):
        pass

    def stake(self, xpr):
        logger.debug(f"Staking by user {self.account}")
        cmd=f"{PROTON} push action eosio.token transfer '[\"{self.account}\", \"{SC_ACCOUNT}\", \"{xpr}.0000 XPR\", "+\
            f"\"freeos stake\"]' -p {self.account}@active"
        logger.debug((f"{cmd}"))
        s,o,e = self.run(cmd)
        logger.debug(f"{s} : {o} {e}")
        return (s,o,e)

    def claim(self):
        logger.debug(f"Executing {called_by()}(): user={self.account}")
        print(f"Executing {called_by()}(): user={self.account}")
        cmd = f"{PROTON} push action {SC_ACCOUNT} claim '[\"{self.account}\"]' -p {self.account}@active"
        logger.debug((f"{cmd}"))
        s, o, e = self.run(cmd)
        logger.debug(f"{s} : {o} {e}")
        return (s, o, e)

    def unstake(self):
        logger.debug(f"Executing {called_by()}(): user={self.account}")
        print(f"Executing {called_by()}(): user={self.account}")
        cmd = f"{PROTON} push action {SC_ACCOUNT} unstake '[\"{self.account}\"]' -p {self.account}@active"
        logger.debug((f"{cmd}"))
        s, o, e = self.run(cmd)
        logger.debug(f"{s} : {o} {e}")
        return (s, o, e)



class FreeosUser(BaseUser):
    def __init__(self, username):
        super(FreeosUser, self).__init__(username)




if __name__=='__main__':
    #freeos33333=FreeosUser("freeos333333")
    #print(freeos33333)

    #freeos33333.is_unlocked("secondshahid")
    #freeos33333.unlock_wallet("secondshahid")
    #freeos33333.is_unlocked("secondshahid")
    #freeos33333.lock_wallet("secondshahid")
    #freeos33333.is_unlocked("secondshahid")
    euser = "moshamosha"
    user=BaseUser("firstusertom")
    user.unlock_wallet()
    #user.stake(10)
    user.claim()