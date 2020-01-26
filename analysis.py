import pandas as pd
import os

df = pd.read_csv("patients.txt")

print(">>Averages\n")
avAge = df['age'].mean()
avHeight = df['height'].mean()
avWeight = df['weight'].mean()

print("The average age is: " + str(avAge))
print("The average height is: " + str(avHeight))
print("The average weight is: " + str(avWeight) + "\n")

print(">>BMIs\n")
df['BMI'] = (df.weight / df.height**2) * 10000
print(df[['name','BMI']].sort_values('BMI', ascending=False))

print("\n>>Adult patients who are overweight\n")
overweight = df['BMI'] >= 25
adult = df['age'] >= 18
print(df[overweight & adult].sort_values('BMI', ascending=False))

os.system("pause")
