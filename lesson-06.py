# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from itertools import cycle
from time import sleep

class TrafficLight:
    colors_queue = ("красный", "жёлтый", "зелёный")
    time_queue = (7, 2, 5)
    message = ("Красный - стоп", "Жёлтый - приготовиться", "Зелёный - вперёд!")
    
    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.colors_queue)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.colors_queue.index(self.__color)])
                sleep(self.time_queue[self.colors_queue.index(self.__color)])
                self.__color = next(my_cycle)

my_traffic = TrafficLight("жёлтый")
my_traffic.running()








# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число
# см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length
    @property
    def square(self):
        return self._length * self._width

    def get_width_of_asphalt(self, weight_ratio, thinkness):
        asphalt = self.square * weight_ratio * thinkness
        return asphalt

my_road = Road(20, 10000)
print(my_road.get_width_of_asphalt(25, 0.5))








# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, \
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии \
#     (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    @property

    def full_name(self):
        return f"{self.name} {self.surname}"

    @property
    def full_salary(self):
        return self._income['wage'] + self._income['bonus']

my_position = Position('Andrew', 'Ivanov', 'devops', 120000, 30000)
print(f'Total salary of {my_position.full_name} is {my_position.full_salary}')






# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.


class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"машина {self.color} цвета, марки {self.name} поехала со скоростью {self.speed}")

    def stop(self):
        print(f"машина {self.color} цвета, марки {self.name} остановилась")

    def turn(self, direction):
        print(f"машина {self.color} цвета, марки {self.name} повернула на  {direction}")

    def show_speed(self):
        print(f"Текущая скорость машины -  {self.speed} ")

class TownCar(Cars):
    def show_speed(self):
        if self.speed > 60:
            print("Пора бы и замедлиться!")
        else:
            Cars.show_speed(self)

class SportCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

class WorkCar(Cars):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости для Вашего чудовища")


class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(self, speed, color, name, is_police=True)


my_police_car = PoliceCar(90, "white", "Megan")
my_police_car.go()
my_police_car.turn(">>>")
my_police_car.stop()
my_police_car.show_speed()

my_work_car = WorkCar(90, "black", "TownCar", False)
my_work_car.go()
my_work_car.turn(">>>")
my_work_car.stop()
my_work_car.show_speed()

my_sport_car = SportCar(220, "red", "BMV")
my_sport_car.go()
my_sport_car.turn("<<<<>>>>>>>")
my_sport_car.show_speed()

my_town_car = TownCar(55, "black", "Megan", False)
my_town_car.go()
my_town_car.turn(">>>")
my_town_car.stop()
my_town_car.show_speed()



# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def draw(self):
        print(f"Можно рисовать и {self.title}")


class Pencil(Stationary):
    def draw(self):
        print(f"А можно рисовать и {self.title}")

class Handl(Stationary):
    def draw(self):
        print(f"Но можно и малюкать вот им- {self.title}")

pen = Pen("Карандаш")
pencil = Pencil("Ручка")
handl = Handl("Маркер")
pen.draw()
pencil.draw()
handl.draw()



