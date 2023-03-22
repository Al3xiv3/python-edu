class Person:
    def __init__(self, name: str, surname: str, sex: "F" or "M", age: int):
        """Тут мы классу даем поля, то бишь  self.name = name создаст поле (атрибут) name и
        присвоит ему значение из аргументов"""
        #   поле   значение
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def about_me(self):
        print(f'Hello, my name is {self.name} {self.surname}, I\'m {self.age} old, I\'m {self.sex}')

    def growing_up(self):
        self.age += 1




person = Person('Alexander', 'Sivolodsky', 'M', 25)

person.about_me()

person.growing_up()
print(person.age)


