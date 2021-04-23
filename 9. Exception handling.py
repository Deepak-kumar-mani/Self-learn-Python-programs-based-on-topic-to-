
####$$$~~~~~~ Exception ~~~~~~$$$####

""" In Python, exceptions can be handled using a try statement. ...
The portion that can cause exception is placed inside try block.
If no exception occurs, except block is skipped and normal flow continues.
But if any exception occurs, it is caught by the except block.  """

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##a = [1, 2, 3] 
##try:  
##    print("Second element = %d" %(a[1])) 
##    print("Fourth element = %d" %(a[3]))
  
##except IndexError: 
##    print("An error occurred")


        #~~~~Output
        ##Second element = 2
        ##An error occurred


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##try :  
##    a = 4
##    if a < 4 :
##            b = a/(a-3)
##    print("Value of b = ", b)
##except(ZeroDivisionError, NameError): 
##    print("\nError Occurred and Handled")


        #~~~~Output
        ##Value of b =  -2.0

        #~~~~Output(if the a value is greater than 4)
        ##Error Occurred and Handled

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##while True:
##     try:
##         x = int(input("Please enter a number: "))
##         break
##     except ValueError:
##         print("Oops!  That was no valid number.  Try again...")

        #~~~~Output
        ##Please enter a number: 
        ##Oops!  That was no valid number.  Try again...
        ##Please enter a number: 123
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import sys
##randomList = ['a', 0, 2]
##for entry in randomList:
##    try:
##        print("The entry is", entry)
##        r = 1/int(entry)
##        break
##    except:
##        print("Oops!",sys.exc_info()[0],"occured.")
##        print("Next entry.")
##        print()
##print("The reciprocal of",entry,"is",r)


        #~~~~Output
        ##The entry is a
        ##Oops! <class 'ValueError'> occured.
        ##Next entry.
        ##
        ##The entry is 0
        ##Oops! <class 'ZeroDivisionError'> occured.
        ##Next entry.
        ##
        ##The entry is 2
        ##The reciprocal of 2 is 0.5


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" The raise statement allows the programmer to force a specific exception
to occur. The sole argument in raise indicates the exception to be raised.
This must be either an exception instance or an exception class  """

##try:  
##    raise NameError("Hi there")
##except NameError: 
##    print("An exception")
##    raise 

        #~~~~Output
        ##An exception
        ##NameError: Hi there


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import sys
##try:
##    f = open('myfile.txt')
##    s = f.readline()
##    i = int(s.strip())
##except OSError as err:
##    print("OS error: {}".format(err))
##except ValueError:
##    print("Could not convert data to an integer.")
##except:
##    print("Unexpected error:", sys.exc_info()[0])
##    raise

        #~~~~Output
        ##OS error: [Errno 2] No such file or directory: 'myfile.txt'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def input_age(age):
##   try:
##       if(int(age)<=18):
##           raise ZeroDivisionError
##   except ValueError:
##       return 'ValueError: Cannot convert into int'
##   else:
##       return 'Age is saved successfully'

##print(input_age('23'))  
##print(input_age('18'))


        #~~~~Output
        ##Age is saved successfully
        ##    raise ZeroDivisionError
        ##ZeroDivisionError

        #~~~~Output (if the input age is given as string)
        ##Age is saved successfully
        ##ValueError: Cannot convert into int

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class MyError(Exception):
##        
##    def __init__(self, value): 
##        self.value = value 
##
##    def __str__(self): 
##        return(repr(self.value)) 
##try: 
##    raise(MyError(3*2)) 
##except MyError as error: 
##    print('A New Exception occured: ',error.value) 

        #~~~~Output
        ##A New Exception occured:  6


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class UnderAge(Exception):
##   pass
##
##def verify_age(age):
##   if int(age) < 18:
##       raise UnderAge
##   else:
##       print('Age: '+str(age))

##verify_age(23)  
##verify_age(17) 

        #~~~~Output
        ##Age: 23
        ##raise UnderAge
        ##UnderAge


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class B(Exception):
##    pass
##class C(B):
##    pass
##class D(C):
##    pass

##for cls in [B, C, D]:
##    try:
##        raise cls()
##    except D:
##        print("D")
##    except C:
##        print("C")
##    except B:
##        print("B")

        #~~~~Output
        ##B
        ##C
        ##D

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class NumberTooSmallError(Exception):
##        pass
## 
##class NumberTooBigError(Exception):
##    message = '\nException: NumberTooBigError:\nYour number is too big. \nTry a smaller one!'
## 
##class NumberThreeError(Exception):
##    def __init__(self):
##        print('\nException: ThreeNumberError:\nThree is not number ya\'re lookin\' for.\n')
## 
##class NumberFiveError(Exception):
##        pass #uncaught exception
 
 
#function that uses user-defined exceptions
##def checkNumber(num):
##    if(num == 3):
##        raise NumberThreeError
##    elif(num == 5):
##        raise NumberFiveError
##    elif(num < 99):
##        raise NumberTooSmallError("Exception: given number is too small")
##    elif(num > 99):
##        raise NumberTooBigError("Exception: given number is too big")
##    return num
 
 
#python try...catch block (why it is called try...except?)
##while 1:
##    try:
##        usrInput = int(input( "\nPlease enter the magic number: " ))
##        print(checkNumber(usrInput))
##    except NumberTooSmallError:
##        print("Number too small")
##    except NumberTooBigError as e:
##        print("Number too big" + e.message)
##    except NumberThreeError:
##        print('Ooops!')
##    else:
##        break
 

        #~~~~Output
        ##Please enter the magic number: 3
        ##
        ##Exception: ThreeNumberError:
        ##Three is not number ya're lookin' for.
        ##
        ##Ooops!
        ##
        ##Please enter the magic number:



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~Output


