import web3
import web3.eth
import web3.personal
import web3.contract
import web3.miner
import json
import pickle
import time
import rsa

class Library:

    user_address = None
    password = None
    contract_address = None
    abi = ''
    bin = ''
    w3 = None
    ws = None

    def __init__(self):
        self.w3 = web3.Web3(web3.HTTPProvider('http://192.168.1.21:8545'))
        # self.ws = self.w3.eth.contract(
        #     address=self.contract_address,
        #     abi='',
        # )

    # Works
    def new_geth_account(self, password):
        password = str(password)
        user_address = self.w3.personal.newAccount(password)
        return user_address

    # Works
    def auth_geth(self, login, password):
        try:
            login = web3.Web3.toChecksumAddress(login)
        except Exception:
            return False
        else:
            self.user_address = login
            self.password = str(password)
            log = self.w3.personal.unlockAccount(login, password)
        return log

    def new_ok_ck(self):
        (publikKey, privatKey) = rsa.newkeys(512)
        str_privatKey = {'e': privatKey.e}
        file_name = 'privatKey_'+self.user_address+'.txt'
        with open(file_name, 'w') as ck_file:
            ck_file.write('')
