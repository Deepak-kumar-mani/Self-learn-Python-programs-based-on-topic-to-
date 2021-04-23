
#~~~~~~~~ Loops ~~~~~~~#

x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

        #~~~~Output
        ##['ab', 'cd']

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


##for x in range(3, 8, 2):
##    print(x)

        #~~~~Output
        ##3
        ##5
        ##7
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##for x in range(10):
##    # Check if x is even
##    if x % 2 == 0:
##        continue
##    print(x)

        #~~~~Output
        ##1
        ##3
        ##5
        ##7
        ##9

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##for i in range(1, 4):
##    if(i%5==0):
##        break
##    print(i)
##else:
##    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
    
        #~~~~Output
        ##1
        ##2
        ##3
        ##this is not printed because for loop is terminated because of break but not due to fail in condition


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##cnt=1 #this is the initial variable
##while cnt < 5 :
##        #inside of while loop
##        print (cnt),
##        print ("This is inside of while loop")
##        cnt+=1;
##else :
##        #this statement will be printed if cnt is equals to 5
##        print (cnt),
##        print("This is outside of while loop")
        
        #~~~~Output
        ##1
        ##This is inside of while loop
        ##2
        ##This is inside of while loop
        ##3
        ##This is inside of while loop
        ##4
        ##This is inside of while loop
        ##5
        ##This is outside of while loop



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##word="Python"
##pos=0 #initial position is zero
##while pos < len(word) :
##	print (word[pos])
##	#increment the position after printing the letter of that position
##	pos+=1
	
        #~~~~Output
        ##P
        ##y
        ##t
        ##h
        ##o
        ##n

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##var = 100
##while var == 100 :  # an infinite loop
##   data = input("Enter something:")
##   print ("You entered : ", data)
##
##print ("Good Bye Friend!")

        #~~~~Output
        ##Enter something:123
        ##You entered :  123
        ##Enter something:213
        ##You entered :  213
        ##Enter something:
        ##You entered :  
        ##Enter something:132
        ##You entered :  132
        ##Enter something:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

