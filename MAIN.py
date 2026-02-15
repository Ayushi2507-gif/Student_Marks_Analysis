# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("AYU.csv")
print(data)

# Create bar chart
plt.figure(figsize=(8,5))   
plt.bar(data['Name'],data['Marks'])

# Add title and labels
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display graph
plt.show()
