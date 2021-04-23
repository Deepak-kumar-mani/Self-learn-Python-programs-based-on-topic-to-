##~~~~~~~~ Magic Method in class ~~~~~~~~##

## All the class variables are public
## its a blueprint

##class car():
##      def __init__(self, windows, doors, enginetype): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.enginetype = enginetype
##      def drive(self):  # Method inside the class
##            print("The person drives the car")
##c=car(4, 6, 'Petrol')

                        #----- Output
                        ## there will be no output over here


##print(dir(c))

"""
the output here are all the magic methods of the class attribute 'c'
"""
                        #----- Output
                        ## ['__class__', '__delattr__', '__dict__', '__dir__',
                        ## '__doc__', '__eq__', '__format__', '__ge__',
                        ## '__getattribute__', '__gt__', '__hash__',
                        ## '__init__', '__init_subclass__', '__le__', '__lt__',
                        ## '__module__', '__ne__', '__new__', '__reduce__',
                        ## '__reduce_ex__', '__repr__', '__setattr__',
                        ## '__sizeof__', '__str__', '__subclasshook__',
                        ## '__weakref__', 'doors', 'drive', 'enginetype', 'windows']


##class car():
##      def __init__(self, windows, doors, enginetype): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.enginetype = enginetype
##      def drive(self):  # Method inside the class
##            print("The person drives the car")
##c=car(4, 6, 'Petrol')
##print(c)
"""
Here when we print the class object c it calls the magic method __str__ by
refering the memory object
We can always over ride the magic method
"""
                        #----- Output
                        ## <__main__.car object at 0x03333B10>


#Over riding the magic methods
##class car():
##      def __init__(self, windows, doors, enginetype): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.enginetype = enginetype
##      def __str__(self):
##            return "the obj has been initialized" ## magic method always return 
##      def drive(self):  # Method inside the class
##            print("The person drives the car")
##c=car(4, 6, 'Petrol')
##print(c)
                        #----- Output
                        ## the obj has been initialized


##print(c.__sizeof__())
                        #----- Output
                        ## 16


"""
Now i want to over ride the magic method sizeof
"""
##class car():
##      def __init__(self, windows, doors, enginetype): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.enginetype = enginetype
##      def __sizeof__(self):
##            return "this displays the sixe of the object"
##      def __str__(self):
##            return "the obj has been initialized" ## magic method always return 
##      def drive(self):  # Method inside the class
##            print("The person drives the car")
##c=car(4, 6, 'Petrol')
##print(c)
                        #----- Output
                        ## the obj has been initialized


##print(c.__sizeof__())
                        #----- Output
                        ## this displays the sixe of the object
