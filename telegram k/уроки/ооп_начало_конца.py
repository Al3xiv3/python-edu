# Классы
class Car:  # Класс машина
    # self Указывает на экземляр класса  в нашем случае перем. car
    def __init__(self, model: str, max_speed: int, mark: str):  # этот метод вызывается, когда создаем объект
        # Обьявим атрибуты/поля (переменные) класса
        self.model = model  # У класса создаем атрибут model и кладем Значение которое даем при создании
        self.max_speed = max_speed
        self.mark = mark
        print('я родился')  # PRINT будет при создании объеекта   Car('volga', 180) Напримерр

    def drive(self):  # self Обязателен
        print('поехал')

    def set_speed(self, new_speed: int):
        self.max_speed = new_speed  # Переопределяем скорость

    def mark_2(self):
        print('530d')


# инит - магический метод, который выполняется при создании экземпляра

car = Car('bmw', 400, '530d')  # создание экземляра
# car - экземляр класса Car
car.mark_2()
print(car.mark)
car.drive()
print(car.max_speed)
car.set_speed(500)
print(car.max_speed)


print(type(1))