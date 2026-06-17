import pandas as pd 
import matplotlib.pyplot as plt 

health_diet = pd.read_csv("Pandas/data/healthy_diet_calorie_intake.csv")
print(health_diet)
print(health_diet.dtypes)
print(health_diet.describe)


# How to set a str vaLue given from the csv file to make a simple plot graph depending on what you want on it 
health_diet['Diet_Type'].value_counts().head(10).plot(kind='pie', color='skyblue')
plt.xlabel("Diet type")
plt.ylabel('Different types of diet each person intakes')
plt.title('Healthy Person Diagram based of Diet')
plt.show()

# How to set a float or int value for a simple graph
health_diet['BMI'].plot()
plt.xlabel('Body mass')
plt.ylabel('Weight')
plt.title('Healthy Person BMI Record')
plt.show()