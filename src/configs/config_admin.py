#
# Admin Account related configs

EOS_TOKEN_ACCOUNT="eosio.token"
SC_ACCOUNT='freeost'
SC_ACCOUNT_PASSWORD='PW5JTqydS2UX4VyUuaDhZVeWeRzdfphcpjqNDj1Es27s3r11TXiyy'

SC_CONFIG_ACCOUNT='freeoscfgt'
SC_CONFIG_ACCOUNT_PASSWORD='PW5JxCe6mVRnvxMqLm2gSJocv14ysg9GRvx2do5Di4mK6kymB3abr'

SC_WALLET_PSW_FILE=''
SC_WALLET_FILE=''

SC_ABI="freeos.abi"
SC_WSM="freeos.wasm"
SC_CONFIG_ABI="freeosconfig.abi"
SC_CONFIG_WSM="freeosconfig.wasm"

DATE_TIME_PATTERN="%Y-%m-%d %H:%M:%S"
ITERATION_START_DATE="2021-02-20 19:15:00"
ITERATION_INTERVAL="00:10:00"
TIMEZONE='Pacific/Auckland'
ITERATION_START_FROM_NUM=1
TOTAL_NUM_ITERATIONS=6

END_POINT="https://protontestnet.greymass.com"
WALLET_DIR = "/Users/shahid/eosio-wallet"
PROTON=f"/usr/local/bin/cleos -u {END_POINT}"

SC_NAME_WASM_PATH='/Users/shahid/eosio-wallet/WASM/freeos'
SC_CONFIG_WASM_PATH='/Users/shahid/eosio-wallet/WASM/freeosconfig'

STAKE_UPSERT_LIST=[[0,0,0,0,0,10,0,0,0,0,0],
              [5,0,0,0,10,20,0,0,0,0,0],
              [10,0,0,0,20,30,0,0,0,0,0],
              [20,0,0,0,30,50,0,10,0,0,0],
              [30,0,0,0,50,80,0,20,0,0,0],
              [40,0,0,0,80,130,0,30,0,0,0],
              [50,0,0,0,130,210,0,50,0,0,0],
              [60,0,0,0,210,340,0,80,0,0,0],
              [70,0,0,0,340,550,0,130,0,0,0],
              [80,0,0,0,550,890,0,210,0,0,0],
              [90,0,0,0,890,1440,0,340,0,0,0],
              [100,0,0,0,1440,2330,0,550,0,0,0]]

ITERATIONS_TOKENS_ISSUED={    1:[100,0],
                              2:[125, 50],
                              3:[150,113],
                              4:[175,188],
                              5:[200, 275],
                              6:[225, 375],
                              7:[250, 488],
                              8:[275, 613],
                              9:[300, 750],
                              10:[325, 900],
                              11:[350, 1063],
                              12:[375, 1238],
                              13:[400, 1425],
                              14:[425, 1625],
                              15:[450, 1838],
                              16:[475, 2063],
                              17:[500, 2300],
                              18:[525, 2550],
                              19:[550, 2813],
                              20:[575, 3088],
                              21:[600, 3375],
                              22:[625, 3675],
                              23:[650, 3988],
                              24:[675, 4313],
                              25:[700, 4650]
                              }
ITERATIONS_TOKENS_DEFAULT=ITERATIONS_TOKENS_ISSUED[25]

MD_SUM={SC_ABI:"df5ad62a284e183cd350af90b8126c8b",
        SC_WSM:"944bba7080d871887643f96cdffed10b",
        SC_CONFIG_ABI:"87f352e727e843ae9f713916f264dfd5",
        SC_CONFIG_WSM:"409424aedb3b4dda57647b9b13689dd5"}





if __name__=='__main__':
    print(ITERATIONS_TOKENS_DEFAULT)
    print(PROTON)
    print(ITERATIONS_TOKENS_ISSUED[22])


