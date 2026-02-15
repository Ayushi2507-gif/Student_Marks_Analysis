import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("AYU.csv")
print(data)
plt.figure(figsize=(8,5))   
plt.bar(data['Name'],data['Marks'])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
