import subprocess
import traceback
from subprocess import PIPE, Popen
from src.utils.base_logger import logger
from src.configs.config import called_by


def run(cmd):
    status = -1
    proc_output = proc_err = None
    print(f"Executing: {cmd}")
    try:
        #cmd_list = cmd.split(" ")
        logger.info(f"{called_by()}(): Executing: {cmd}")
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        status = proc.returncode
        proc_output, proc_err = proc.communicate()
        proc_output = proc_output.strip()
        proc_err = proc_err.strip()
        if not status:
            if (not proc_output) or proc_err:
                status = -1
            else:
                status = 0
        logger.debug(f"Status: {status}: Output: {proc_output}, {proc_err}")
    except Exception as exp:
        logger.error(repr(exp))
        logger.error(f"Status: {status}: Output: {proc_output}, Error: {proc_err}")
        print(f"Status: {status}: Output: {proc_output}, Error:{proc_err}")

    finally:
        print(f"Status: {status}: Output: {proc_output}\n{proc_err}")
        return (status, proc_output, proc_err)

def rrun(cmd):
    status = -1
    proc_output = proc_err = None
    cmd_list = cmd.split(" ")
    logger.info(f"{called_by()}: Executing: {cmd_list}")

    try:
        cp = subprocess.run(cmd, shell=True,universal_newlines=True, stdout=PIPE, stderr=PIPE)
        logger.info(f"Executing: {cmd_list}")
        status = cp.returncode
        proc_output = cp.stdout.strip()
        proc_err = cp.stderr.strip()
        if not status:
            if (not proc_output) or proc_err:
                status = -1
            else:
                status = 0
        logger.debug(f"Status: {status}: Output: {proc_output}, {proc_err}")
    except Exception as exp:
        logger.error(repr(exp))
        logger.error(repr(traceback.print_exc()))
        logger.error(f"Status: {status}: Output: {proc_output}, Error: {proc_err}")
        print(f"Status: {status}: Output: {proc_output}, Error:{proc_err}")
    finally:
        return (status, proc_output, proc_err)

if  __name__ == '__main__':
    #cmd='sudo purge'
    cmd = "/usr/local/bin/cleos -u https://protontestnet.greymass.com wallet list"
    print (run(cmd))
    #print(prun(cmd))