import os
import csv


path = os.path.join("Resouces", "election_data.csv")

with open(path, "r") as in_file
    
    csv_reader = csv.DictReader(in_file)
    
    for row in csv_reader:
        
        
# Final Print out

print("Election Results")
print("-" * 25)
print(f'Total Votes: {num_votes}')
print("-" * 25)
print(f'Khan: {total}')
print(f'Correy: {total}')
print(f'Li: {total}')
print(f"O'Tooley: {total}")
print("-" * 25)
print(f'Winner: {___}')
print("-" * 25)

        