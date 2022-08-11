# from random import choice
#
#
# class Car:
#     """Main car"""
#     direction = ["noth", "notheast", "east", "southeast",
#                  "south", "southwest", "west", "nothwest"]
#
#     def __init__(self, name, color, speed, police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = police
#         print(f"New car: {name} has a color: {color}. \n Is the car a police car? {police}")
#
#     def go(self):
#         print(f'{self.name}: Car went.')
#
#     def stop(self):
#         print(f'{self.name}: Car stopped!')
#
#     def turn(self):
#         print(f'{self.name}: Car turned{choice(self.direction)}')
#
#     def show_speed(self):
#         return f'{self.name}: Car speed: {self.speed}.'
#
#
# class TownCar(Car):
#     """City car"""
#
#     def show_speed(self):
#         return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()
#
#
# class WorkCar(Car):
#     """Cargo Track"""
#
#     def show_speed(self):
#         return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()
#
#
# class SportCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#     def __init__(self, name, color, speed):
#         super().__init__(name, color, speed, police=True)
#
#
# police_car = PoliceCar('"Копы"', "синявка", 100)
# work_car = WorkCar('"Газель"', "черный", 40)
# sport_car = SportCar('"Мажорка"', "неон", 120)
# town_car = TownCar("Кэб", "красный", 65)
#
# List_of_cars = [police_car, work_car, sport_car, town_car]
#
# for n in List_of_cars:
#     n.go()
#     print(n.show_speed())
#     n.turn()
#     n.stop()
#     print()

# class Stationery:
#     def __init__(self, title="Something information"):
#         self.title = title
#
#     def draw(self):
#         print(f'Start drawing! {self.title}')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Start drawing with {self.title} pen!')
#
#
# class Pensil(Stationery):
#     def draw(self):
#         print(f'Start drawing with {self.title} pensil!')
#
#
# class Marker(Stationery):
#     def draw(self):
#         print(f'Start drawing with {self.title} marker!')
#
#
# stat = Stationery()
# pen = Pen("Звезда")
# pencil = Pensil("Коммунарка")
# marker = Marker("Китайский рандом")
#
# office_supplies = [stat, pen, pencil, marker]
#
# for n in office_supplies:
#     n.draw()
