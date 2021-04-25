
#AirClaim Command Templates

from .config_admin import SC_ACCOUNT, PROTON, SC_CONFIG_ACCOUNT, EOS_TOKEN_ACCOUNT

#Contract Version
CONTRACT_VERSION_CMD=f"{PROTON} push action {SC_ACCOUNT} version '[]' -p ACCOUNT@active "

#Contract Actions
REGUSER_CMD=f"{PROTON} push action {SC_ACCOUNT} reguser '[\"ACCOUNT\"]' -p ACCOUNT@active"
GETUSER_CMD=f"{PROTON} push action {SC_ACCOUNT} getuser '[\"ACCOUNT\"]' -p ACCOUNT@active"

STAKE_CMD=f"{PROTON} push action {EOS_TOKEN_ACCOUNT} transfer " \
          f"'[\"ACCOUNT\", \"{SC_ACCOUNT}\", \"UNIT\",\"freeos stake\"]' -p ACCOUNT@active"
UNSTAKE_CMD=f"{PROTON} push action {SC_ACCOUNT} unstake '[\"ACCOUNT\"]' -p ACCOUNT@active"

CLAIM_CMD=f"{PROTON} push action {SC_ACCOUNT} claim '[\"ACCOUNT\"]' -p ACCOUNT@active"
UNVEST_CMD=f"{PROTON} push action {SC_ACCOUNT} unvest '[\"ACCOUNT\"]' -p ACCOUNT@active"

#Iterations
SET_ITERATION_CMD=f"{PROTON} push action {SC_CONFIG_ACCOUNT} iterupsert " \
                  f"'[ITERATION,\"START_DATE\", \"END_DATE\",RATE1, RATE2]' -p {SC_CONFIG_ACCOUNT}@active"
GET_ITERATION_CMD=f"{PROTON} push action {SC_CONFIG_ACCOUNT} getiter '[ITERNUM]' -p {SC_CONFIG_ACCOUNT}@active"
GET_ALL_ITERATIONS_CMD=f"{PROTON} get table {SC_CONFIG_ACCOUNT} {SC_CONFIG_ACCOUNT} iterations --limit 1000"

SET_CURRENT_RATE=f"{PROTON} push action {SC_CONFIG_ACCOUNT} currentrate '[RATE]' -p {SC_CONFIG_ACCOUNT}@active"
CURRENT_EXCHANGE_RATE=f"{PROTON} get table {SC_CONFIG_ACCOUNT} {SC_CONFIG_ACCOUNT} exchangerate"

#Freeos & XPR Currencies
GETCURRENCY_CMD=f"{PROTON} get currency balance CONTRACT ACCOUNT UNIT"
TRANSFER_CURRENCY_CMD=f"{PROTON} push action {EOS_TOKEN_ACCOUNT} transfer " \
                      f"'[\"FROM_ACC\", \"ACCOUNT\", \"UNIT\", \"MEMO\"]' -p FROM_ACC@active"
#Manage Wallets
WALLET_LIST_CMD=f"{PROTON} wallet list"
UNLOCK_WALLET_CMD=f"{PROTON} wallet unlock -n proton_ACCOUNT --password PASSWORD"
LOCK_WALLET_CMD=f"{PROTON} wallet lock -n proton_ACCOUNT"
