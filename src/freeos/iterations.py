import json
import sys
import os
import src

from datetime import datetime, time, timedelta
from getpass import getpass
from src.configs.config_admin import *
from src.configs.config import *
from src.configs.airclaim_cmd import *
from src.utils.base_logger import logger
from src.utils.utils import run as run
from src.freeos.user import BaseUser as User, FreeosUser

sys.path.insert(0, os.path.abspath('..'))


class Iterations(object):
    """Enter the start Date & Time in format YYYY/MM/DD HH:MM:SS, mention the count of iterations,
    and the interval between each iterations that you plan.
    Time is assumed to be in UTC.
    Effective time shall be mentioned also as per local time
    """
    def __init__(self):
        self.start_iteration_time=None
        self.current_iteration = 0
        self.num_iterations=TOTAL_NUM_ITERATIONS
        #self.tokens_tuple=None
        self.sc_admin_acc = FreeosUser(SC_ACCOUNT)
        self.sc_config_acc=FreeosUser(SC_CONFIG_ACCOUNT)

    def admin_passwords(self):
        global SC_ACCOUNT_PASSWORD, SC_CONFIG_ACCOUNT_PASSWORD
        SC_ACCOUNT_PASSWORD = getpass(prompt=f"Enter Wallet Password for {SC_ACCOUNT}", stream=sys.stderr)
        SC_CONFIG_ACCOUNT_PASSWORD = getpass(f"Enter Wallet Password for {SC_CONFIG_ACCOUNT}")


    def add_time_to_date(self, start_time, time_string = ITERATION_INTERVAL):
        if len(str(time_string).split(":")) == 3:
            delta_time=datetime.strptime(time_string,"%H:%M:%S")

        if type(start_time) is str:
            start_time = datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")

        end_time = start_time + timedelta(hours=delta_time.hour,
                                          minutes=delta_time.minute,
                                          seconds=delta_time.second-1)
        end_time = end_time.strftime(DATE_TIME_PATTERN)

        next_iter_time=start_time + timedelta(hours=delta_time.hour,
                                          minutes=delta_time.minute,
                                          seconds=delta_time.second)
        logger.debug(f"Evaluated next iteration time: {next_iter_time} [Interval: {ITERATION_INTERVAL}]")
        next_iter_time = next_iter_time.strftime(DATE_TIME_PATTERN)
        return end_time, next_iter_time

    def set_iteration(self, iter_num, start_time, end_time):
        s=o=e = None

        try:
            if iter_num in ITERATIONS_TOKENS_ISSUED:
                tokens=ITERATIONS_TOKENS_ISSUED.get(iter_num)
            else:
                tokens=ITERATIONS_TOKENS_DEFAULT

            if not self.sc_config_acc.is_unlocked():
                self.sc_config_acc.unlock_wallet(SC_CONFIG_ACCOUNT, SC_CONFIG_ACCOUNT_PASSWORD)

            cmd = SET_ITERATION_CMD.replace('ITERATION',str(iter_num))\
                .replace('START_DATE',start_time)\
                .replace('END_DATE',end_time)\
                .replace('RATE1', str(tokens[0]))\
                .replace('RATE2', str(tokens[1]))
            logger.debug(f"Setting Iteration {iter_num}: {cmd}")
            s,o,e = run(cmd)
        except Exception as exp:
            logger.error(f"{called_by()} {repr(exp)}")
            sys.exit(-1)
        finally:
            return s,o,e

    def set_current_rate(self, current_rate):
        if not current_rate:
            return
        cmd=SET_CURRENT_RATE.replace('RATE', str(current_rate))
        return run(cmd)


    def calculate_iteration(self, target_iteration):
        iter_start=iter_end=ITERATION_START_DATE
        count = 0
        print(f"Starting with: {iter_end}")
        while(count < target_iteration):
            iter_start = iter_end
            offset_end, iter_end = self.add_time_to_date(iter_start)
            count += 1
        logger.debug(f"Calculated Iteration Params: {target_iteration}, {iter_start}, {offset_end}")
        return iter_start, offset_end

    def get_current_iteration(self):
        cmd=GET_ALL_ITERATIONS_CMD
        logger.debug((f"{GET_ALL_ITERATIONS_CMD}"))
        s, o, e = run(cmd)
        logger.debug(f"{s} : {o} {e}")
        stats = json.loads(o)
        self.current_iteration = int(stats["rows"][-1]["iteration_number"])
        return self.current_iteration



def ExecuteIterations():
    iteration = Iterations()
    current_iteration = iteration.get_current_iteration()
    current_iteration = 4
    next_iteration = current_iteration +1

    print(f"Starting with iteration number: {next_iteration}")
    while (next_iteration <= iteration.num_iterations):
        print (f"Processing: {next_iteration}")
        iter_start, offset_end = iteration.calculate_iteration(next_iteration)
        s,o,e = iteration.set_iteration(next_iteration, iter_start, offset_end)
        print(s,o,e)

        ans = input(f"Iteration {next_iteration} configured. Do you want to configure next iteration? [Y/n]: ").lower()
        if not ans in ['y','yes']:
            sys.exit(0)
        next_iteration += 1
        new_rate = input("Enter current rate of FREEOS: ")
        message = f"Setting current rate of FREEOS: {new_rate}"
        print(message)
        logger.debug(message)



if __name__=='__main__':
    #print(ITERATIONS_TOKENS_DEFAULT)
    print(ROOT_DIR)
    iters = Iterations()
    #iters.delta_to_second("23:23:12")
    #iters.set_iteration(22, "2021-02-28 19:00:00","2021-03-01 09:59:59")
    #iters.admin_passwords()
    #iters.unlock_admin_wallets()
    #iters.delta_to_time("2021-02-28 19:00:00", ITERATION_INTERVAL)
    #iters.calculate_iteration(1)
    #iters.calculate_iteration(3)
    #iters.get_current_iteration()
    ExecuteIterations()
