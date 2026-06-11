import pandas as pd
import matplotlib.pyplot as plt

# Str 
# -> .value_counts 

# Int or float
# x= and y=

# Read file from csv
kpop_stats = pd.read_csv("Pandas/data/kpop idols.csv")



# Joining duplicate tables -> their seems to be duplicate columns 
kpop_stats.columns = [''.join(dict.fromkeys(col.split())) for col in kpop_stats.columns]
print(kpop_stats.columns.tolist())

print(kpop_stats)
print(kpop_stats.describe())
print(kpop_stats.head())
print(kpop_stats.dtypes)

# Plotting Graph 
kpop_stats['Birthplace'].value_counts().head(100).plot(kind='line', color='skyblue')
plt.xlabel("Birthplace by each kpop idol")
plt.title("Kpop Idols ")
plt.show()

kpop_stats['Country'].value_counts().head(10).plot(kind='bar', color='skyblue', autopct='%1.1f%%')
plt.xlabel("Country by each kpop idols")
plt.title("Kpop idols")
plt.show()

kpop_stats["Height"].plot()
kpop_stats.plot(x="StageName", y="Height")
kpop_stats.plot(x="StageName", y="Weight")
plt.show()

kpop_stats["Gender"].value_counts().head(1667).plot(kind='pie', color='skyblue')
plt.xlabel("Kpop idols")
plt.title('Kpop idols by gender')
plt.show()

kpop_stats["Instagram"].value_counts().head(1667).plot(kind='pie', color='skyblue')
plt.xlabel("Kpop idols")
plt.title('Kpop idols by Instagram')
plt.show()
