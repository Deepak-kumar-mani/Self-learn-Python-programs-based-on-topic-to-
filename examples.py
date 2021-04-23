        ##~~~~~~~~~~~~~~~ Basic programs ~~~~~~~~~~~~##

# Program to Calculate the Average of Numbers in a Given List

##n=int(input("Enter the number of elements to be inserted: "))
##a=[]
##for i in range(0,n):
##    elem=int(input("Enter element: "))
##    a.append(elem)
##avg=sum(a)/n
##print("Average of elements in the list",round(avg,2))

        #~~~~output
        ##Enter the number of elements to be inserted: 4
        ##Enter element: 2
        ##Enter element: 3
        ##Enter element: 4
        ##Enter element: 5
        ##Average of elements in the list 3.5

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Python Program to exchange the values of two numbers without using a temporary variable

##a=int(input("Enter value of first variable: "))
##b=int(input("Enter value of second variable: "))
##a=a+b
##b=a-b
##a=a-b
##print("a is:",a," b is:",b)

        #~~~~~ Output
        ##Enter value of first variable: 2
        ##Enter value of second variable: 5
        ##a is: 5  b is: 2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Python Program to reverse a given number.

##n=int(input("Enter number: "))
##rev=0
##while(n>0):
##    dig=n%10
##    rev=rev*10+dig
##    n=n//10
##print("Reverse of the number:",rev)

        #~~~~~Output
        ##Enter number: 123
        ##Reverse of the number: 321


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Python Program to check whether a given number is a palindrome

##n=int(input("Enter number:"))
##temp=n
##rev=0
##while(n>0):
##    dig=n%10
##    rev=rev*10+dig
##    n=n//10
##if(temp==rev):
##    print("The number is a palindrome!")
##else:
##    print("The number isn't a palindrome!")
##

        #~~~~Output
        ##Enter number:525
        ##The number is a palindrome!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Python Program to check if a date is valid

##date=input("Enter the date: ")
##dd,mm,yy=date.split('/')
##dd=int(dd)
##mm=int(mm)
##yy=int(yy)
##if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
##    max1=31
##elif(mm==4 or mm==6 or mm==9 or mm==11):
##    max1=30
##elif(yy%4==0 and yy%100!=0 or yy%400==0):
##    max1=29
##else:
##    max1=28
##if(mm<1 or mm>12):
##    print("Date is invalid.")
##elif(dd<1 or dd>max1):
##    print("Date is invalid.")
##elif(dd==max1 and mm!=12):
##    dd=1
##    mm=mm+1
##    print("The incremented date is: ",dd,mm,yy)
##elif(dd==31 and mm==12):
##    dd=1
##    mm=1
##    yy=yy+1
##    print("The incremented date is: ",dd,mm,yy)
##else:
##    dd=dd+1
##    print("The incremented date is: ",dd,mm,yy)

        #~~~~~Output
        ##Enter the date: 15/10/2019
        ##The incremented date is:  16 10 2019


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Calculate the Average of Numbers in a Given List

##year=int(input("Enter year to be checked:"))
##if(year%4==0 and year%100!=0 or year%400==0):
##    print("The year is a leap year!")
##else:
##    print("The year isn't a leap year!")

        #~~~~~Output
        ##Enter year to be checked:2019
        ##The year isn't a leap year!



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Program to generate all the divisors of an integer

##n=int(input("Enter an integer:"))
##print("The divisors of the number are:")
##for i in range(1,n+1):
##    if(n%i==0):
##        print(i)

        #~~~~~Output
        ##The divisors of the number are:
        ##1
        ##2
        ##4
        ##5
        ##10
        ##20

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# to print the largest even and largest odd number in a list

##n=int(input("Enter the number of elements to be in the list:"))
##b=[]
##for i in range(0,n):
##    a=int(input("Element: "))
##    b.append(a)
##c=[]
##d=[]
##for i in b:
##    if(i%2==0):
##        c.append(i)
##    else:
##        d.append(i)
##c.sort()
##d.sort()
##count1=0
##count2=0
##for k in c:
##    count1=count1+1
##for j in d:
##    count2=count2+1
##print("Largest even number:",c[count1-1])
##print("Largest odd number",d[count2-1])


#~~~~~ Output
##Enter the number of elements to be in the list:6
##Element: 2
##Element: 5
##Element: 3
##Element: 5
##Element: 1
##Element: 9
##Largest even number: 2
##Largest odd number 9


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

