import web3
import web3.eth
import web3.personal
import web3.contract
import web3.miner
import json
import pickle
import time
import rsa
import Network
import Lib
import Crypt

class Library:
    user_address = None
    password = None
    contract_address = web3.Web3.toChecksumAddress("0xe17cf4b293688b55ce8c61ffa5e2704580967afa",)
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

    # МОДУЛЬ 2

    def create_file(self):
        net = Network.Network()
        cry = Crypt.Crypt()
        data = net.get_message()
        print(data)
        if data:
            if data.get('category') == '3':
                file_name = data.get('file_name')
                file_data = data.get('data')
                with open('C:\\Users\\user\\Desktop\\Library\\' + file_name, 'w') as new_file:
                    new_file.write(file_data)
                title = data.get('file_name')
                tipe = data.get('type')
                file_data = data.get('data').encode()
                file_hash = cry.get_hash(file_data)
                self.auth_geth(data.get('author'), '123')
                self.w3.personal.unlockAccount(self.user_address, self.password)
                self.w3.eth.defaultAccount = self.user_address
                tx = self.ws.functions.create_file_3(title, tipe, file_hash).transact({'gas': 900000})
                self.w3.miner.start(1)
                self.w3.eth.waitForTransactionReceipt(tx)
                self.w3.miner.stop()

            elif data.get('category') == '2':
                file_name = data.get('file_name')
                file_data = data.get('data')
                address = data.get('author')

                file_data_enc = cry.aes_encode(file_data, '123')

                with open('C:\\Users\\user\\Desktop\\Library\\' + file_name, 'wb') as new_file:
                    new_file.write(file_data_enc)
                title = data.get('file_name')
                tipe = data.get('type')
                file_data_enc = data.get('data').encode()
                file_hash = cry.get_hash(file_data_enc)
                timeout = int(data.get('timeout'))
                self.auth_geth(data.get('author'), '123')
                self.w3.personal.unlockAccount(self.user_address, self.password)
                self.w3.eth.defaultAccount = self.user_address
                tx = self.ws.functions.create_file_2(title, tipe, timeout, file_hash).transact({'gas': 900000})
                self.w3.miner.start(1)
                self.w3.eth.waitForTransactionReceipt(tx)
                self.w3.miner.stop()

            elif data.get('category') == '1':
                title = data.get('file_name')
                tipe = data.get('type')
                file_name = data.get('file_name')

                file_data = data.get('data').encode()
                enc_file_data = cry.aes_encode(file_data, '123')
                file_hash = cry.get_hash(enc_file_data)

                self.auth_geth(data.get('author'), '123')
                self.w3.personal.unlockAccount(self.user_address, self.password)
                self.w3.eth.defaultAccount = self.user_address
                tx = self.ws.functions.create_file_1(title, tipe, file_hash).transact({'gas': 900000})
                self.w3.miner.start(1)
                self.w3.eth.waitForTransactionReceipt(tx)
                self.w3.miner.stop()

                with open('C:\\Users\\user\\Desktop\\Library\\'+file_name, 'wb') as catalog:
                    catalog.write(enc_file_data)
                cat_file = ''
                cat_file += str(self.files_number() - 1)+'\t'
                cat_file += str(data.get('file_name'))+'\t'
                cat_file += str(data.get('type'))+'\t'
                cat_file += str(data.get('category'))+'\t'
                cat_file += str(data.get('timeout'))+'\t'
                cat_file += str(file_hash)+'\t'
                cat_file += str('123')
                with open('C:\\Users\\user\\Desktop\\Library\\new_catalog.txt', 'a') as catalog:
                    catalog.write(cat_file)
                    catalog.write('\n')


    def get_file_by_id(self, file_id):
        answer = self.ws.functions.get_file_1(file_id).call()
        return answer

    def get_file_by_id_info(self, file_id):
        answer = self.ws.functions.get_file_1(file_id).call()
        info = self.ws.functions.get_file_2(file_id).call()
        answer.append(info)
        return answer

    def files_number(self):
        number = self.ws.functions.get_file_number().call()
        return number

    def show_all_files(self):

        user = self.get_user_by_user_address(self.user_address)
        print(user)
        if user[2] == 0:
            number = self.files_number()
            answer = []
            for i in range(number):
                new_answer = []
                file = self.get_file_by_id(i)
                if str(file[1]) != '' and str(file[2]) != '':
                    info = self.ws.functions.get_file_2(i).call()
                    for j in range(len(file)):
                        new_answer.append(str(file[j]))
                    new_answer.append(str(info[1]))
                    new_answer.append(str(info[2]))
                    new_answer.append(str(info[3]))
                    answer.append(new_answer)
            return answer
        elif user[2] == 1 or user[2] == 3:
            number = self.files_number()
            answer = []
            for i in range(number):
                file = self.get_file_by_id(i)
                if str(file[1]) != '' and str(file[2]) != '':
                    for j in range(len(file)):
                        file[j] = str(file[j])
                    answer.append(file)
            return answer

    def confirm_print_3(self, file_id):
        file_id = int(file_id)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.confirm_print_3(file_id).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

        file = self.get_file_by_id(file_id)
        cat_file = ''
        for j in range(len(file)):
            cat_file += str(file[j]) + '\t'
        with open('C:\\Users\\user\\Desktop\\Library\\new_catalog.txt', 'a') as catalog:
            catalog.write(cat_file)
            catalog.write('\n')

    def refuse_print_3(self, file_id):
        file_id = int(file_id)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.refuse_print_3(file_id).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

    def confirm_print_2(self, file_id):
        file_id = int(file_id)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.confirm_print_2(file_id).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

        file = self.get_file_by_id(file_id)
        cat_file = ''
        for j in range(len(file)):
            cat_file += str(file[j]) + '\t'
        cat_file += '123'
        with open('C:\\Users\\user\\Desktop\\Library\\new_catalog.txt', 'a') as catalog:
            catalog.write(cat_file)
            catalog.write('\n')

    def refuse_print_2(self, file_id):
        file_id = int(file_id)
        self.w3.personal.unlockAccount(self.user_address, self.password)
        self.w3.eth.defaultAccount = self.user_address
        tx = self.ws.functions.refuse_print_2(file_id).transact({'gas': 900000})
        self.w3.miner.start(1)
        self.w3.eth.waitForTransactionReceipt(tx)
        self.w3.miner.stop()

        file = self.get_file_by_id(file_id)
        cat_file = ''
        for j in range(len(file)):
            cat_file += str(file[j]) + '\t'
        with open('C:\\Users\\user\\Desktop\\Library\\new_catalog.txt', 'a') as catalog:
            catalog.write(cat_file)

    def find_file(self):
        net = Network.Network()
        message = net.get_message()
        print(message)
        if message:
            file_id = int(message.get('id'))
            user_address = str(message.get('user_address'))
            file = self.get_file_by_id(file_id)
            print(file)
            file_name = file[1]
            file_hash = file[6]

            if file[4] == 3:
                text = ''
                with open('C:\\Users\\user\\Desktop\\Library\\'+ file_name, 'r') as file:
                    for row in file:
                        text += row
                data = {'file_name': file_name, 'data': text, 'hash': file_hash}
                net = Network.Network()
                net.send_message(data)
                return True
            elif file[4] == 2:
                text = b''
                with open('C:\\Users\\user\\Desktop\\Library\\'+ file_name, 'rb') as file:
                    for row in file:
                        text += row
                cry = Crypt.Crypt()
                text = cry.aes_decode(text, '123').decode()
                file_hash = cry.get_hash(text)
                data = {'file_name': file_name, 'category': 2, 'data': text, 'hash': file_hash}
                net = Network.Network()
                net.send_message(data)
                return True
            elif file[4] == 1:
                user = self.get_user_by_user_address(user_address)
                user_category = int(user[2])
                file_category = int(file[4])
                if user_category == file_category:
                    text = ''
                    with open('C:\\Users\\user\\Desktop\\Library\\' + file_name, 'r') as file:
                        for row in file:
                            text += row
                    data = {'file_name': file_name, 'data': text, 'hash': file_hash}
                    net = Network.Network()
                    net.send_message(data)
                    return True
                else:
                    print('Wrong category')
                    self.w3.personal.unlockAccount(self.user_address, self.password)
                    self.w3.eth.defaultAccount = self.user_address
                    tx = self.ws.functions.wrong_category(int(file_id), str(user_address)).transact({'gas': 900000})
                    self.w3.miner.start(1)
                    self.w3.eth.waitForTransactionReceipt(tx)
                    self.w3.miner.stop()
                    net.send_message('Wrong category')


    def get_file(self, file_id):
        cry = Crypt.Crypt()
        net = Network.Network()
        status = net.send_message(file_id)
        if not status:
            return False
        data = net.get_message()
        file_id = int(file_id)
        file_data = data.get('data')
        if data:
            file_name = data.get('file_name')
            file_hash = data.get('hash')
            if data.get('category') == 2:
                file_data = cry.aes_encode(ata.get('data'), '123')
            my_file_hash =  cry.get_hash(file_data)
            if file_hash == my_file_hash:
                self.w3.personal.unlockAccount(self.user_address, self.password)
                self.w3.eth.defaultAccount = self.user_address
                tx = self.ws.functions.right_hash(file_id, self.user_address).transact({'gas': 900000})
                self.w3.miner.start(1)
                self.w3.eth.waitForTransactionReceipt(tx)
                self.w3.miner.stop()
                with open('C:\\Users\\user\\Desktop\\my_library\\' + file_name, 'w') as file:
                    file.write(file_data)
            else:
                self.w3.personal.unlockAccount(self.user_address, self.password)
                self.w3.eth.defaultAccount = self.user_address
                tx = self.ws.functions.wrong_hash(file_id, self.user_address).transact({'gas': 900000})
                self.w3.miner.start(1)
                self.w3.eth.waitForTransactionReceipt(tx)
                self.w3.miner.stop()
            return True
        else:
            return False

