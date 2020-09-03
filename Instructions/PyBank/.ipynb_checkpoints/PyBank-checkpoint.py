import os
import csv


path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as in_file:

    csv_reader = csv.reader(in_file)
    
    num_rows = 0
    total = 0
    changes = []
    
    for e ,row in enumerate(csv_reader):
        if e == 0:
            False
        else:
            num_rows += 1
            total += int(row[1])
        
        variance.append(int(row[1]))
        
            
 #Calculate variance between months           
for i in range(1, len(variance)):
    changes.append((int(variance[i])- int(variance[i-1])))
    
    
    last_period_row = variance[i-1]
    current_period_row = variance[i]
    
    change = ???
    changes.append(change)

average_change = ???
greatest_change = ???

print(num_rows)
print(total)
print(variance)
print(changes)

# Final Print out

print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {num_rows}')
print(f'Total: ${total}')
print(f'Average Change: {___}')
print(f'Greatest Increase in Profits: {_Month_} {___}')
print(f'Greatest Decrease in Profits: {_Month_} {___}') 
