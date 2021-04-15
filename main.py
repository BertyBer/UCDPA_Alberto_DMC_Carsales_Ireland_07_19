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

df07 = pd.read_csv(r"C:\Users\Alberto\Desktop\Data Analytics\passenger cars 2007.csv")
#print(df07.head(11))
#print(df07.tail(5))
#print(df07.shape)
#print(df07.columns)
#print(df07.dtypes)
#print(df07.loc[1:1000, "Year":"Engine type"])
#print(df7)

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

df_row = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])
#df_row = pd.concat([df1, df13])

# I have concatenated my 13 data sets into one but now the row labels are wrong so I need to adjust them.

#df_row_reindex = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13], ignore_index=True)
#df_row_reindex = pd.concat([df1, df13], ignore_index=True)

cars = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13])

#print(cars)
#print(df_row.tail(10))
#print(df_row.shape)
#print(cars.tail(60))
#print (cars[1:4])
#print(cars.iloc[6])
pd.set_option("display.max_rows", None, "display.max_columns", None)

#print(cars.head())

#print(cars.shape)
#print(cars.isnull().sum())
#print(cars.info())

#print(cars.fillna(value=0))


print(cars.columns)

#print(cars.shape)

print(cars.info())

#print(cars["Year"].head(50))

#print(cars.head(2))
#print(cars.isnull())



print(cars.shape)


#print(cars.isnull().sum())
cars_row = cars.dropna(axis = 0)
print(cars_row.shape)
# I am not dropping any columns with the next code because i will be left with no columns, so I am going to replace the values with zero instead.
#cars_col = cars.dropna(axis=1)
#print(cars_col.shape)

zero_fill_data = cars.fillna(0)
print(zero_fill_data.isnull().sum())

#print(cars_col.shape)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#x = cars["Month"].head(500)
#y1 = cars["Year"].head(500)
#y2 = cars["Engine type"].head(500)
#y3 = cars["Car registration count"].head(500)
#y4 = cars["Year"].head(500)

#plt.plot(x,y1, marker="o", linestyle="--", color="g", label="per county")
#plt.plot(x,y2, marker="*", linestyle="-.", color="b", label="Engine type")
#plt.plot(x,y3, marker="+", linestyle=":", color="r", label="Engine type")
#plt.plot(x,y4, marker=".", linestyle="solid", color="y", label="Engine type")

#plt.title("Engine Type by County")
#plt.xlabel("County")
#plt.ylabel("Engine and Car count")
#plt.legend()
#plt.tight_layout()
#plt.show()


