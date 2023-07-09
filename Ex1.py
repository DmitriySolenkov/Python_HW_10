class Animal:
    def __init__(self, name, age, colour):
        self._name = name
        self._age = age
        self.__colour = colour

    def increase_age():
        self.age += 1

    def get_name(self):
        return self._name

    def get_colour(self):
        return self.__colour

    def get_age(self):
        return self._age

    def check_info(self):
        print(f'Name= {self._name}, age= {self._age}, colour= {self.__colour}')


class Zebra(Animal):

    def __init__(self, name, age, colour, strips_number=20, max_speed=30):
        Animal.__init__(self, name, age, colour)
        self.strips_number = strips_number
        self.max_speed = max_speed

    def check_spec_info(self):
        print(
            f'Max speed: {self.max_speed}, number of strips: {self.strips_number}')


class Spider(Animal):

    def __init__(self, name, age, colour, eyes_amount, status):
        Animal.__init__(self, name, age, colour)
        self.eyes_amount = eyes_amount
        self.status = status

    def check_spec_info(self):
        print(f'Amount of eyes: {self.eyes_amount}, status: {self.status}')


class Snake(Animal):

    def __init__(self, name, age, colour, movement_type="crawling"):
        Animal.__init__(self, name, age, colour)
        self.movement_type = movement_type

    def check_spec_info(self):
        print(f'Movement type: {self.movement_type}')


class Fabric:
    def __init__(self, zebras_list, spiders_list, snakes_list):
        self.zebras_list = zebras_list
        self.spiders_list = spiders_list
        self.snakes_list = snakes_list

    def add_Zebra():
        name = input("Enter name: ")
        age = input("Enter age: ")
        colour = input("Enter colour: ")
        strips_number = input("Enter number of strips: ")
        max_speed = input("Enter max speed: ")
        zebras_list.append(Zebra(name, age, colour, strips_number, max_speed))

    def print_zebras(self):
        for i in zebras_list:
            print()
            i.check_info()
            i.check_spec_info()


Bob = Zebra("Bob", 23, "black or white", 15, 23)
zebras_list = []
zebras_list.append(Bob)

John = Spider("John", 3, "blue", 8, "terrifying")
spiders_list = []
spiders_list.append(John)

Alex = Snake("Alex", 4, "red")
snakes_list = []
snakes_list.append(Alex)

fabric = Fabric(zebras_list, spiders_list, snakes_list)
fabric.print_zebras()

Fabric.add_Zebra()
fabric.print_zebras()
