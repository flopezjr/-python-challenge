import os
import csv

TEXT_FILE = os.path.join("Analysis", "PyBank.txt")

path = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
changes = []



with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
        
    for row in (csv_reader):
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
        total_months = len(list(months))
        pl_total = sum(profit_loss)
            
#Calculate variance between months  
#     last_period_row = variance[i-1]
#     current_period_row = variance[i]
with open(path, "r") as file:
    csv_reader = csv.reader(file)

    for i in range(1, len(profit_loss)):
        changes.append((int(profit_loss[i])- int(profit_loss[i-1])))
    
        avg_changes = round(sum(changes)/ len(changes), 2)
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
    

# Final Print out

print("Financial Analysis")
print("-" * 25)
print(f'Total Months: {total_months}')
print(f'Total: ${pl_total}')
print(f'Average Change: ${avg_changes}')
print(f'Greatest Increase in Profits: {months[25]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {months[44]} (${greatest_decrease})') 

#.txt file
with open (TEXT_FILE, "w+") as file:
    file.write("Financial Analysis\n")
    file.write('-' * 25)
    file.write(f'\nTotal Months: {total_months}\n')
    file.write(f'Total: ${pl_total}\n')
    file.write(f'Average Change: ${avg_changes}\n')
    file.write(f'Greatest Increase in Profits: {months[25]} (${greatest_increase})\n')
    file.write(f'Greatest Decrease in Profits: {months[44]} (${greatest_decrease})') 