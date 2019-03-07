import Contract
class cli:
    comand = str()
    Estate = Contract.Library()
    def help(self):
        print("Список команд")
        print("eixt - выйти из программы")
        print("autorization - авторизоваться в geth")
        print("regestration - регестрация в geth")
    def autorization(self):
        print("Введите логин ")
        login = input()
        print("Введите пароль")
        password = input()
        Station =  self.Estate.auth_geth(login,password)
        if Station ==True:
            print("Авторизация прошла успешно")
        else:
            print("Неправельный логин или пароль введите заного")
    def regestration(self):
        print("Введите пароль")
        password = input()
        adr = self.Estate.new_geth_account(password)
        print("Вы успешно зарегестрировались ваш Id (логинр) "+ adr)

    def mainloop(self):
        while True:
            self.comand = input()
            if self.comand == "help":
                self.help()
            elif self.comand == "autorization":
                self.autorization()
            elif self.comand=="exit":
                exit()
            elif self.comand == "registration":
                self.regestration()
            else:
                print("Введна не правельная команда введите комнду help что бы посмотреть доступные команды")


obj = cli()
obj.mainloop()