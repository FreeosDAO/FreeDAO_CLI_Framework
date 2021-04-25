#!/usr/bin/env python3

import pathlib
import os, sys
PROJECT_ROOT_DIR = os.path.abspath(os.curdir)

# User configs
ROOT_DIR=str(pathlib.Path(__file__).parent.parent.parent)

USER_JSON=str(pathlib.Path("users.json").absolute())
sys.path.append(ROOT_DIR)

from src.configs.config_admin import *
print(dir())
print (ROOT_DIR,'\n',ITERATIONS_TOKENS_ISSUED)


if __name__=='__main__':
    print(ROOT_DIR)
    print(USER_JSON)
    print(PROJECT_ROOT_DIR)


