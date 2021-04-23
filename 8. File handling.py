
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Program to read the contents of a file

##a=str(input("Enter the name of the file with .txt extension:"))
##file2=open(a,'r')
##line=file2.readline()
##while(line!=""):
##    print(line)
##    line=file2.readline()
##file2.close()

        #~~~~~Output
        ##Hi and hello
        ##This programming language is
        ##Python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Program to count the number of words in a text file

##fname = input("Enter file name: ")
##num_words = 0
 
##with open(fname, 'r') as f:
##    for line in f:
##        words = line.split()
##        num_words += len(words)
##print("Number of words:")
##print(num_words)

        #~~~~Output
        ##Enter file name: deepak.txt
        ##Number of words:
        ##8


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Program to count the number of lines in a text file

##fname = input("Enter file name: ")
##num_lines = 0

##with open(fname, 'r') as f:
##    for line in f:
##        num_lines += 1
##print("Number of lines:")
##print(num_lines)

        #~~~~Output
        ##Enter file name: deepak.txt
        ##Number of lines:
        ##3


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Program to count the frequency of words appearing

##test_string=input("Enter string:")
##l=[]
##l=test_string.split()
##wordfreq=[l.count(p) for p in l]
##print(dict(zip(l,wordfreq)))

#~~~~Output
##Enter string:orange banana apple apple orange pineapple
##{'orange': 2, 'banana': 1, 'apple': 2, 'pineapple': 1}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program to Read a String from the User and Append it into a File

##fname = input("Enter file name: ")
##file3=open(fname,"a")
##c=input("Enter string to append: \n");
##file3.write("\n")
##file3.write(c)
##file3.close()
##print("Contents of appended file:");
##file4=open(fname,'r')
##line1=file4.readline()
##while(line1!=""):
##    print(line1)
##    line1=file4.readline()    
##file4.close()

        #~~~~Output
        ##Enter file name: deepak.txt
        ##Enter string to append: 
        ##Program to Read a String from the User and Append it into a File
        ##Contents of appended file:
        ##Hi and hello
        ##This programming language is
        ##Python.
        ##Program to Read a String from the User and Append it into a File

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program to Copy the Contents of One File into Another

##with open("test.txt") as f:
##    with open("out.txt", "w") as f1:
##        for line in f:
##            f1.write(line)

        #~~~~Output
        #new output file is created in the same directory 


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program that Reads a Text File and Counts the Number of Times a Certain Letter Appears

##fname = input("Enter file name: ")
##l=input("Enter letter to be searched:")
##k = 0
 
##with open(fname, 'r') as f:
##    for line in f:
##        words = line.split()
##        for i in words:
##            for letter in i:
##                if(letter==l):
##                    k=k+1
##print("Occurrences of the letter:")
##print(k)


        #~~~~Output
        ##Enter file name: deepak.txt
        ##Enter letter to be searched:i
        ##Occurrences of the letter:
        ##8


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Python Program to Count the Number of Blank Spaces

fname = input("Enter file name: ")
k = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isspace):
                    k=k+1
print("Occurrences of blank spaces:")
print(k)


#~~~~Output



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~Output




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~Output







