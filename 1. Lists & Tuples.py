##~~~~~~~~~ List ~~~~~~~~~##

##a = [10,20,30,40,50,60,70,80,90]
##print(a)
##print(len(a))
##print(min(a))
##print(max(a))

                #~~~~Output
                ##[10, 20, 30, 40, 50, 60, 70, 80, 90]
                ##9
                ##10
                ##90

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##print (a + [100,110,120])

                #~~~~Output
                ##[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##print (a[0])

                #~~~~Output
                ##10


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##a[0]=15
##print(a)

                #~~~~Output
                ##[15, 20, 30, 40, 50, 60, 70, 80, 90]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##print (a*3)

                #~~~~Output
                ##[10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##a = [10,20,[30,40,50],60]
##print (a)

                #~~~~Output
                ##[10, 20, [30, 40, 50], 60]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##a = [10,20,[30,40,50],60]
##print (a[2])

                #~~~~Output
                ##[30, 40, 50]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##a = [10,20,[30,40,50],60]
##print (a[2][0])

                #~~~~Output
                ##30

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##find the largest number in a list

##a=[]
##n=int(input("Enter number of elements:"))
##for i in range(1,n+1):
##    b=int(input("Enter element:"))
##    a.append(b)
##a.sort()
##print("Largest element is:",a[n-1])

                #~~~~Output
                ##Enter number of elements:5
                ##Enter element:45
                ##Enter element:32
                ##Enter element:5
                ##Enter element:000
                ##Enter element:5
                ##Largest element is: 45

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#find the second largest number in a list

##a=[]
##n=int(input("Enter number of elements:"))
##for i in range(1,n+1):
##    b=int(input("Enter element:"))
##    a.append(b)
##a.sort()
##print("Second largest element is:",a[n-2])

                #~~~~Output
                ##Enter number of elements:3
                ##Enter element:45
                ##Enter element:55
                ##Enter element:66
                ##Second largest element is: 55

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program to put the even and odd elements in a list into two different lists
##a=[]
##n=int(input("Enter number of elements:"))
##for i in range(1,n+1):
##    b=int(input("Enter element:"))
##    a.append(b)
##even=[]
##odd=[]
##for j in a:
##    if(j%2==0):
##        even.append(j)
##    else:
##        odd.append(j)
##print("The even list",even)
##print("The odd list",odd)

                #~~~~Output
                ##Enter number of elements:6
                ##Enter element:44
                ##Enter element:55
                ##Enter element:66
                ##Enter element:77
                ##Enter element:88
                ##Enter element:99
                ##The even list [44, 66, 88]
                ##The odd list [55, 77, 99]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# to merge two lists and sort it

##a=[]
##c=[]
##n1=int(input("Enter number of elements:"))
##for i in range(1,n1+1):
##    b=int(input("Enter element:"))
##    a.append(b)
##n2=int(input("Enter number of elements:"))
##for i in range(1,n2+1):
##    d=int(input("Enter element:"))
##    c.append(d)
##new=a+c
##new.sort()
##print("Sorted list is:",new)


                #~~~~Output
                ##Enter number of elements:5
                ##Enter element:11
                ##Enter element:22
                ##Enter element:33
                ##Enter element:44
                ##Enter element:55
                ##Enter number of elements:3
                ##Enter element:66
                ##Enter element:77
                ##Enter element:88
                ##Sorted list is: [11, 22, 33, 44, 55, 66, 77, 88]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#to sort a list according to the length of the elements

##a=[]
##n=int(input("Enter number of elements:"))
##for i in range(1,n+1):
##    b=input("Enter element:")
##    a.append(b)
##a.sort(key=len)
##print(a)


                #~~~~Output
                ##Enter number of elements:4
                ##Enter element:1
                ##Enter element:123
                ##Enter element:23
                ##Enter element:456
                ##['1', '23', '123', '456']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#swap the first and last value of a list.

##a=[]
##n= int(input("Enter the number of elements in list:"))
##for x in range(0,n):
##    element=int(input("Enter element" + str(x+1) + ":"))
##    a.append(element)
##temp=a[0]
##a[0]=a[n-1]
##a[n-1]=temp
##print("New list is:")
##print(a)


                #~~~~Output
                ##Enter the number of elements in list:5
                ##Enter element1:1
                ##Enter element2:2
                ##Enter element3:3
                ##Enter element4:4
                ##Enter element5:5
                ##New list is:
                ##[5, 2, 3, 4, 1]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#read a list of words and return the length of the longest one

##a=[]
##n= int(input("Enter the number of elements in list:"))
##for x in range(0,n):
##    element=input("Enter element" + str(x+1) + ":")
##    a.append(element)
##max1=len(a[0])
##temp=a[0]
##for i in a:
##    if(len(i)>max1):
##       max1=len(i)
##       temp=i
##print("The word with the longest length is:")
##print(temp)


                #~~~~Output
                ##Enter the number of elements in list:5
                ##Enter element1:1
                ##Enter element2:asd
                ##Enter element3:asdf
                ##Enter element4:qwer
                ##Enter element5:zxcc
                ##The word with the longest length is:
                ##asdf


#####~~~~~~~~~~  Tuple ~~~~~~~~~~~~~####


##my_tuple = ()
##print(type(my_tuple))

                #~~~~Output
                ##<class 'tuple'>

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##my_tuple = (1, 2, 3)
##print(my_tuple)

                #~~~~Output
                ##(1, 2, 3)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##my_tuple = (1, "Hello", 3.4)
##print(my_tuple)

                #~~~~Output
                ##(1, 'Hello', 3.4)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##my_tuple = 3, 4.6, "dog"
##print(my_tuple)
##print(type(my_tuple))

                #~~~~Output
                ##(3, 4.6, 'dog')
                ##<class 'tuple'>

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##tuple1 = (0, 1, 2, 3) 
##tuple2 = ('python', 'FITA')
##print(tuple1 + tuple2)

        #~~~~~ Output
        ##(0, 1, 2, 3, 'python', 'FITA')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##tuple1 = (0, 1, 2, 3) 
##tuple2 = ('python', 'FITA') 
##tuple3 = (tuple1, tuple2) 
##print(tuple3)
          
        #~~~~Ouput
        ##((0, 1, 2, 3), ('python', 'FITA'))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##list1 = [0, 1, 2] 
##print(tuple(list1))

##print(tuple('python'))

        #~~~~Ouput
        ##(0, 1, 2)
        ##('p', 'y', 't', 'h', 'o', 'n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Search within Tuple
##a=(3,5,7,11,13,17);
##print (3 in a)
##print (43 in a)

        #~~~~Output
        ##True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Adding elements to tuple
# The following line will give an error message.
##a.append(91)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Deleting a Tuple
##del a

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Iterating over a tuple
##a =(3,5,7,11,13,17);
##for x in a:
## print (x);

        #~~~~~Output
        ## 3
        ##5
        ##7
        ##11
        ##13
        ##17

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Concatenation
##a=(3,5,7,11,13);
##b=("c","c++","java","angular");
##print(a+b)

        #~~~~Ouput
        ##(3, 5, 7, 11, 13, 'c', 'c++', 'java', 'angular')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Length of tuple
##print(len(b+a))

        #~~~~Ouput
        ##9

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Slicing operator
##print(a[0:3])


        #~~~~Ouput
        ##(3, 5, 7)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Count function
a=(3,5,7,11,13,11,7,11,11);
print(a.count(11))

        #~~~~Ouput
        ##1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Index function
##print(a.index(11))


        #~~~~Ouput
        ##0







