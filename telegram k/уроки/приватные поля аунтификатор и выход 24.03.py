# пишем класс User. Поля: логин, пароль и айпи
users = {
    'boss777': ['qwerty', '193.0.55.10'],
    'hacker7': ['yamoskvuhacknul', '243.100.57.10']
}


# база юзеров

class User:
    def __init__(self, login: str, password: str, ip: str):
        self.login = login
        self.__password = password
        self.__ip = ip  # приватное поле
        self.__is_login = False  # сначало не вошел

    def authentication(self):
        if self.login in users.keys():  # если логин есть в базе
            p, ip = users[self.login]  # получи пароль из базы  в значиии список из пароля и айпи
            print(f"Успешный вход с ip='{self.__ip}'")  # обращаемся к приватному полю
            self.__is_login = True

        else:  # если логина нет в базе
            print(f"Неверный логин: '{self.login}'. Попробуйте еще раз.")

    def exit(self):
        if self.__is_login == True:
            print(f"До свидания, '{self.login}'! Будем рады Вам снова!")


user1 = User('nagibator2015', '123456', '95.100.100.10')
user2 = User('hacker7', 'yamoskvuhacknul', '212.100.53.10')

user1.authentication()
user2.authentication()

user1.exit()
user2.exit()