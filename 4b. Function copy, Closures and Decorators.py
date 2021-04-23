##~~~~~~~~~~~ function copy ~~~~~~~~~~~~~~~~~ ##


##def welcome():
##    print("Welcome python class")
##welcome()

                  #------Output
                  ## Welcome python class

##def welcome():
##    print("Welcome python class")
##wel = welcome()
##print(wel)

                  #------Output
                  ## Welcome python class
                  ## None

##def welcome():
##    return "Welcome python class"
##wel=welcome()
##del welcome

                  #------Output
                  ## there will be no output


##def welcome():
##    return "Welcome python class"
##wel=welcome()
##del welcome
##welcome()

                  #------Output
                  ## NameError: name 'welcome' is not defined


##def welcome():
##    return "Welcome python class"
##wel=welcome()
##del welcome
##print(wel)

                  #------Output
                  ## Welcome python class



##~~~~~~~~~~~~ closures  ~~~~~~~~~~## decorators
"""
its nothing but a function inside a function
here what we do is as a user we will provide input to main function and we
also use it inside sub function
whatever the variable is available in main function can be acced in sub function
"""

##def main_welcome():
##      msg = " Hello "
##      def sub_welcome_class():
##            print("welcome to python class")
##            print(msg)
##            print("EnJoY as python developer ")

"""
1.) when i write a function inside a function can i use the msg variable from main
function inside a sub function -- Ans) yes we can defenitly access it
2.) we need to return the main function
"""

##def main_welcome():
##      msg = " Hello "
##      def sub_welcome_class():
##            print("welcome to python class")
##            print(msg)
##            print("EnJoY as python developer ")
##      return sub_welcome_class
##main_welcome()


                  #------Output
                  ## there will be no output a memory address will be created


##def main_welcome():
##      msg = " Hello "
##      def sub_welcome_class():
##            print("welcome to python class")
##            print(msg)
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##main_welcome()
"""
pls note here what ever msg i have passed in the main class has been printed
in the sub class
"""
                  #------Output
                  ## welcome to python class
                  ## Hello 
                  ## EnJoY as python developer 


##def main_welcome(msg):
##      def sub_welcome_class():
##            print("welcome to python class")
##            print(msg)
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##main_welcome("Student")


                  #------Output
                  ## welcome to python class
                  ## Student
                  ## EnJoY as python developer 


##def main_welcome(fun):
##      def sub_welcome_class():
##            print("welcome to python class")
##            fun         # here we have not declared or assigned for the argument passed
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##main_welcome(print)
"""
Here i'm passing a pring function to the main function below is my output
"""


                  #------Output
                  ## welcome to python class
                  ## EnJoY as python developer 


##~~~~~~~~~~~ decorators ~~~~~~~~~~##
"""
decorator is inside a function we can give a parameter as function
insted of specifice variable or a msg
"""

#this is the starter of decorators or initial of decorators
##def main_welcome(fun):
##      def sub_welcome_class():
##            print("welcome to python class")
##            fun("We are learning Python")
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##main_welcome(print)
"""
Here we are passing print function to the main class argument and that returns
the sub function and its been called now the fun is replaced with the print and
its get printed
"""

                  #------Output
                  ## welcome to python class.
                  ## We are learning Python.
                  ## EnJoY as python developer.



##def main_welcome(fun):
##      def sub_welcome_class():
##            print("welcome to python class")
##            print(fun("We are learning Python"))
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##main_welcome(len)

                  #------Output
                  ## welcome to python class.
                  ## 22
                  ## EnJoY as python developer.



##def main_welcome(fun):
##      def sub_welcome_class():
##            print("welcome to python class")
##            fun()
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##
##def new_fun():
##      print("We are enjoying python")

##main_welcome(new_fun)

                  #------Output
                  ## welcome to python class
                  ## We are enjoying python
                  ## EnJoY as python developer 

"""
the other way of calling the function by using @main_function
"""

##def main_welcome(fun):
##      def sub_welcome_class():
##            print("welcome to python class")
##            fun()
##            print("EnJoY as python developer ")
##      return sub_welcome_class()  ## here we have included the function call 
##
##@main_welcome     ##<--  <-- this is the decorator
##def new_fun():
##      print("We are enjoying python")

                  #------Output
                  ## welcome to python class
                  ## We are enjoying python
                  ## EnJoY as python developer 
