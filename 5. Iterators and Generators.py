####$$$$~~~~~~~~~~ Iterators ~~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~~ Iterators ~~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~~ Iterators ~~~~~~~~~~~$$$$####

"""
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can
traverse through all the values and which will return data, one element at a time.

Python iterator object must implement two special methods, __iter__()
and __next__(), collectively called the iterator protocol

"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##mytuple = ("a", "b", "c")
##myit = iter(mytuple)
##
##print(next(myit))
##print(next(myit))
##print(next(myit))

        #~~~~Output
        ##a
        ##b
        ##c

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##my_list = [4, 7, 0, 3]
##my_iter = iter(my_list)
##print(next(my_iter))
##print(next(my_iter))
##print(my_iter.__next__())
##print(my_iter.__next__())

        #~~~~Output
        ##4
        ##7
        ##0
        ##3



####$$$$~~~~~~~~~~ Generators ~~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~~ Generators ~~~~~~~~~~~$$$$####
####$$$$~~~~~~~~~~ Generators ~~~~~~~~~~~$$$$####

"""
Generators are used to create iterators, but with a different approach.
Generators are simple functions which return an iterable set of items,
one at a time, in a special way

"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def my_gen():
##    n = 1
##    print('This is printed first',n )
##    yield n

##    n += 1
##    print('This is printed second',n)
##    yield n

##    n += 1
##    print('This is printed at last',n)
##    yield n

##a = my_gen()
##next(a)
##next(a)
##next(a)

        #~~~~Output
        ##This is printed first 1
        ##This is printed second 2
        ##This is printed at last 3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def simpleGeneratorFun(): 
##    yield 1            
##    yield 2            
##    yield 3  

##for value in simpleGeneratorFun():  
##    print(value)
    
        #~~~~Output
        ##1
        ##2
        ##3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def fruits():
##   yield "Mango"
##   yield "Jackfruit"
##   yield "Banana"
##   yield  "Guava"

##getfruits = fruits()
##print(next(getfruits))
##print(next(getfruits))
##print(next(getfruits))
##print(next(getfruits))

        #~~~~Output
        ##Mango
        ##Jackfruit
        ##Banana
        ##Guava
