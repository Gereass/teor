class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")
        self.a = 47
        print(self.a)
        

person = Person("Alice")
person.say_hello() # выведет "Hello, my name is Alice"