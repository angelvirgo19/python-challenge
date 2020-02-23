import os
import csv
os.path.join('..','Resources','election_data.csv')
csvpath = os.path.join('..\\Resources\\election_data.csv')
csvpath
Candidate_names={}

Votes = []

with open(csvpath,mode='r') as file:
    csvreader = csv.reader(file, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Votes.append(row[0])
        Candidate = row[2]
        if Candidate in Candidate_names:
            Candidate_names [Candidate]+=1
        else:
            Candidate_names [Candidate]=1
            

            
    print("Election Results")
    print("-----------------------------------")
    print(f'Total Votes: {len(Votes)}')
    Total_Votes = len(Votes)
    Max_Votes = 0
    Winner = " "
    print("-----------------------------------")
    for Candidate in Candidate_names:
        Percentage_won = (Candidate_names [Candidate]/Total_Votes)*100
        print(f'{Candidate}: {Percentage_won:.3f}% ({Candidate_names[Candidate]})')
        if Candidate_names[Candidate]>Max_Votes:
            Max_Votes = Candidate_names[Candidate]
            Winner = Candidate

    print("-----------------------------------")
    print(f'Winner: {Winner}')
    print("-----------------------------------")

with open("Election_Results.txt","w") as file:
    file.write(" Election Results")
    file.write("\n-----------------------------------")
    file.write(f'\n Total Votes: {len(Votes)}')
    file.write("\n-----------------------------------")     
    for Candidate in Candidate_names:
        Percentage_won = (Candidate_names [Candidate]/Total_Votes)*100
        file.write(f'\n {Candidate}: {Percentage_won:.3f}% ({Candidate_names[Candidate]})')
    file.write("\n-----------------------------------")
    file.write(f'\n Winner: {Winner}')
    file.write("\n-----------------------------------")