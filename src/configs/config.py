#
import pathlib
import os, sys
from argparse import ArgumentParser, ArgumentError
import inspect

called_by=lambda: inspect.stack()[1][3]

PROJECT_ROOT_DIR = os.path.abspath(os.curdir)

# User configs
ROOT_DIR=str(pathlib.Path(__file__).parent.parent.parent)
LOG_DIR=ROOT_DIR

USER_JSON=str(pathlib.Path("users.json").absolute())
sys.path.append(ROOT_DIR)

class Args():
    def __init__(self):
        self.args = ArgumentParser(allow_abbrev=False,
                                   description='Automation Framework to Deploy and Test FreeDAO')
        self.args.add_argument('--iteration', '-I',type=str, action='store', required=False, help='invoke iteration feature')
        self.args = self.args.parse_args()
        print(called_by())




if __name__=='__main__':
    print(ROOT_DIR)
    print(USER_JSON)
    print(PROJECT_ROOT_DIR)
    args = Args()
    print(args.args.iteration)
    print (called_by())

