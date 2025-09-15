# Pandas = Python library for data analysis and data manupulation.
# It provides two main structures:
# -Series → 1D labeled array (like a column).
# -DataFrame → 2D labeled table (like an Excel sheet).

import pandas as pd #importing the library

print("\n----------------------------INTRODUCTION TO PANDAS----------------------------")

#can also define indexes, otherwise will be 0,1,2...
series=pd.Series([44,52,17,62,82], index=['Programming','Database','Data Structures','Automata','Applied Physics'])
print("\nSeries:\n",series) 

df=pd.DataFrame({
    "Names":["Khalid","Ali","Usman"], 
    "Marks":[87,75,57]},
    index=[1,2,3])
print("\nDataFrame:\n",df)

df=pd.read_csv("C:\\Users\\Studywise\\Desktop\\Khalid Brainium\\Python-ML Practice\\iris.csv")
print("\n",df.head()) #top 5 values
print("\n",df.tail()) #last 5 values
print("\n",df.describe()) #will give info like count, mean, std, min, max, 20%, 50%, 75%
print("\n",df.info()) #will give info like datatype, Non Null Values

print("\n-------------DATA SELECTION-------------")
print("\nVariety\n",df["variety"])
print("\nSepal Length - Variety\n",df[["sepal.length","variety"]]) #print specific columns


print("\nIterating Rows:\n",df.iloc[-1]) #iloc=index location, print row index wise

df2=pd.read_csv("C:\\Users\\Studywise\\Desktop\\Khalid Brainium\\Python-ML Practice\\data.csv")
print("\nDataFrame 2 Head\n",df2.head())
print("\n",df2.dropna().head()) #will drop rows containing null
print("\n",df2.fillna('-').head()) #will replace the null values with specific values

#rename columns
print("\nRenaming:\n",df.rename(columns={"sepal.length":"Sepel Length","sepal.width":"Sepel Width","petal.length":"petal Length","petal.width":"Petal Width"}).head())

print("\nChanging Data type:\n",df['sepal.length']==df['sepal.length'].astype(int))#changing data types

print("\nLength of DataFrame: ",len(df)) #print length
# df["Zeros"] = [0 for i in range(len(df))]  # creates a list of zeros
df["New Column"]="Pending Value" #create new column and add values
print("Dataframe:\n",df)
def fx(a):
    return a*a
df["SL Square"]=df["sepal.length"].apply(fx) #create a new column and pass values from the function
print("Dataframe:\n",df)

df["SL + 5"]=df["sepal.length"] +5 # create new column by manupulating any previous one
print("Dataframe:\n",df)

df.to_csv("C:\\Users\\Studywise\\Desktop\\Khalid Brainium\\Python-ML Practice\\export.csv", index=False) #save csv, index=false will not store indexes

df=pd.DataFrame({
    "Name:":["Khalid","Ali","Hassan","Saim"],
    "Roll No:":[4324,5241,7352,5433]},
    index=[1,2,3,4])
df1=pd.DataFrame({
    "Name:":["Aasim","Usman","Shabbir"],
    "Roll No:":[3242,6352,8554]},
    index=[1,2,3])
df2=pd.DataFrame({
    "Name:":["Khalid","Ali","Ahmed"],
    "Marks:":[94,53,65]},
    index=[1,2,3])

df3=pd.DataFrame({
    "Name:":["Khalid","Ali","Ahmed"],
    "DOB:":['14 Oct 2001','22 Feb 2003','19 Mar 2002']},
    index=[1,2,3])
print("\nConcatinating Rows:\n",pd.concat([df,df1])) #concatinating different dataframes (Row wise)

print("\nConcatinating Columns:\n",pd.concat([df,df2], axis=1)) #concatinating different dataframes (Column Wise)

print("\nMerging:\n",pd.merge(df,df2, on="Name:")) #will merge  dataframes on matcing rows

print("\nSorting:\n",df2.sort_values(by="Marks:", ascending=False)) #will sort data, ascending=False will display in descending

print("\nDroping Column:\n",df2.drop(["Name:", "Marks:"], axis=1)) #to drop columns

df3["DOB:"] = pd.to_datetime(df3["DOB:"], format="%d %b %Y") #extracting Date

print("\nExtracting Year:\n", df3["DOB:"].dt.month)
