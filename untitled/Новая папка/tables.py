import web3


# вывод таблицы запросов роли
number = Store.get_request_number()
new_answer = []
for i in range(number):
    request = Store.get_request_id_by_request_number(i)
    array = []
    if request[1] != 0:
        array.append(str(request[0]))
        array.append(str(request[1]))
        new_answer.append(array)


number = Store.get_request_number()
new_answer = []
for i in range(number):
    request = Store.get_request_id_by_request_number(i)
    array = []
    if request[2] != 0:
        array.append(str(request[0]))
        array.append(str(request[2]))
        new_answer.append(array)


number = Store.get_user_number
new_answer = []
for i in range(number):
    user = Store.get_user_by_user_id(i)
    array = []
    if user[3] != 0:
        array.append(str(user[0]))
        array.append(str(user[1]))
        array.append(str(user[2]))
        array.append(str(user[3]))
        array.append(str(user[4]))
        new_answer.append(array)