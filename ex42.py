## Animal is-a object 
class Animal(object):
    pass

#
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

##Person is an object
class Person(object):

    def __init__(self, name):
        #Person has a self 
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        #"Employee has name and salary"
        #
        super(Employee, self).__init__(name)
        #
        self.salary = salary

# class x()
"## make a class named fish that is an object
class Fish(object):
    pass

## make class Salmon that is a Fish
class Salmon(Fish):
    pass

## make class Halibut that is an instance of Fish(another class)
class Halibut(Fish):
    pass


# rover is an instance of class Dog
#foo = x()  set foo to an instance of X
rover = Dog("Rover")

## satan is an instance of class cat
satan = Cat("Satan")

## mary is an instance of person
mary = Person("Mary")

# foo.k = Q
#from foo get the K attribute and set it to Q
#from mary get the pet attribute and set it to satan
#Mary has a pet that is Satan
mary.pet = satan

#foo = X(self, j) set foo to an instance of class x
#frank is an instance of class employee
frank = Employee("Frank", 120000)

#Frank has a pet that is rover
frank.pet = rover

#flipper is an instance of fish
flipper = Fish()

##foo = x() set foo to an instance of x
#crouse is a salmon
crouse = Salmon()

##harry is an instance of Halibut
harry = Halibut()