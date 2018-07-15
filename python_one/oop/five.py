class Animal(object):
    def print_info(self):
        print('Animal is running')



#animal = Animal()
#animal.print_info()


class Cat(Animal):
    def print_info(self):
        print('Cat is running')




class Dog(Animal):
    def print_info(self):
        print('Dog is running')



cat = Cat()
cat.print_info()
dog = Dog()
dog.print_info()
