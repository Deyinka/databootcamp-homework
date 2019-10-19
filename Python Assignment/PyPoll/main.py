# Import os module that has functions to interact with the file system
import os
# Import module for reading CSV files
import csv

#Get current working directory
csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Resources", "election_analysis.txt")


#Initialize variables
Totalcount = 0; Kcount = 0; Ccount = 0; Lcount = 0; Ocount = 0; MXV_count = 0

#Function for % calculation
def percentage (part, whole):
    return 100 * float(part)/float(whole)

#Open and read CSV file
with open(csvpath, newline='') as electionData:
     csvreader = csv.reader(electionData, delimiter=',')

     for y in csvreader:
         voterid = y[0]
         country = y[1]
         candidate = y[2]
         # Total Vote Count
         Totalcount = Totalcount + 1

         # Candidate's votecount
         if candidate =="Khan":
            Kcount = Kcount + 1
         if candidate =="Correy":
            Ccount = Ccount + 1
         if candidate =="Li":
            Lcount = Lcount + 1
         if candidate =="O'Tooley":
            Ocount = Ocount + 1
            
# Define (dictionary) list : candidate and votes
     candidatevote = {"Khan": Kcount,"Correy": Ccount,"Li" :Lcount, "O'Tooley": Ocount}
     # Find winner 
     for candidate, value in candidatevote.items():
         if value > MXV_count:
            MXV_count = value
            Winner = candidate
# Display results       
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {Totalcount}'+'\n')
print(f'-------------------------------'+'\n')
print(f'Khan: {percentage(Kcount,Totalcount):.3f}%  ({Kcount})')
print(f'Correy: {percentage(Ccount,Totalcount):.3f}%  ({Ccount})')
print(f'Li: {percentage(Lcount,Totalcount):.3f}%  ({Lcount})')
print(f'O\'Tooley: {percentage(Ocount,Totalcount):.3f}%  ({Ocount})')
print(f'-------------------------------'+'\n')
print(f'Winner: {Winner} '+'\n')
print(f'-------------------------------'+'\n')