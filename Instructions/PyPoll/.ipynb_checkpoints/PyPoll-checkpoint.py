import os
import csv

TEXT_FILE = os.path.join("Analysis", "PyPoll.txt")

path = os.path.join("Resources", "election_data.csv")
#append 
votes = []
candidates =[]

#count candidate votes
counter = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "OTooley": 0  
}

with open(path, "r") as file:
    
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        votes.append(row)
        candidates.append(row[2])
#Counter
for candidate in candidates  :
    if candidate =="Khan":
        counter["Khan"] +=1
    elif candidate =="Correy":
        counter["Correy"] += 1
    elif candidate =="Li":
        counter["Li"] += 1
    elif candidate =="O'Tooley":
        counter["OTooley"] += 1  
    
#counter to integer

    khan_votes = int(counter["Khan"])
    correy_votes = int(counter["Correy"])
    li_votes = int(counter["Li"])
    otooley_votes = int(counter["OTooley"])

# Votes per Candidate by percent

    total_votes = khan_votes + correy_votes + li_votes + otooley_votes
    k_p = (khan_votes / total_votes) * 100
    c_p = (correy_votes / total_votes) * 100
    l_p = (li_votes / total_votes) * 100
    o_p = (otooley_votes / total_votes) * 100

 # Winner
    if k_p > max(c_p, l_p, o_p):
        winner = "Khan"
    elif c_p > max(k_p, l_p, o_p):
        winner = "Correy"
    elif l_p > max(c_p, k_p, o_p):
        winner = "Li"
    else:
        winner = "O'Tooley"


# Final Print out
print("Election Results")
print("-" * 25)
print(f'Total Votes: {len(votes)}')
print("-" * 25)
print(f"Khan: {float(k_p)}% ({counter['Khan']})")
print(f"Correy: {round(c_p)}% ({counter['Correy']})")
print(f"Li: {round(l_p)}% ({counter['Li']})")
print(f"O'Tooley: {round(o_p)}% ({counter['OTooley']})")
print("-" * 25)
print(f"Winner: {winner}")
print("-" * 25)

#.txt file

with open (TEXT_FILE, "w") as file:
    print("TEST")