##def my_function():
##  print("Hello from a function")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def fun(*names):
##  for name in names:
##       print("Hello",name)
##fun("ab","bc","cd","de")


        #~~~~Output
        ##Hello ab
        ##Hello bc
        ##Hello cd
        ##Hello de


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def fun(first, second, third, *Lst_Var):
##    print("First: %s" % first)
##    print("Second: %s" % second)
##    print("Third: %s" % third)
##    print("And all the rest... %s" % list(Lst_Var))
##fun(1,2,3,4,5)

        #~~~~Output
        ##First: 1
        ##Second: 2
        ##Third: 3
        ##And all the rest... [4, 5]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Warehouse:
##        purpose = 'storage'
##        region = 'west'
##
##w1 = Warehouse()
##print(w1.purpose, w1.region)
##w2 = Warehouse()
##w2.region = 'east'
##print(w2.purpose, w2.region)

        #~~~~Output
        ##storage west
        ##storage east



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class MyClass:
##	"This is my second class"
##	a = 10
##	def func():
##		print('Hello')
##print(MyClass.a)
##print(MyClass.func())

        #~~~~Output
        ##10
        ##Hello
        ##None


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class fun:
##    kind = 'cat'         
##    def __init__(self, name):
##        self.name = name    
##d = fun('dog')
##e = fun('mouse')
##print(d.kind)
##print(e.kind)           
##print(d.name)                  
##print(e.name)                  

        #~~~~Output
        ##cat
        ##cat
        ##dog
        ##mouse


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##class Person_details:
##  def __init__(self, name, age):
##    self.name = name
##    self.age = age
##
##p1 = Person_details("Dhoni", 37)
##
##print(p1.name)
##print(p1.age)
      
        #~~~~Output
        ##Dhoni
        ##37


