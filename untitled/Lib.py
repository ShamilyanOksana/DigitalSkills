import random
import hashlib
import Crypt


class Lib:
    def create_files(self, a, b):
        for i in range(a, b+1):
            filename = 'C:\\Users\\user\\Desktop\\Library\\'+'file'+str(i)+'.txt'
            new_file = open(filename, 'w')
            new_file.close()

    def create_catalog(self, a, b, category):
        type_book = ['Печатные издание', "Издаиня для слабовидящих", "Официальные документы", "Неопубликованные документы", "Патентные документы"]
        author = ["Иванов", "Александров", "Сидоров", "Петров", "Алексеев"]
        with open('C:\\Users\\user\\Desktop\\Library\\catalog.txt', 'a') as catalog:
            for i in range(a, b+1):
                catalog.write(str(i-1) + '\t')
                filename = 'file'+str(i)+'.txt'
                catalog.write(filename + '\t')
                rnd = random.randint(0, 4)
                catalog.write(author[rnd] + '\t')
                rnd = random.randint(0, 4)
                catalog.write(type_book[rnd] + '\t')
                catalog.write(str(category) + '\t')
                with open('C:\\Users\\user\\Desktop\\Library\\'+'file'+str(i)+'.txt', 'rb') as current_file:
                    text = b''
                    for row in current_file:
                        text += row
                hash = hashlib.sha256(text).hexdigest()
                catalog.write(hash + '\t')
                if int(category) == 2:
                    catalog.write("0x280c28e82f000827c8a259ba2a57bd66e89fc54c" + '\t')
                    catalog.write('3' + '\t')
                else:
                    catalog.write('0' + '\t')
                    catalog.write('0' + '\t')
                catalog.write('\n')

    def encode_file(self, filename):
        with open('C:\\Users\\user\\Desktop\\Library\\'+filename, 'rb') as file:
            text = b''
            for row in file:
                text += row
        cry = Crypt.Crypt()
        ctext = cry.aes_encode(text, '123')
        with open('C:\\Users\\user\\Desktop\\Library\\' + filename, 'wb') as file:
            file.write(ctext)

    def get_file_data(self, path):
        with open(path, 'r') as file:
            text = ''
            for row in file:
                text += row
        return text