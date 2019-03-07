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
    contract_address = web3.Web3.toChecksumAddress('0xdac20dd01329a9dd8faee4f63d9bf2a7e8440a7c')
    with open('Store.abi', 'r') as file:
        abi = file.read()
    with open('Store.bin', 'r') as file:
        bin = file.read()
    w3 = None
    ws = None

    def __init__(self):
        self.w3 = web3.Web3(web3.HTTPProvider('http://192.168.1.21:8545'))
        self.ws = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.abi,
        )


    # Works
    def new_geth_account(self, password):
        '''
        если нет аккаунта в geth
        создает новый аккаунт в geth
        :param password:
        :return:
        '''
        self.password = str(password)
        self.user_address = self.w3.personal.newAccount(password)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        return self.user_address

    # Works
    def auth_geth(self, login, password):
        '''
        если ЕСТЬ аккаунт в geth
        входит в свой аккаунт
        :param login:
        :param password:
        :return:
        '''
        try:
            login = web3.Web3.toChecksumAddress(login)
        except Exception:
            return False
        else:
            self.user_address = login
            self.password = str(password)
            log = self.w3.personal.unlockAccount(self.user_address, self.password)
        return log

    # Works
    def new_ok_ck(self, name=' '):
        '''
        если НЕТ аккаунта в системе
        генерируем открытый и закрытый ключ
        :return:
        '''
        (publikKey, privatKey) = rsa.newkeys(512)
        str_privatKey = {'e': privatKey.e, 'd': privatKey.d, 'n': privatKey.n, 'p': privatKey.p, 'q': privatKey.q}
        str_privatKey = json.dumps(str_privatKey)
        str_publicKey = {'e': publikKey.e, 'n': publikKey.n}
        str_publicKey = json.dumps(str_publicKey)
        file_name = 'privatKey_' + self.user_address + '.txt'
        with open(file_name, 'w') as ck_file:
            ck_file.write(str_privatKey)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.check_in(name, str_publicKey).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    # Works
    def admin_genesis(self, name=' '):
        (publikKey, privatKey) = rsa.newkeys(512)
        str_privatKey = {'e': privatKey.e, 'd': privatKey.d, 'n': privatKey.n, 'p': privatKey.p, 'q': privatKey.q}
        str_privatKey = json.dumps(str_privatKey)
        str_publicKey = {'e': publikKey.e, 'n': publikKey.n}
        str_publicKey = json.dumps(str_publicKey)
        file_name = 'ADMIN_privatKey_' + self.user_address + '.txt'
        with open(file_name, 'w') as ck_file:
            ck_file.write(str_privatKey)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.admin_genesis(self.user_address, name, str_publicKey).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    # Works
    def libr_genesis(self, name=' '):
        (publikKey, privatKey) = rsa.newkeys(512)
        str_privatKey = {'e': privatKey.e, 'd': privatKey.d, 'n': privatKey.n, 'p': privatKey.p, 'q': privatKey.q}
        str_privatKey = json.dumps(str_privatKey)
        str_publicKey = {'e': publikKey.e, 'n': publikKey.n}
        str_publicKey = json.dumps(str_publicKey)
        file_name = 'LIB_privatKey_' + self.user_address + '.txt'
        with open(file_name, 'w') as ck_file:
            ck_file.write(str_privatKey)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.libr_genesis(self.user_address, name, str_publicKey).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def get_role(self, user_address):
        answer = self.get_user_by_user_address(user_address)
        return str(answer[3])

    # Works
    def get_user_id_by_user_address(self, user_address):
        user_address = web3.Web3.toChecksumAddress(user_address)
        answer = self.ws.functions.get_user_id_by_user_address(user_address).call()
        return answer

    # Works
    def get_user_by_user_address(self, user_address):
        user_address = web3.Web3.toChecksumAddress(user_address)
        answer = self.ws.functions.get_user_by_user_address(user_address).call()
        return answer

    def get_user_number(self):
        answer = self.ws.functions.get_user_number().call()
        return answer

    def get_user_by_user_id(self, user_id):
        answer = self.ws.functions.get_user_by_user_id(user_id).call()
        return answer

    def check_in(self, user_address):
        '''
        вход в систему если есть аккаунт
        '''
        number = self.get_user_number()
        for i in range(number):
            user_address = web3.Web3.toChecksumAddress(user_address)
            user = self.get_user_by_user_id(i)
            roles = {'1': 'Admin', '2': 'Lib', '3': 'User'}
            if user[3] == '0':
                return 'Ваш аккаунт заблокирован'
            if user[0] == user_address:
                return roles.get(str(user[3]))
        return 'Вы не зарегестрированы'

    def request_admin_rights(self):
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.request_admin_rights().transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def request_librarian_rights(self):
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.request_librarian_rights().transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def show_all_users(self):
        number = self.get_user_number()
        new_answer = []
        for i in range(number):
            user = self.get_user_by_user_id(i)
            array = []
            if user[3] != 0:
                array.append(str(user[0]))
                array.append(str(user[1]))
                array.append(str(user[2]))
                array.append(str(user[3]))
                array.append(str(user[4]))
                new_answer.append(array)
        return new_answer

    def get_request_number(self):
        answer = self.ws.functions.get_request_number().call()
        return answer

    def get_request_by_request_number(self, request_number):
        request_number = int(request_number)
        answer = self.ws.functions.get_request_by_request_number(request_number).call()
        return answer

    def show_request_category(self):
        number = self.get_request_number()
        new_answer = []
        for i in range(number):
            request = self.get_request_by_request_number(i)
            array = []
            if request[2] != 0:
                array.append(str(request[0]))
                array.append(str(request[2]))
                new_answer.append(array)
        return new_answer

    def show_request_roles(self):
        number = self.get_request_number()
        new_answer = []
        for i in range(number):
            request = self.get_request_by_request_number(i)
            array = []
            roles = {'1': 'Администратор', '2': 'Библиотекарь'}
            role = roles.get(str(request[1]))
            if request[1] != 0:
                array.append(str(request[0]))
                array.append(str(role))
                new_answer.append(array)
            return new_answer

    def confirm_rights(self, user_address, new_role):
        user_address = web3.Web3.toChecksumAddress(user_address)
        roles = {'1': 'Администратор', '2': 'Библиотекарь'}
        if new_role == 'Администратор':
            new_role = 1
        elif new_role == 'Библиотекарь':
            new_role = 2
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.confirm_rights(user_address, int(new_role)).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def refuse_rights(self, user_address, new_role):
        user_address = web3.Web3.toChecksumAddress(user_address)
        roles = {'1': 'Администратор', '2': 'Библиотекарь'}
        if new_role == 'Администратор':
            new_role = 1
        elif new_role == 'Библиотекарь':
            new_role = 2
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.refuse_rights(user_address, int(new_role)).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def request_access_to_other(self):
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.request_access_to_other().transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def confirm_access_to_other(self, user_address):
        user_address = web3.Web3.toChecksumAddress(user_address)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.confirm_access_to_other(user_address).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def refuse_access_to_other(self, user_address):
        user_address = web3.Web3.toChecksumAddress(user_address)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.refuse_rights(user_address).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def delete_user(self, user_address):
        user_address = web3.Web3.toChecksumAddress(user_address)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.delete_user(user_address).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()




