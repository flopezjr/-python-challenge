import os
import csv

# OUT_PATH = "budget_data_clean.csv"

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as in_file:

    csv_reader = csv.reader(in_file)
    
    num_rows = 0
    total = 0
    
    for e ,row in enumerate(csv_reader):
        if e == 0:
            False
        else:
            num_rows += 1
            total += int(row[1])
     
        print(type(row))        
print(num_rows)
print(total)
print(type(csv_reader))

# Final Print out

print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {num_rows}')
print(f'Total: ${total}')
print(f'Average Change: {___}')
print(f'Greatest Increase in Profits: {_Month_} {___}')
print(f'Greatest Decrease in Profits: {_Month_} {___}') 
