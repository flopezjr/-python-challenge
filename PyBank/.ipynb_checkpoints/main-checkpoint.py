import csv
import os

path = os.path.join("Resources", "budget_data.csv")

with open(path, "w+") as file:
    list_of_strings = [str(e) for e in row]
    
print(list_of_strings)