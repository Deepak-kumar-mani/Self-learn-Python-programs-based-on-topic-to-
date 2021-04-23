## Abstract class

##class shape():
##      def area(self): pass
##      def perimeter(self): pass

"""
pls note here shape class will act like a templet for square class
and i dont want to allow the user to create an instant for the shape class
"""
##class square(shape):  
##      def __init__(self, side):
##            self.__side = side
##
##shape = shape()

                        ## Output --> here my code runs fine that is
                        ## i can creat an instance for the shape class
                        ## which i dont want
"""
the second this is the method inside the shape class is implemented inside the
square class
"""

## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##from abc import ABC, abstractmethod
##class shape(ABC):
##      
##      @abstractmethod
##      def area(self): pass
##
##      @abstractmethod
##      def perimeter(self): pass
##
##
##class square(shape):  
##      def __init__(self, side):
##            self.__side = side
##
##shape = shape()

                        ## Output
                        ## TypeError: Can't instantiate abstract class shape
                        ## with abstract methods area,perimeter




##from abc import ABC, abstractmethod
##class shape(ABC):
##      
##      @abstractmethod
##      def area(self): pass
##
##      @abstractmethod
##      def perimeter(self): pass


##class square(shape):  
##      def __init__(self, side):
##            self.__side = side

##squ = square(2)

                        ## Output
                        ## TypeError: Can't instantiate abstract class square
                        ## with abstract methods area,perimeter





##from abc import ABC, abstractmethod
##class shape(ABC):
##      @abstractmethod
##      def area(self): pass
##      def perimeter(self): pass
##
##class square(shape):  
##      def __init__(self, side):
##            self.__side = side
##      def area(self):
##            return self.__side * self.__side
##
##squ = square(2)
"""
If we note here we have only one abstract method in the shape class
and that we have instantiated in the square class
so it will run perfectly
"""
                        ## Output
                        ## there will be no output



##from abc import ABC, abstractmethod
##class shape(ABC):
##      
##      @abstractmethod
##      def area(self): pass
##
##      @abstractmethod
##      def perimeter(self): pass
##
##
##class square(shape):  
##      def __init__(self, side):
##            self.__side = side
##      def area(self):
##            return self.__side * self.__side
##
##squ = square(2)

                        ## Output
                        ## TypeError: Can't instantiate abstract class square
                        ## with abstract methods perimeter





from abc import ABC, abstractmethod
class shape(ABC):
      
      @abstractmethod
      def area(self): pass

      @abstractmethod
      def perimeter(self): pass


class square(shape):  
      def __init__(self, side):
            self.__side = side
      def area(self):
            return self.__side * self.__side
      def perimeter(self):
            return 4* self.__side

squ = square(2)
print(squ.area())
print(squ.perimeter())



                  ## Output
                  ## 4
                  ## 8
