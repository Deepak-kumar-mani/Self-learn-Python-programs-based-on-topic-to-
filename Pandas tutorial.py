import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import re

df = pd.read_csv(r'E:\Study material\Notes and working\Python office practics\pokemon_data.csv')
print(df.tail(3))

##df = pd.read_excel(r"C:\Users\DManiX092238\Downloads\pandas-master\pokemon_data.xlsx")
##print(df_xlsx.tail(3))

##df = pd.read_csv(r'C:\Users\DManiX092238\Downloads\pandas-master\pokemon_data.txt', delimiter = '\t')
#print(df.head(5))


##~~~~~~~~~~~~Reading data in pandas
##~~~~~~~ Read each column ~~~~~~~~~~##

#print(df.columns)
#df.columns
#print(df['Name'])
#print(df['Name'][0:5])                                     #~~~~~~~~first 5 names
#print(df[['Name','Type 1','HP']][0:5])                     #~~~~~~~~~~~to list more column we need to declare list of list



##~~~~~~~~~~~ Read each row ~~~~~~~~~~~~##

#print(df.head(4))                                          #~~~~~~~~ display data upto 4th row
#print(df.iloc[4])                                          #~~~~~~~~ disply only 4th row
#print(df.iloc[1:4])                                        #~~~~~~~~ display from 1st to 4th row
#print(df.loc[df['Type 1'] == "Grass"])                     #~~~~~~~~~~ it displays only which had Type 1 as Grass




##~~~~~~~~~~~ Read a specific location/position( Row'R'/Column'C') ~~~~~~~~~~##

#print(df.iloc[2,1])                                        #~~~~~~~~~~ it will search perticular position
##for index, row in df.iterrows():
##    print(index, row)                                     #~~~~~~~~~~ it will iterate index and row
##for index, row in df.iterrows():
##    print(index, row['Name'])                             #~~~~~~~~   it will iterates by index and Name
#print(df.describe())                                       #~~~~~~~~~~~~ it gives high level statics
#print(df.sort_values('Name'))                              #~~~~~~~~~~ sorts the name in alfabetical order
#print(df.sort_values('Name', ascending = False))           #~~~~~~~~ sort by deceiding order
#print(df.sort_values(['Type 1', 'Speed']))                 #~~~~~~~~~ if we have multiple column then open up in list
#print(df.sort_values(['Type 1', 'HP'], ascending = True))  #~~~~~~~~ it sorts by two column by ascending order
#print(df.sort_values(['Type 1', 'HP'], ascending = [1,0])) #~~~~~~~~~ it sorts by first ascending and next by decending by the character [1,0]


##~~~~~~~~~~~~ Making changes to data ~~~~~~~~~~ ##

#print(df.head(5))
#df['Total'] = df['HP']+df['Speed']+df['Defense']           #~~~~~~~~~ it will create new column as Total and add the HP, Speed, Defance and make an total
#print(df.head(5))



##~~~~~~~~~~~~ to drop and add an column ~~~~~~~~~~~~~~##

#df.drop(columns = ['Total'])                               #~~~~~~~~~ it delets the column named as Total and throws an error as Not found
#print(df.head(5))

#df['Total'] = df.iloc[:, 4:10].sum(axis =1)                #~~~~~~~~~ it will add from 4th column to 10th column
#print(df.head(5))



##~~~~~~~~~~~ To inter change the columns ~~~~~~~##

#df['Total'] = df.iloc[:, 4:10].sum(axis =1)                #~~~~~~~~~ it will add from 4th column to 10th column
cols = list(df.columns.values)
#df = df[['total','HP','Defense']]  #--- not working prperly
df =df[cols[0:1] + [cols[-1]]+cols[4:12]]                   #~~~~~~~~~ it rerranges the column
print(df.head(5))


##~~~~~~~~~~~ to save an update to new file ~~~~~~~~~~~~~~~##

#df.to_csv('modified.csv')                                   #~~~~~~~~~~~ it will save the file as modified to current directory
#df.to_csv('modified.csv', index = False)                    #~~~~~~~~~~~ it will remove the column with no column names
#df.to_excel('modified.xlsx', index = False)                 #~~~~~~~~~~~ it will save in excel formatt
#df.to_csv('modified.txt', index = False, sep ='\t')         #~~~~~~~~~~~ it will save in text formatt



##~~~~~~~~~~~ Fieltering Data ~~~~~~~~~~~~~~##

#print(df.loc[df['Type 1'] == 'Grass'])                                             #~~~~~~~~~ it will filter out only Grass in the type 1 column
#print(df.loc[(df['Type 1'] == 'Grass')&(df['Type 2'] == 'Poison')])                #~~~~~~ it will take two columns and two keywords and filter out
#print(df.loc[(df['Type 1'] == 'Grass')&(df['Type 2'] == 'Poison')&(df['HP']>70)])   #~~~~~~ passing different condition
#new_df = df.loc[(df['Type 1'] == 'Grass')&(df['Type 2'] == 'Poison')&(df['HP']>70)] #~~~~~~ assigining the condition to new identifier
#new_df.to_csv('filtered.csv', index =False)                                        #~~~~~~~~~~ saving this modified file
#new_df = new_df.reset_index()                               #~~~~~~~~~~~ it will reset the index from 1 and it will be in new column
#print(new_df)                                               #~~~~~~~~~~~ printing the reseted index
#new_df = new_df.reset_index(drop=True)                      #~~~~~~~~~~~ it will drop the old index 
#print(new_df)                                               #~~~~~~~~~~~ printing the new index
#new_df.reset_index(drop=True, inplace = True)               #~~~~~~~~~~~ its another way to drop and reset the index
#print(new_df)                         
#print(df.loc[df["Name"].str.contains('Mega')])              #~~~~~~~~~~~ it display the word only which includes Mega in the Name column
#print(df.loc[~df["Name"].str.contains('Mega')])             #~~~~~~~~~~~ it display the word only which does not have the name Mega in the Name column by including the symbol'~'
#print(df.loc[df["Type 1"].str.contains('Fire|Grass', regex = True)])    #~~~~~~ it will disply all the items contain Fire and Grass based on the column Type 1
#print(df.loc[df["Type 1"].str.contains('fire|grass',flags=re.I, regex = True)])    #~~~~~~ this is usd to avoid the case sensetive filter out
#print(df.loc[df["Name"].str.contains('pi[a-z]*',flags=re.I, regex = True)]) #~~~~~~~~ it will display the names which contains the character pi
#print(df.loc[df["Name"].str.contains('^pi[a-z]*',flags=re.I, regex = True)]) #~~~~~~~~ it will display only with the start of the word with character 'PI' by using the key work '^'


##~~~~~~~~~ Conditional changes ~~~~~~~~~~##

#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'         #~~~~~~~~ it will change the name from Fire to Flamer inside the column Type 1 
#print(df)                                                   #~~~~~~~~ it will print the changes
#df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = False        #~~~~~~~~ it will filter out flamerfrom Type 1 and change the Ligenday Fire to False
#print(df)
#df.loc[df['Total']>500,['Generation','Legandary']] = 'Test Value'   #~~~~~ if the total is greater than 500, it will change values in the colum Generation and LEgendary
#print(df)
#df.loc[df['Total']>500,['Generation','Legandary']] = ['Test1','Test2']  #~~~~~~ #~~~~~ if the total is greater than 500, it will change multipule values in Generation and Legendary column
#print(df)


##~~~~~~~~~~ Aggregate Statistis ~~~~~~~~~~##

#df = pd.read_csv('modified.csv')
#print(df.columns)
#print(df.groupby(['Type 1']).mean())                        #~~~~~~~~ it finds the mean value of each items in the column Type 1
#print(df.groupby(['Type 1']).mean().sort_values('Speed', ascending = False)) #~~~~~~~~~ it will sort the value of column speed 
#print(df.groupby(['Type 1']).sum())                         #~~~~~~~~ it finds the sum value of each items in the column Type 1
#print(df.groupby(['Type 1']).count())                         #~~~~~~~~ it finds the count value of each items in the column Type 1
#df['Count'] = 1                                             #~~~~~~~~~ it will add another column called count with value 1
#print(df)
#print(df.groupby(['Type 1']).count()['Count'])              #~~~~~~~~~ it will display only the number of counts and Type 1 column
#print(df.groupby(['Type 1', 'Type 2']).count()['Count'])              #~~~~~~~~~ it will display only the number of counts and Type 1 and Type 2 column



##~~~~~~~~~~~~ Working with large amounts of data ~~~~~~~~~##

#df = pd.read_csv('modified.csv', chunksize=10)              #~~~~~~~~~~ it means we are passing 5 rows at a time
##for df in pd.read_csv('modified.csv', chunksize=5):
##    print(df)
#print(df.read_csv('modified.csv', chunksize = 10)) 
