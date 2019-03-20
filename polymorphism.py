class Pet:
    def __init__(self, name):
        self.name = name

    def say(self):
        return f'My name is{self.name}'


class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'Voff, my name is {self.name} and my breed is {self.breed}'


class Cat(Pet):

    def __init__(self, name, breed, colour):
        super().__init__(name)
        self.breed = breed
        self.colour = colour

    def say(self):
        return f'Meow, my name is {self.name} and my breed is {self.breed}, also I have my {self.colour} colour'


my_dog = Dog('Chappy', 'Hasky')
my_cat = Cat('Catty', 'Scottish', 'Black')

print(my_dog.say())
print(my_cat.say())