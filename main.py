# spam = 40
# spam
# print (spam)

# print ("alice"+ "bob")
# print(len("Alice"))

#print("hello what is your name")
#myName = input()
#print("Really good to see you here, " + myName)
#print("Fun fact, the length of your name is:")
#print(len(myName))
#print("what is your age?")
#myAge = input()
#print ("Do you know you will be " + str(int(myAge)+6)+ " in six years time?")
#print("I know, mind blowing!! " + myName)
#print("OK, enough talking, let's do this")

#export data frames

import pandas as pd

df7 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2007.csv")
print(df7.head(11))
print(df7.tail(5))
print(df7.shape)
print(df7.columns)
print(df7.dtypes)
print(df7.loc[1:1000, "Year":"Engine type"])
#print(df7)

df8 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2008.csv")
#print(df8)
df1 = pd.DataFrame({df7: df8})
print(df1)
df9 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2009.csv")
#print(df9)

df10 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2010.csv")
#print(df10)

df11 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2011.csv")
#print(df11)

df12 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2012.csv")
#print(df12)

df13 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2013.csv")
#print(df13)

df14 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2014.csv")
#print(df14)

df15 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2015.csv")
#print(df15)

df16 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2016.csv")
#print(df16)

df17 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2017.csv")
#print(df17)

df18 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2018.csv")
#print(df18)

df19 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2019.csv")
#print(df19)

