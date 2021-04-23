## ClassMethod and Class Variables
"""
Whenever we want to update a class variable we use @classmethod
"""

##class car():
##      base_price = 10000  # this the class variable
##      def __init__(self, windows, doors, power): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.power = power
##      def what_base_price(self):
##            print("the base priccd is {}".format(self.base_price))
"""
There are two was to get the class variable
"""
##car1 = car(4, 5, 2000)
##print(car1.base_price) # method 1 calling by instant method
##print(car.base_price) # method 2 calling directly by class name

                  #----- Output
                  ## 10000
                  ## 10000



## Now i have a condition output that every year i want to add
## infilation rate of 10% to introduce that we use a @classmethod

##class car():
##      base_price = 10000  # this the class variable
##      def __init__(self, windows, doors, power): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.power = power
##      def what_base_price(self):
##            print("the base priccd is {}".format(self.base_price))
##      @classmethod                                    ## this method directly refers to the class
##      def revise_base_price(cls, inflation):          ## this cls refers to the class method
##            cls.base_price = cls.base_price+inflation*cls.base_price

##car.revise_base_price(0.10)
##car1 = car(4, 5, 2000)
##print(car1.base_price)
##print(car.base_price)

                  #----- Output
                  ## 11000
                  ## 11000




## ~~~~~~ Static Method ~~~~~~~~~##
import datetime
now = datetime.datetime.now()
print(now.year)
                  #----- Output
                  ## 2021
##class car():
##      base_price = 10000  # this the class variable
##      def __init__(self, windows, doors, power): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.power = power
##      def what_base_price(self):
##            print("the base priccd is {}".format(self.base_price))
##
##      @classmethod      ## this method directly refers to the class
##      def revise_base_price(cls, inflation):          ## this cls refers to the class method
##            cls.base_price = cls.base_price+inflation*cls.base_price
##
##      @staticmethod     ## is statics method we do not provide any parameter like self or cls
##      def check_year():    ## pls note when class is loaded the first method to initialize is static method
##            if now.year == 2021:
##                  return True
##            else:
##                  return False
##print(car.check_year())
                  #----- Output
                  ## True


##class car():
##      base_price = 10000  # this the class variable
##      def __init__(self, windows, doors, power): # this is a initializing constructur
##            self.windows = windows
##            self.doors = doors
##            self.power = power
##      def what_base_price(self):
##            print("the base priccd is {}".format(self.base_price))
##
##      @classmethod      ## this method directly refers to the class
##      def revise_base_price(cls, inflation):          ## this cls refers to the class method
##            cls.base_price = cls.base_price+inflation*cls.base_price
##
##      @staticmethod     ## is statics method we do not provide any parameter like self or cls
##      def check_year():    ## pls note when class is loaded the first method to initialize is static method
##            if now.year == 2021:
##                  return True
##            else:
##                  return False
##car1 = car(6, 5, 1780)
##if (car.check_year()):
##      pass
##else:
##      car.revise_base_price(0.10)
##print(car.base_price)

                  #----- Output
                  ## 100000
