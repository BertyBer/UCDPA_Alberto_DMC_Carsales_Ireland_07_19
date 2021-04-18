
#Initial coding

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

#importing packages
#importing database passenger cars databases 2007-2019

import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
import seaborn as sns
import numpy as np



df07 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2007.csv")
#print(df07.head(11))
#print(df07.tail(5))
#print(df07.shape)
#print(df07.columns)
#print(df07.dtypes)
#print(df07.loc[1:1000, "Year":"Engine type"])
#print(df7)

#checking columns and items and importing the rest of the datasets

df08 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2008.csv")
#print(df8)


df09 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2009.csv")
#print(df9)

df010 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2010.csv")
#print(df10)

df011 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2011.csv")
#print(df11)

df012 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2012.csv")
#print(df12)

df013 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2013.csv")
#print(df13)

df014 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2014.csv")
#print(df14)

df015 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2015.csv")
#print(df15)

df016 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2016.csv")
#print(df16)

df017 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2017.csv")
#print(df17)

df018 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2018.csv")
#print(df18)

df019 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2019.csv")
#print(df19)

df1 = pd.DataFrame(df07, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df2 = pd.DataFrame(df08, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df3 = pd.DataFrame(df09, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df4 = pd.DataFrame(df010, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df5 = pd.DataFrame(df011, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df6 = pd.DataFrame(df012, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df7 = pd.DataFrame(df013, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df8 = pd.DataFrame(df014, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df9 = pd.DataFrame(df015, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df10 = pd.DataFrame(df016, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df11 = pd.DataFrame(df017, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df12 = pd.DataFrame(df018, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])
df13 = pd.DataFrame(df019, columns = ["Year", "Month", "County", "Registration type", "Engine type", "Car registration count"])

# I have concatenated my 13 data sets into one and call it cars.

#df_row_reindex = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13], ignore_index=True)
#df_row_reindex = pd.concat([df1, df13], ignore_index=True)

#cars = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])
cars = df13
#print(cars.head())
#print(cars.tail())
print(cars.shape)
#print(cars[1:4])
#print(cars.iloc[6])
pd.set_option("display.max_rows", None, "display.max_columns", None)
#print(cars.head(20))

#Getting the NaN values and checking how many I have
#print(cars.isnull().sum())
#print(cars.info())


#I am going to drop the rows with a NaN value because I have a lot of Data
#print(cars.isnull().sum())
#to drop the rows with zero values.
cars_row = cars.dropna(axis = 0)
print(cars_row.shape)

#If I want to drop the columns, I would use:
#cars_col = cars.dropna(axis=1)

#I am now replacing the remaining NaN values with non declared instead of dropping the columns:
#print(cars.isnull().sum())
cars.fillna(value= "", inplace=True)
#print(cars.isnull().sum())

print(cars.columns)
#print(cars.shape)
#print(cars.info())

cars.columns = ["Year", "Month", "County", "Registration_Type", "Engine_Type", "Car_Reg_Count"]

#iterrows

#print(next(cars.iterrows())[1])

#for index, row in cars.head(n=10).iterrows():
     #print(index, row)

# iterate over rows with iterrows()

#for index, row in cars.head(20).iterrows():
     ################################################# access data using column names
     #print(index, row['Year'], row['County'], row['Registration_Type'])

#for row in cars.head(20).itertuples():
    #print(row.Year, row.County, row.Registration_Type)

#cars.sort_values("County")
#print(cars.head(10))

cars.sort_values("Engine_Type")
print(cars.head(10))


#Visualization
#I am using only the last year for this

print(pd.set_option("display.max_rows", None, "display.max_columns", None))
x = cars["Month"].head(10)
y1 = cars["Car_Reg_Count"].head(10)
#y2 = cars["Year"].head(10)

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="Reg_Count")
#plt.plot(x,y2,marker="*", linestyle="-.", color="b", label='PriceEuro')
plt.title("test1")
plt.xlabel("test2")
plt.ylabel("test3")
plt.legend()
plt.tight_layout()
plt.show()

#------------------------------------------#----------------

cars = pd.DataFrame(np.random.randn(1000, 2), columns=["Month", "Car_Reg_Count"])

cars["Month"] = cars["Car_Reg_Count"] + np.arange(1000)

cars.plot.hexbin(x="Month", y="Car_Reg_Count", gridsize=25)

plt.show()

#===============================================================

cars.to_numpy()
cars.describe()
cars.T
cars.sort_index(axis=1, ascending=False)
cars.sort_values(by="Car_Reg_Count")
print(cars(90))