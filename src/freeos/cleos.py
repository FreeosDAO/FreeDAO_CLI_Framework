import logging
import subprocess
import traceback
from logging import exception
import requests

log = logging.getLogger(__name__)

log.info("Hello logging!")

class Cleos (object):
    """This is the main cleos management module
to perform all the operations"""

    def __init__(self):
        self.scope=None
        self.username=None
        self.contract_name=None
        self.url=None

    def execute(self, command):
        try:
            assert command, "Invalid command"
            command=command.strip()

            command_args=command.split(" ")
            logging.debug("Command: ")
            process = subprocess.run(command_args,
                                     stdout=subprocess.PIPE,
                                     stdin=subprocess.PIPE,
                                     universal_newlines=True)
        except exception as exp:
            traceback.print_exc()
        finally:
            pass
        return self, process.returncode, process.stdout, process.stderr

    def browse(self, url, method='get',**kwargs):
        resp = None
        # Validate command
        # log the command
        # Process the  argument or command
        # log the command result
        try:
            #process kwargs
            arg = ""
            for (k,v) in kwargs:
                arg += f"{k}={v}"
            print ("Formatted: K & V:" + arg)
            if ('get' == method):
                resp = requests.get(url)

        except exception as exp:
            traceback.print_exc()
        finally:
            pass
        return self, resp.status_code, resp.json(), resp

    def action_reguser(self):
        return self

    def action_stake(self):
        return self


    def action_unstake(self):
        return self

    def action_claim(self):
        return self

if __name__=='__main__':
    cleos = Cleos()
    #cleos.execute("cleos -u URL")
    #log.info("Hello logging2!")
    #cleos.browse("http://www.google.com")
    print(cleos.execute("uname -a")[0].execute("date"))
    d ={'a':1}
    print(cleos.browse("http://faucet-kylin.blockzone.net/create/mshahid12nov", method='get'))