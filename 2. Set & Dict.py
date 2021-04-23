####$$$$ ~~~~~~~~~~~~~  Set ~~~~~~~~~~~~~$$$$####
####$$$$ ~~~~~~~~~~~~~  Set ~~~~~~~~~~~~~$$$$####
####$$$$ ~~~~~~~~~~~~~  Set ~~~~~~~~~~~~~$$$$####


myset = {"hi", 2, "bye", "Hello World",123,5444,0,0,0,'hi'}
##print(myset)

        #~~~~~output
        ##{'hi', 2, 'Hello World', 'bye'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##myset.add("Beginners")
##print(myset)

        #~~~~Ouput
        ##{2, 'BeginnersBook', 'hi', 'Hello World', 'bye'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##myset.update([2,3,4])
##print(myset)

        #~~~~Output
        ##{2, 3, 4, 'hi', 'bye', 'Hello World'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

myset.update([4,5], {1,6,8},(444,555,333))
print(myset)

        #~~~~Output
        ##{1, 2, 4, 5, 'hi', 6, 8, 'Hello World', 'bye'}



####$$$$ ~~~~~~~~~~~~~  Dict ~~~~~~~~~~~~~$$$$####
####$$$$ ~~~~~~~~~~~~~  Dict ~~~~~~~~~~~~~$$$$####
####$$$$ ~~~~~~~~~~~~~  Dict ~~~~~~~~~~~~~$$$$####

"""Dictionaries are Python’s implementation of a data structure
that is more generally known as an associative array.
A dictionary consists of a collection of key-value pairs.
Each key-value pair maps the key to its associated value """

"More than one entry per key is not allowed ( no duplicate key is allowed)"
"""The values in the dictionary can be of any type while the
        keys must be immutable like numbers, tuples or strings."""
"""Dictionary keys are case sensitive- Same key name but with the different
        case are treated as different keys in Python dictionaries."""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#to add a key-value pair to a dictionary

##key=int(input("Enter the key (int) to be added:"))
##value=int(input("Enter the value for the key to be added:"))
##d={}
##d.update({key:value})
##print("Updated dictionary is:")
##print(d)

        #~~~~Output
        ##Enter the key (int) to be added:12
        ##Enter the value for the key to be added:5
        ##Updated dictionary is:
        ##{12: 5}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#add a key-value pair to a dictionary

##d1={'A':1,'B':2}
##d2={'C':3}
##d1.update(d2)
##print("Concatenated dictionary is:")
##print(d1)

        #~~~~Output
        ##Concatenated dictionary is:
        ##{'A': 1, 'B': 2, 'C': 3}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#check if a given key exists in a dictionary or not

##d={'A':1,'B':2,'C':3}
##key=input("Enter key to check:")
##if key in d.keys():
##      print("Key is present and value of the key is:")
##      print(d[key])
##else:
##      print("Key isn't present!")

        #~~~~Output
        ##Enter key to check:a
        ##Key isn't present!
        ##>>> 
        ##======= RESTART: E:\Study material\Examples for students\Set & Dict.py =======
        ##Enter key to check:A
        ##Key is present and value of the key is:
        ##1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#sum all the items in a dictionary

##d={'A':100,'B':540,'C':239}
##print("Total sum of values in the dictionary:")
##print(sum(d.values()))

        #~~~~Output
        ##Total sum of values in the dictionary:
        ##879

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#multiply all the items in a dictionary.

##d={'A':10,'B':10,'C':239}
##tot=1
##for i in d:    
##    tot=tot*d[i]
##print(tot)

        #~~~~Output
        ##23900

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #Counts the frequency of words appearing in that string using a dictionary.

        ##test_string=input("Enter string:")
        ##l=[]
        ##l=test_string.split()
        ##wordfreq=[l.count(p) for p in l]
        ##print(dict(zip(l,wordfreq)))

        #~~~~Output
        ##Enter string:conjection cannot be a conjection because its an conjection
        ##{'conjection': 3, 'cannot': 1, 'be': 1, 'a': 1, 'because': 1, 'its': 1, 'an': 1}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#create a dictionary with key as first character
        #and value as words starting with that character

##test_string=input("Enter string:")
##l=test_string.split()
##d={}
##for word in l:
##    if(word[0] not in d.keys()):
##        d[word[0]]=[]
##        d[word[0]].append(word)
##    else:
##        if(word not in d[word[0]]):
##          d[word[0]].append(word)
##for k,v in d.items():
##        print(k,":",v)

        #~~~~Output
        ##Enter string:this is a test string
        ##t : ['this', 'test']
        ##i : ['is']
        ##a : ['a']
        ##s : ['string']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program to form a dictionary from an object of a class

##class A(object):  
##     def __init__(self):  
##         self.A=1  
##         self.B=2  
##obj=A()  
##print(obj.__dict__)

        #~~~~Output
        ##{'A': 1, 'B': 2}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program to map two lists into a dictionary

##keys=[]
##values=[]
##n=int(input("Enter number of elements for dictionary:"))
##print("For keys:")
##for x in range(0,n):
##    element=int(input("Enter element" + str(x+1) + ":"))
##    keys.append(element)
##print("For values:")
##for x in range(0,n):
##    element=int(input("Enter element" + str(x+1) + ":"))
##    values.append(element)
##d=dict(zip(keys,values))
##print("The dictionary is:")
##print(d)

        #~~~~Output
        ##Enter number of elements for dictionary:2
        ##For keys:
        ##Enter element1:1
        ##Enter element2:2
        ##For values:
        ##Enter element1:12
        ##Enter element2:23
        ##The dictionary is:
        ##{1: 12, 2: 23}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Count the Frequency of Words Appearing in a String Using a Dictionary

##test_string=input("Enter string:")
##l=[]
##l=test_string.split()
##wordfreq=[l.count(p) for p in l]
##print(dict(zip(l,wordfreq))) 

        #~~~~Output
        ##Enter string:conjuction cannot be a conjuction because its a conjuction
        ##{'conjuction': 3, 'cannot': 1, 'be': 1, 'a': 2, 'because': 1, 'its': 1}

#Using the zip() function, merge the lists containing the words and the word counts into a dictionary.
