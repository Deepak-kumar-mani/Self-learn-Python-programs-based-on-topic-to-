import numpy as np
import matplotlib.pyplot as plt


##L = [1,2,3,4,5,]            ## creating simple list of datas
##np_arr = np.array(L)        ## converting a list to array 
##print(np_arr)   
##print(type(np_arr))         ## O/P-<class 'numpy.ndarray'> ~~~nd array are basic object where all the array built on

##np.mat = np.mat('1 2;3 4; 5 6')  ## to create and matrix
##print(np.mat)                    ## created and matrix

##print(np.array(np.mat('1 2;3 4; 5 6'))) ## from numpy matrix to array



####~~~~~~~~~~~~~~ Type Casting ~~~~~~~~~~~~####

##a = np.array([1,2,3,4])         ## we should list of array
##a = np.array([1,2.0,3])         ## here we have given the data type as float
##print(a)                        ## all the data type converted to float highest data type is used float is highest preceidence

        ## type precedence ##
            ##bool
            ##int
            ##float
            ##string

##print(np.array([1,2,3],dtype=float))        ## it will convert all the datatypes to float
##print(np.array([1,2,3],dtype='U'))          ## it will convert all the datatypes to Unicode that is string
##print(np.array([12345,2,3],dtype='<U2'))    ## it will convert all the datatypes and crop up to 2 character '<'
##print(np.array([1,2,3],dtype=complex))      ## it will convert all the datatypes to complex

##x = np.array([('ram',26,100000.0),('shyam',31,32000)], dtype =[('name','<U10'),('age','int32'),('salary','<f4')])
##print('row 1',x[0])                         ## here we can specify the perticulare data type for each column
##print('row 1',x[1])




####~~~~~~~~~~~ Two Dimensional arry ~~~~~~~~~~~~~####


##two_arr = np.array([(1,2,3),(4,5,6),(7,8,9)])   ## creating two dimentional array (rows and column)
##print(two_arr)

##print('shape of 2-D array is ', two_arr.shape)              ## tells what type of array it is
##print('Number of dimensions 2-D array is ', two_arr.ndim)   ## it tells the number of dimension ~~~ 2
##print('Data type 2-D array is ', two_arr.dtype)             ## tells what type of datas are available
##print('Size of 2-D array is ', two_arr.size)                ## it tells how many datas are there in array





####~~~~~~~~~~~~ Three dimensional array ~~~~~~~~~~~~~~####


##three_arr = np.array([[[5.3,10.2,15.1],[20.3,11.2,6.1],[55.3,14.9,45.4]],[[5.3,10.2,15.1],[20.3,11.2,6.1],[55.3,14.9,45.4]]])
##print(three_arr)
##print('shape of 2-D array is ', three_arr.shape)              ## tells what type of array it is ((2, 3, 3)) ~~ two set of data, 3 rows and 3 column
##print('Number of dimensions 2-D array is ', three_arr.ndim)   ## it tells the number of dimension ~~ 3
##print('Data type 2-D array is ', three_arr.dtype)             ## tells what type of datas are available
##print('Size of 2-D array is ', three_arr.size)                ## it tells how many datas are there in array (2 * 3 * 3) = 18

##three_arr = np.array([[[1,2,3],[4,5,6]],[[5,6,7],[6,7,8]]])
##print(three_arr)
##print('shape of 2-D array is ', three_arr.shape)              ## tells what type of array it is ((2, 3, 3)) ~~ 2 set of data(3rd dimention length), 2 rows(2nd dimention length) and 3 column(1st dimention length)
##print('Number of dimensions 2-D array is ', three_arr.ndim)   ## it tells the number of dimension ~~ 3
##print('Data type 2-D array is ', three_arr.dtype)             ## tells what type of datas are available
##print('Size of 2-D array is ', three_arr.size)                ## it tells how many datas are there in array (2 * 2 * 3) = 12

##l=[[[5.3,10.2],[20.3,11.2],[55.3,14.9]],[[5.3,10.2],[20.3,11.2],[55.3,14.9]],[[5.3,10.2],[20.3,11.2],[55.3,14.9]],[[5.3,10.2],[20.3,11.2],[55.3,14.9]]]
##three_arr = np.array(l)
##print(three_arr)
##print('shape of 2-D array is ', three_arr.shape)              ## tells what type of array it is ((3, 3, 2)) ~~ four set of data, 3 rows and 2 column
##print('Number of dimensions 2-D array is ', three_arr.ndim)   ## it tells the number of dimension ~~ 3
##print('Data type 2-D array is ', three_arr.dtype)             ## tells what type of datas are available
##print('Size of 2-D array is ', three_arr.size)                ## it tells how many datas are there in array (3 * 3 * 2) = 18



####~~~~~~~~~~~~ NumPy import function~~~~~~~~~~~####


##print(np.zeros((3,4)))                                        ##  it ceated an array of 3 rows and 4 columns and fills the data with zeros
##print(np.ones((2,3,4)))                                       ##  it creates an arry of 2 sets of data, 3 rows an 4 column and fills the date with ones
##print(np.empty((2,3)))                                        ##  it dosent initialize anything it randomely fills the date whatever available in the memory
##print(np.eye((4)))                                            ## its a square matrix and the diagonal will be one

##arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
##print('array is ')
##print(arr)
##print('dagonal of above array is: ',np.diag(arr))             ## this commend is used to print the diagonal of the array listed above
                                                                  #here you can give even 2rows and 3columns any kind it will accept

##print(list(range(20)))                                        ## here it will print till the given rage
##print(np.arange(10,30,5))                                     ## here we have give start value, end value and the step, it will follow the slicing method
##print(np.arange(1,100,2.5))


#print(np.linspace(1,100,5))                                    ## here it will create list of no with equal space including the start value and end value with  equal steps as given
#print(np.linspace(0,2,9))
##x = np.linspace(0,2*np.pi, 100)                               ## it created 100 different values frm 0 to 2*pi
##print(x)                                                      
##f = np.sin(x)                                                 ## here each value stored in sin of x and the sin wave ploted
##plt.plot(f)                                                   ## here it will create an sin wave graph with 100 different points from 0 to 10
##plt.show()


        ## np.tril --> triangular of lower matrix

##arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(arr)
##print('--------')
##print(np.tril(arr))                                           ## here it prints only the lower set of data in array list

##arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(arr)
##print('--------')
##print(np.tril(arr, -1))                                       ## here it removes the diagonal also


        ## np.triu --> triangular of upper matrix

##arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(arr)
##print('--------')                   
##print(np.triu(arr))                                           ## here it prints only the upper set of data in array list

##arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(arr)
##print('--------')                   
##print(np.triu(arr,1))                                         ## here it removes the diagonal also




####~~~~~~~~~~~~ Printing Array ~~~~~~~~~~~~####

##a = np.arange(9)
##print(a)                                                      ## here it will will print the no up to the rage 9

##print(np.arange(12).reshape(2,2,3))                           ## here we have given the range as 12 this is the size of an array and we have given the sape as 2 set of data with 2 rows and 3 columns
                                                                   #while giving the range and reshare we should ensure the range is equeal if we multiple the reshape array size

##print(np.arange(1000))                                        ## a range dosent work on string it returns in numeric values
##s = np.array(['a','b','c','d'])
##print(s.reshape(2,2))                                         ## here it prints the sting in 2 by 2 matrix



####~~~~~~~~~~~ Random number generation ~~~~~~~~~~####


##print('Random number generation (from uniform distribution)')
##print(np.random.rand(2,3))                                    ## here it generates random number in 2 by 3 matrix and its uniform distribution from 0 to 1

##print('Number from normal distributon with zero mean an standard deviation 1 iex., standard normal')
##print(np.random.randn(4,3))                                   ## here its an non uniform distriution by adding 'n' to the rand

##print('Number from normal distributon with zero mean an standard deviation 1 iex., standard normal')
##print(np.random.randn(10))                                    ## here its an non uniform distriution and prints value from 0 and 1

##plt.plot(np.random.rand(100))                                 ## here it will plot a rand value from 0 to 1 with 100 intervals
##plt.show()
                                            
##plt.hist(np.random.randn(10))                                 ## here it will plot a rand value from 0 to 1 with 100 intervals
##plt.show()                                                    ## here it will print the normal distribution

##plt.hist(np.random.randn(1000))          ## here we are taking more values it will show as bell curve
##plt.show()

##arr = np.random.randn(4,3)
##print(arr.std())

##print('Random integer vector:',np.random.randint(1,100,10))   ## here it will thow 10 randam samples from 1 to 100
##print('\n Random integer matrix')

##print(np.random.randint(1,100,(4,4)))                         ## here it will create an integer value from 1 to 100 with 4 by 4 matrix
##print('\n20 samples drawn from a dice throw:',np.random.randint(1,7,20)) ## here it takes 20 samples from 1 to 6



####~~~~~~~~~~~~~ Basic operations ~~~~~~~~~~~~####

##a = np.array([20,30,40,50])
##b = np.arange(1,5)
##print(a)                                                       ## here a s haveing 4 values
##print(b)                                                       ## here b will have 4 values from 1 to 4

    ##~~~~ Elementwise arithmatic operations ~~~~##

##add = a+b
##sub = a-b
##div = a/b
##mul = a*b                                                      ## here it will do element to elementwise arithmatic operations
##print('addition',add)
##print('Substraction',sub)
##print('Division',div)
##print('multiplication',mul)

    ##~~~~~ Arithmatic operations with scalar values ~~~~~##

##print(b**2)                                                    ## here we are squreing the b values
##print(b * 10)                                                  ## here we are multipuling the b values
##print(a < 35)                                                  ## here we are doing boolian values (true/false)


    ##~~~~ Matrix operations ~~~~~##
##a = np.array([[1,1],[0,1]])
##b = np.array(np.arange(4).reshape(2,2))
##print(a)
##print('~~~~~~~')
##print(b)

##add = a + b
##sub = a - b
##print('\n',add)
##print('~~~~~~')
##print(sub)


    ##~~~~ Matrix multiplication ~~~~##
##a = np.array([[2,3],[1,4]])
##b= np.array([[6,4],[7,5]])
##print(a)
##print('\n',b)
##c = a*b                                                       ## this is normal multiplication 
##print('\n',c)
##print(a.dot(b))                                               ## this is how matrix multiplication works here as such like column of the first array multiplies rows of the second array rows and column should be equal
                                                                 ## 2x6+3X7 , 2X4+3X5
                                                                 ## 1X6+4X7 , 1X4+4X5

##c = np.array(np.arange(10,16))                                ## here it generats nomber from 10 to 16
##print(c)
##print(c.reshape(3,2))                                         ## here it converts and reshape the list of array into 3 by 2 matrix

        ##~~~~~~~~ or~~~~~~~ ##


##e = np.array((np.random.randint(1,100,6)).reshape(2,3))       ## here it will generate 6 random no from 1 to 100 and reshape into 2row by 3column matrix
##print(e)


        ##~~~~~~~~ or~~~~~~~ ##

##c = np.array((np.arange(10,16)).reshape(3,2))
##print(c)
##d = np.array((np.arange(8,12)).reshape(2,2))
##print('~~~~~~~~~\n',d)
##print('~~~~~~~~~~~~~~\n',c.dot(d))                            ## here clculation works as the no of rows in c array is equeal to no of column in d array 


##c = np.array((np.arange(10,16)).reshape(3,2))
##print(c)
##d = np.array((np.random.randint(1,100,9)).reshape(3,3))
##print(d)
##print(c.dot(d))                                               ## here the dimention is not equal and it wont work



####~~~~~~~ Universal methods ~~~~~~~####

    ## argmax, argmin, argsort, average, ceil, corrcoef, cov,
    ## cross, cumprod, cumsum, diff, dot, floor, inner, inv,
    ## max, maximum, mean, median, min, minimum, nonzero,outer,
    ## prod, re, round, sort, std, sum, trace, transpose, var,
    ## vdot, vectorize, where


##a =np.arange(12).reshape(3,4)
##print(a)

##print('sum of elements ',a.sum())                             ## here it prints the sum of an array
##print('min of elements ',a.min())                             ## here it prints the min value of an array
##print('max of elements ',a.max())                             ## here it prints the max value of an array
##print('std of elements ',a.std())                             ## here it prints the stndard divation of an array
##print('mean of elements ',a.mean())                           ## here it prints the mean of an array
##print(a.shape)                                                ## here it tells what type of matrix is (3,4)

        ## if the Axis=0 workes in column wise
##print(a.sum(axis=0))                                          ## here it sums only the 0th column
##print(a.sum(axis=1))                                          ## here it sums only the 1st column

        ## if axis=1 works in row wise
##print(a.min(axis=0))                                          ## here it prints the minimum vlaue in each row
##print(a.cumsum(axis=1))                                       ## here it cumulate the sum of previous index

##print(np.exp(a))                                              ## here it prints the exponential form
##print(np.sqrt(a))                                             ## here it prints the queare root of

##b = np.random.rand(4,3)
##print(b)
##print(np.argmax(b))
##print(np.max(b))



####~~~~~~~~~~ Indexing, Slicing and iterating ~~~~~~~~~~~####

##a = np.linspace(1,10,15)                    ## here we are creating 15 equeal points from 1 to 10
##print(a)                                    ## here it will print it as an list of array
##print('------------------------')
##print(a[2])                                 ## here it will print the 2nd index value
##print('------------------------')
##print(a[2:5])                               ## here it will print from 2nd index to 5th index
##print('------------------------')
##print(a[::-])                               ## here it will print from reverse direction


####~~~~~~~~~~~~ Multidimensional arrays ~~~~~~~~~~ ####

##A = np.arange(20).reshape(5,4)              ## here it will create and list of array in the shape of 5 rows and 4 column with the given range 20
##print(A)
##print(A.shape)                              ## it will tell the shape of the matrix
##print(A[2:4, 1:3])                          ## here it will print the from 2 row to 3rd row 4th row will be skipped
                                               # and 1st column and 2nd column will be print 3rd column will be skipped
##print(A[0:3, 1])                            ## here it prints the 0th, 1st, 2nd row and 1st column
##print(A[:, 1])                              ## to print perticular the column her it prints the 1st column
##print(A[1:3, :])                            ## here iw will print the 1st, 2nd rows 
##print(A[-1])                                ## here it prints the last row
##print(A[3],'\n~~~~~~~~~')                   ## here it prints the 3rd row
##print(A[3, :],'\n~~~~~~~~~')                ## here it prints the 3rd row
##print(A[3, ...],'\n~~~~~~~~~')              ## here it prints the 3rd row

##b =np.arange(45).reshape(3,3,5)             ## it creates and multi dimention array 
##print(b)
##print(b[1, 1:3, 1:3])                       ## here it will print the 1set of array with 1st nad 2nd rows and 1st and 2nd column

####~~~~~~~~~~ Iteration or for loop~~~~~~~~#####
b =np.arange(45).reshape(3,3,5)
##for i in range(3):
##    print('department',i)                  ## here it will itrates through multidimensional array
##    for j in range(3):
##        print('\t Employee ',j)
##        print(b[i,j])

##print(b.flat)                               ## here it itrates into each single element
##print(b.ravel())                            ## it just simply returns an list of element

##b =np.arange(45).reshape(3,3,5)
##print(b.T)                                  ## here 'T' indicates to inter change the rows and column


####~~~~~~~~~To open an file using numpy~~~~~~~~~~~~~###

##import numpy as no
##var = np.genformtxt('filename', delimiter = ',', usecols=np.arange(2,7),ship_header = True)



####~~~~~~~~ manuplating multiple arrays into single operations~~~~~~~~~~~~~####

##a= np.floor(10*np.random.random((2,2)))
##print(a)
##print('~~~~~~~~~~~~~')
##b= np.floor(10*np.random.random((2,2)))
##print(b)
##print('~~~~~~~~~~~~~')
##print(np.vstack((a,b)))
##print('~~~~~~~~~~~~~')
##print(np.hstack((a,b)))
##print('~~~~~~~~~~~~~')
##print(np.concatenate((a,b), axis =0))
##print('~~~~~~~~~~~~~')
##print(np.concatenate((a,b), axis =1))
##print('~~~~~~~~~~~~~')
##print(np.column_stack((a,b)))
##print('~~~~~~~~~~~~~')
##print(np.row_stack((a,b)))
##print('~~~~~~~~~~~~~')


####~~~~~~~~~~~~ Broadcastin ~~~~~~~~~~~~~####

"""two different element can be add if the pattern matchs, if pattern dosent match we can traverse the
list and use it to add the different elements"""


####~~~~~~~~~~~~ Split ~~~~~~~~~~~~~~~~~~####

""" and also we can do splitting"""
##a= np.floor(10*np.random.random((4,12)))        ## here it rendomly prints 4 rows and 12 columns of data
##print(a)
##print('~~~~~~~~~~~~~~~~~~~~')
##print(np.hsplit(a,3))                           ## here the array splitted in he horizontal direction
##print('~~~~~~~~~~~~~~~~~~~~')
"""here it will work only on equal division of columns to over come this
we can specify the split levels"""

##print(np.hsplit(a,(3,8,9)))                           ## here the array splitted as first 3 colum and next array set us from 4th column to 8th column
##print('~~~~~~~~~~~~~~~~~~~')                            # and then 9th column as one set of array and balance is last set of array
##print(np.vsplit(a,2))                           ## here the array splitted in he horizontal direction
##print('~~~~~~~~~~~~~~~~~~~~')


####~~~~~~~~~~~~~~~ Copy and view ~~~~~~~~~~~####

##a = np.arange(12)                           ## createing list of 12 numbers
##b=a                                         ## assigning a to b
##print(a)                                    ## printing a
##print(b is a)                               ## checking whether a and b are same
##b.shape = 3,4                               ## reshaping the b
##print(b)                                    ## printing b
##print(a.shape)                              ## checking a shape as a and b are same whether b shape reflects in a


####~~~~~~~~~~~~~ View or shallow copy ~~~~~~~~~~~~####

##c = a.view()                                ## it creates an metadata using view function and moving it to c
##print(c is a)                               ## will check if a is equal to c
##print(c.base is a)                          ## will check if the base of c is equeal to a
##c.shape = 2,6                               ## reshaping the c
##print(a)                                    ## here it prints the value of a after reshaping b
##print(a.shape)                              ## Checking the shape of a
##c[1,1] = 100                                ## here we are changing the value of 1st row - 1st column
##print(c)                                    ## printing the value of c the above changes reflects in the array
##c[0,1] = 10                                 ## here we are changing the value of 0th row - 2st column
##print(a)                                    ## here it will rflects th changed value of c 
##d = a.copy()
##print(d)


####~~~~~~~~~~~~~~~ Advance/re indexing ~~~~~~~~~~~~~~~####

##a = np.arange(12)**2                        ## it will create 0 to 11 square
##print(a)
##i =np.array([1,1,3,8,5])                    ## it will store the list of arra to  'i'
##print(a[i])                                 ## here it takes the i value in side a and make it as square
##j = np.array([[3,4],[9,7]])                 ## here it will create an multidimensional array
##print(j)
##print(a[j])                                 ## her the j value moved inside a and make it as square


####~~~~~~~~~~~~~~ Multidimensional array ~~~~~~~~~~~~~####

##palette = np.array([[0,0,0],
##                    [255,0,0],
##                    [0,255,0],
##                    [0,0,255],
##                    [255,255,255]]
##                   )                        ## here we have declared an multi dimentional array
##image = np.array([[0,1,2,0],
##                  [0,3,4,0]]
##                 )                          ## here we have declared an multi dimentional array
##print(palette[image])                       ## here i'm useing the image array into palette, first it will print 0th row of palette and then 1st and then 2nd and then last in the first set of array
                                                # and in the second set of array it will print 0th row, 3rd row, 4th row and 0th row


##a = np.arange(12).reshape(3,4)
##print(a)
##i = np.array([[0,1],
##              [1,2]]
##             )
##j = np.array([[2,1],
##              [3,3]]
##             )
##print(a[i,j])                               ## now i&j become the values of a as like [[i0&j2],[i1&j1]] &[[i1&j3],[i2&j3]] and it search the rows and column
                                                # here i is pointing to the first dimension of the index an j is for 2nd dimension index

##a = np.arange(5)
##print(a)
##a[[1,3,4]] = 0                              ## here for the indes 1,3,4 we are assgning the value as 0
##print(a) 


####~~~~~~~~~~~~ Indesing with boolean array ~~~~~~~~~~~~~~~~####
                                                

##a = np.arange(12).reshape(3,4)
##print(a)
##b = a>4                                     ## here we are using the boolean operation it will return as true or false
##print(b)
##print(a[b])
##   #OR#
##print(a[a>4])

####~~~~~~~~~~~ Multidimensional boolean indexing ~~~~~~~~~~~~~~~####

##a = np.arange(12).reshape(3,4)
##print(a)
##b1=np.array([False, True, True])            ## here its representing the rows
##b2=np.array([True, False, True, False])     ## here it representing the column
##print(a[b1,:])                              ## here it will print the rows
##print(a[:, b2])                             ## here it will print the column
##print([b1,b2])                              ## here it prints the intersection that is common element of b1 and b2
