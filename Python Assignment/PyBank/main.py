import os
# Import module for reading CSV files
import csv

#Get current working directory
cvspath = os.path.join("Resources", "budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")

#Initialize variables
tMcount = 0
totalPL = 0
PreviousPL = 0
PL_change = 0
PL_Max = 0
PL_Min = 0
Avg_PL_change = 0
#Open and read CSV file
with open(cvspath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         PL_change =  iAmount - PreviousPL
         

         #greatest increase in profits
         if PL_Max < PL_change:
            PL_Max = PL_change
            PL_MaxDate = month
         #greatest decrease in profits 
         if PL_Min > PL_change:
            PL_Min = PL_change
            PL_MinDate = month

         PreviousPL = iAmount   
         # Get total months
         tMcount= tMcount + 1
         totalPL += int(Amount) 

        
         

## Display Results ##      
#The total number of months included in the dataset
print(f'Total Months: {tMcount}')
#The total net amount of "Profit/Losses" over the entire period
print(f'Total: $ {totalPL}')
# Average Profit/Losses over the entire period
print(f'Average Profit/Losses: {Avg_PL_change}')
# Greatest increase in profit
print(f'Greatest Increase in Profits: {PL_MaxDate} : ($ {PL_Max})')
# Greatest increase in profit
print(f'Greatest Decrease in Profits: {PL_MinDate} : ($ {PL_Min})')
