import pandas as pd

print(f"pandas version: {pd.__version__}")

# 1.) Data types 

# Series only used when creating 1 dimensional table 
planets = pd.Series(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter ', 'Saturn', 'Uranus', 'Neptune'])
print(planets)

cars = pd.Series(['BMW', ''])
print(cars)

car_data = pd.DataFrame({"Car type ": cars,
                         "planets ": planets})

print(car_data)


# Exercise 
foods = pd.Series(['Sushi', 'KimBap', 'Korean BBQ', 'Ramen'])

price_point = (['$6.99', '$3.99', '$35.99', '$7.99'])

food_data = pd.DataFrame({"food ": foods,
                          "price point": price_point})

print(food_data)


# Scenario 
car_sales = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/car-sales.csv")
car_sales.to_csv("Pandas/data/car_sales.csv", index=False)
print(car_sales)
print(car_sales.dtypes)
print(car_sales.describe())

# Stats methods in df
# Mean
print(car_sales.mean(numeric_only=True))
car_prices = pd.Series([3000, 3500, 11250])
print(car_prices.mean())

# Sum
print(car_sales.sum(numeric_only=True))

print(car_sales.sum())

# Printing out columns and targets index 0
print(car_sales.columns)
car_columns = car_sales.columns
print(car_columns[0])

# Index
print(car_sales.index)

# Length
print(len(car_sales))

# # Exercise 
# # Reading the csv file
# heart_disease = pd.read_csv("Pandas/data/heart.csv")
# # Exporting
# heart_disease.to_csv("Pandas/data/heart_disease.csv")
# print(heart_disease)


# 5 Viewing and selecting data
# you can declare more rows by setting an integer
# to display more values
print(car_sales.head())
print(car_sales.head(7))

# bottom rows
print(car_sales.tail())



# .loc and .iloc select data from df n series just like how you would select in sql but in python
animals = pd.Series(['Cat', 'Dog', 'Bird'],
                    index=[0,1,3])

print(animals)
print(animals.loc[3])
print(animals.iloc[1])


print(car_sales)
print(car_sales.loc[3])
print(car_sales.loc[:3])


# Getting all rows based on the particular column
print(car_sales.loc[:, "Colour"])
print(car_sales['Make'])


# Boolean indexing
print(car_sales[car_sales["Odometer (KM)"] > 100000])

# Crosstab views two different columns and together compares them
result = pd.crosstab(car_sales["Make"], car_sales["Doors"])
print(result)

print(car_sales.groupby(["Make"]).mean(numeric_only=True))

# Manipulating data but changing the type using str replace
import matplotlib.pyplot as plt 

print(car_sales["Odometer (KM)"].plot());
print(car_sales.plot(x="Make", y="Odometer (KM)"))
plt.show()

print(car_sales["Odometer (KM)"].hist())
plt.show()


car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '', regex=True)
print(car_sales)

car_sales['Price'] = car_sales["Price"].str[:-2].astype(int)
print(car_sales)
print(car_sales.dtypes)

print(car_sales["Price"].plot())
plt.show()


# Manipulating data
# str.lower just makes the letters in lower case format
print(car_sales["Make"].str.lower())

#fillna function just fills in all the missing value information which may seem useful when theirs only little wholes
# of data



