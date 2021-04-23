####$$$~~~~~~~~~~~ Lambda ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Lambda ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Lambda ~~~~~~~~~~~~~~~~$$$####

""" In Python, anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword, in Python anonymous
functions are defined using the lambda keyword. Anonymous functions are also 
called lambda functions."""

#Syntax #
##lambda arguments: expression

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##x = lambda a : a + 10
##print(x(25))

        #~~~~Outputs
        ##35


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##x = lambda a, b : a * b
##print(x(10, 11))

        #~~~~Outputs
        ##110


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##double = lambda x: x * 2;
##print(double(5))

        #~~~~Outputs
        ##10

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def cube(y): 
##    return y*y*y; 
##print(cube(5))

        #~~~~Outputs
        ##125


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##a = lambda x: x*x*x 
##print(a(9)) 

        #~~~~Outputs
        ##729


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##my_list = [11, 55, 44, 66, 88, 101, 32, 121]
##new_list = list(filter(lambda x: (x%2 == 0) , my_list))
##print(new_list)

        #~~~~Outputs
        ##[44, 66, 88, 32]



####$$$~~~~~~~~~~~ Map ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Map ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Map ~~~~~~~~~~~~~~~~$$$####

"""Python map() function is used to apply the function on all the elements
of specified iterable and return map object. Python map() function applies
the given function to each item of an iterable like the list, tuple, etc.
and returns output as a list. Python map object is an iterator so that we
can iterate over its elements"""

## Syntax  ##

##map(function, iterables)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##chars = ['f', 'i', 't', 'a']
##def change_upper_case(s):
##    return str(s).upper()
##
##map_iterator = map(change_upper_case, chars)
##output_list = list(map_iterator)
##print(output_list)

        #~~~~Output
        ##['F', 'I', 'T', 'A']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##def to_upper_case(s):
##    return str(s).upper()

##map_iterator = map(to_upper_case, ['a', 'b', 'c'])
##my_list = list(map_iterator)
##print(my_list)

##map_iterator = map(to_upper_case, ['a', 'b', 'c'])
##my_set = set(map_iterator)
##print(my_set)

##map_iterator = map(to_upper_case, ['a', 'b', 'c'])
##my_tuple = tuple(map_iterator)
##print(my_tuple)

        #~~~~Outputs
        ##['A', 'B', 'C']
        ##{'C', 'B', 'A'}
        ##('A', 'B', 'C')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#map() with multiple iterable arguments of different sizes

##list_numbers = [1, 2, 3, 4]
##tuple_numbers = (5, 6, 7, 8, 9, 10)
##map_iterator = list(map(lambda x, y: x * y, list_numbers, tuple_numbers))
##print(map_iterator)

##map_iterator = list(map(lambda x, y: x * y, tuple_numbers, list_numbers))
##print(map_iterator)

        #~~~~Outputs
        ##[5, 12, 21, 32]
        ##[5, 12, 21, 32]


####$$$~~~~~~~~~~~ Join ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Join ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Join ~~~~~~~~~~~~~~~~$$$####

""" Python join() method is the method that returns the string concatenated
with the elements of an iterable.  Python String join() method provides a
flexible way to concatenate a string. It concatenates each element of an
iterable (such as a list, string, and a tuple) to the string and returns the
concatenated string """

# Syntax #
##string.join(iterable)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##X = ('Python', 'Fita', "at", "Annanagar")
##Y = '|'.join(X)
##print(Y)

        #~~~~Outputs
        ##Python|Fita|at|Annanagar

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##list1 = ['7','is','dhoni','no:']  
##a = "-"
##a= a.join(list1)
##print(a)

        #~~~~Outputs
        ##07-is-dhoni-no:


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##myDict = {"name": "John", "country": "Norway"}
##mySeparator = "TEST"
##x = mySeparator.join(myDict)
##print(x)

        #~~~~Outputs
        ##nameTESTcountry


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##s1 = 'abc'
##s2 = '123'
##""" Each character of s2 is concatenated to the front of s1""" 
##print('s1.join(s2):', s1.join(s2))
##""" Each character of s1 is concatenated to the front of s2""" 
##print('s2.join(s1):', s2.join(s1))

        #~~~~Outputs
        ##s1.join(s2): 1abc2abc3
        ##s2.join(s1): a123b123c


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##test =  {'mat': 1, 'that': 2}
##s = '->'
##print(s.join(test))

        #~~~~Outputs
        ##mat->that

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##test =  {1:'mat', 2:'that'}
##s = ', '
##print(s.join(test))

        #~~~~Outputs
        ##TypeError: sequence item 0: expected str instance, int found



####$$$~~~~~~~~~~~ Hash ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Hash ~~~~~~~~~~~~~~~~$$$####
####$$$~~~~~~~~~~~ Hash ~~~~~~~~~~~~~~~~$$$####

""" Hash is a fixed size integer which identifies a particular value,
hash() method to encode the data into unrecognisable value.
1) A hash is obtained from a hash function, whose responsibility is
to convert the given information to encoded hash.
2)Clearly, the number of objects can be much more than the number of
hash values and so, two objects may hash to the same hash value.
This is called Hash collision. This means that if two objects have
the same hash code, they do not necessarily have the same value.
"""

# Syntax #
##hash(object)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('Hash for 20 is:', hash(50))

        #~~~~Outputs
        ##Hash for 50 is: 50

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##print('Hash for 50.123 is:',hash(50.23))

        #~~~~Outputs
        ##Hash for 50.123 is: 579806217



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##print('Hash for Python is:', hash('Python'))

        #~~~~Outputs
        ##Hash for Python is: 970437435


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##name = "FITA"
##hash1 = hash(name)
##hash2 = hash(name)

##print("Hash 1: %s" % hash1)
##print("Hash 2: %s" % hash2)

        #~~~~Outputs
        ##Hash 1: -113069994
        ##Hash 2: -113069994

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##tuple_value = (21, 19, 18, 46, 29) # tuples are immutable  
##list_value = [11, 21, 31, 41, 51] # list are mutable
##print ("The tuple hash value is : " + str(hash(tuple_value))) 
##print ("The list hash value is : " + str(hash(list_value)))

        #~~~~Outputs
        ##The tuple hash value is : -1729947466
        ##TypeError: unhashable type: 'list

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Python String encode() decode()"""

##str_original = 'Learning python'

##bytes_encoded = str_original.encode(encoding='utf-8')
##print(type(bytes_encoded))

##str_decoded = bytes_encoded.decode()
##print(type(str_decoded))

##print('Encoded bytes =', bytes_encoded)
##print('Decoded String =', str_decoded)
##print('str_original equals str_decoded =', str_original == str_decoded)


        #~~~~Outputs
        ##<class 'bytes'>
        ##<class 'str'>
        ##Encoded bytes = b'Learning python'
        ##Decoded String = Learning python
        ##str_original equals str_decoded = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~Outputs
