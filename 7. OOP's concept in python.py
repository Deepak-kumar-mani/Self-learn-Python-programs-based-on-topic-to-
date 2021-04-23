
####$$$~~~~~~~ Constructor ~~~~~~~~$$$####

""" Constructor is used for initializing the instance members when we create the object of a class. """

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Employee:  
##    id = 29;  
##    name = "Deepak"  
##    def display (self):  
##         print(self.id,self.name)    
##emp = Employee()  
##emp.display() 

        #~~~~~Output
        ##29 Deepak


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Creating the constructor in python

##class Employee:  
##    def __init__(self,name,id):  
##        self.id = id;  
##        self.name = name;  
##    def display (self):  
##        print(self.id,self.name)  
##emp1 = Employee("Deepak",101)  
##emp2 = Employee("Kumar",102)  

##emp1.display();   
##emp2.display();


        #~~~~~Output
        ##101 Deepak
        ##102 Kumar


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Non-Parameterized Constructor Example

##class Student:
        
    # Constructor - non parameterized    
##    def __init__(self):    
##        print("This is non parametrized constructor")    

##    def show(self,name):    
##        print("Hello",name)    

##student = Student()    
##student.show("Deepak")  

        #~~~~~Output
        ##This is non parametrized constructor
        ##Hello Deepak




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Parameterized Constructor Example

##class Student:    
##    # Constructor - parameterized    
##    def __init__(self, name):    
##        print("This is parametrized constructor")    
##        self.name = name    
##    def show(self):    
##        print("Hello",self.name)    
##student = Student("Deepak")    
##student.show()  

        #~~~~~Output
        ##This is parametrized constructor
        ##Hello Deepak


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Built-in class attributes

##class Student:  

##    def __init__(self,name,id1,age):  
##        self.name = name;  
##        self.id1 = id1;  
##        self.age = age  

##    def display_details(self):  
##        print("Name:%s, ID:%d, age:%d"%(self.name,self.id1))  

##s = Student("Deepak",101,22)

##print(s.__doc__)  
##print(s.__dict__)  
##print(s.__module__) 


        #~~~~~Output
        ##None
        ##{'name': 'Deepak', 'id1': 101, 'age': 22}
        ##__main__


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class animal:

    # class attribute
##    species = "bird"

    # instance attribute
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age

# instantiate the Parrot class
##blue = animal("Blue", 10)
##Red = animal("Red", 15)

# access the class attributes
##print("Blue is a {}".format(blue.__class__.species))
##print("Red is also a {}".format(Red.__class__.species))

# access the instance attributes
##print("{} is {} years old".format( blue.name, blue.age))
##print("{} is {} years old".format( Red.name, Red.age))

        #~~~~~Output
        ##Blue is a bird
        ##Red is also a bird
        ##Blue is 10 years old
        ##Red is 15 years old

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class animal:
    
    # instance attributes
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
    
    # instance method
##    def sing(self, song):
##        return "{} sings {}".format(self.name, song)

##    def dance(self):
##        return "{} is now dancing".format(self.name)

# instantiate the object
##blu = animal("Blue", 10)

# call our instance methods
##print(blu.sing("'Happy'"))
##print(blu.dance())

        #~~~~~Output
        ##Blue sings 'Happy'
        ##Blue is now dancing

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

####$$$$~~~~~~~~~ Inheritance ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Inheritance ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Inheritance ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Inheritance ~~~~~~~~~~$$$$####

""" Inheritance is a way of creating new class for using details of existing
class without modifying it. The newly formed class is a derived class
(or child class). Similarly, the existing class is a base class
(or parent class)."""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Parent():
##       def first(self):
##           print('first function')
 
##class Child(Parent):
##       def second(self):
##          print('second function')
 
##ob = Child()
##ob.first()
##ob.second()

        #~~~~~Output
        ##first function
        ##second function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Multiple Inheritance

##class P1:
##   def func1(self):
##        print("this is function 1")
##class P2:
##   def func2(self):
##        print("this is function 2")
##class C(P1 , P2):
##    def func3(self):
##        print("this is function 3")
 
##x = C()
##x.func1()
##x.func2()
##x.func3()

        #~~~~~Output
        ##this is function 1
        ##this is function 2
        ##this is function 3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Multilevel Inheritance

##class P1:
##   def func1(self):
##        print("this is function 1")
##class C1(P1):
##   def func2(self):
##        print("this is function 2")
##class C2(C1):
##    def func3(self):
##        print("this is function 3")
 
##x = C2()
##x.func1()
##x.func2()
##x.func3()

        #~~~~~Output
        ##this is function 1
        ##this is function 2
        ##this is function 3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Hierarchical Inheritance

##class Parent:
##      def func1(self):
##          print("this is function 1")
##class Child(Parent):
##      def func2(self):
##          print("this is function 2")
##class Child2(Parent):
##      def func3(self):
##          print("this is function 3")
 
##x = Child()
##x1 = Child2()
##x.func1()
##x.func2()
##x1.func1()
##x1.func3()

        #~~~~~Output
        ##this is function 1
        ##this is function 2
        ##this is function 1
        ##this is function 3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Bird:
    
##    def __init__(self):
##        print("Bird is ready")

##    def whoisThis(self):
##        print("Bird")

##    def swim(self):
##        print("Swim faster")

# child class
##class Penguin(Bird):

##    def __init__(self):
        # call super() function
##        super().__init__()
##        print("Penguin is ready")

##    def whoisThis(self):
##        print("Penguin")

##    def run(self):
##        print("Run faster")

##peggy = Penguin()
##peggy.whoisThis()
##peggy.swim()
##peggy.run()

        #~~~~~Output
        ##Bird is ready
        ##Penguin is ready
        ##Penguin
        ##Swim faster
        ##Run faster


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Person:  
##    name = ""  
##    age = 0  
  
##    def __init__(self, personName, personAge):  
##        self.name = personName  
##        self.age = personAge  
  
##    def showName(self):  
##        print(self.name)  
  
##    def showAge(self):  
##        print(self.age)  
  
  
##class Student(Person):
##        studentId = ""

##        def __init__(self, studentName, studentAge, studentId):
##            Person.__init__(self, studentName, studentAge)
##            self.studentId = studentId

##        def getId(self):
##                return self.studentId  
  
##person1 = Person("Richard", 23)  
##person1.showAge()  
##student1 = Student("Max", 22, "102")  
##print(student1.getId())  
##student1.showName()  

        #~~~~~Output
        ##23
        ##102
        ##Max

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

####$$$$~~~~~~~~~ Encapsulation ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Encapsulation ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Encapsulation ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Encapsulation ~~~~~~~~~~$$$$####

""" Using OOP in Python, we can restrict access to methods and variables.
This prevent data from direct modification which is called encapsulation.
In Python, we denote private attribute using underscore as prefix
i.e single “ _ “ or double “ __“."""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Computer:

##    def __init__(self):
##        self.__maxprice = 900

##    def sell(self):
##        print("Selling Price: {}".format(self.__maxprice))

##    def setMaxPrice(self, price):
##        self.__maxprice = price

##c = Computer()
##c.sell()

##c.__maxprice = 1000
##c.sell()

##c.setMaxPrice(1000)
##c.sell()

        #~~~~~Output
        ##Selling Price: 900
        ##Selling Price: 900
        ##Selling Price: 1000


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Car:

##    def __init__(self):
##        self.__updateSoftware()

##    def drive(self):
##        print('driving')

##    def __updateSoftware(self):
##        print('updating software')

##redcar = Car()
##redcar.drive()


        #~~~~~Output
        ##updating software
        ##driving



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Car:

##    __maxspeed = 0
##    __name = ""
    
##    def __init__(self):
##        self.__maxspeed = 200
##        self.__name = "Supercar"
    
##    def drive(self):
##        print('driving. maxspeed ' ,self.__maxspeed)

##    def MaxSpeed(self,speed):
##        self.__maxspeed = speed

##redcar = Car()
##redcar.drive()
##redcar.MaxSpeed(320)
##redcar.drive()

        #~~~~~Output
        ##driving. maxspeed 200
        ##driving. maxspeed 320

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

####$$$$~~~~~~~~~ Polymorphism ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Polymorphism ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Polymorphism ~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~ Polymorphism ~~~~~~~~~~$$$$####



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Parrot:

##    def fly(self):
##        print("Parrot can fly")
    
##    def swim(self):
##        print("Parrot can't swim")

##class Penguin:

##    def fly(self):
##        print("Penguin can't fly")
    
##    def swim(self):
##        print("Penguin can swim")

##def flying_test(bird):
##    bird.fly()

##blu = Parrot()
##peggy = Penguin()

##flying_test(blu)
##flying_test(peggy)

        #~~~~~Output
        ##Parrot can fly
        ##Penguin can't fly


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Bear():
##    def sound(self):
##        print("Groarrr")
    
##class Dog():
##    def sound(self):
##        print("Woof woof!")
    
##def makeSound(animalType):
##        animalType.sound()
    

##bearObj = Bear()
##dogObj = Dog()
    
##makeSound(bearObj)
##makeSound(dogObj)


        #~~~~~Output
        ##Groarrr
        ##Woof woof






