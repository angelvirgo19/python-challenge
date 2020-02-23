import os
import csv
os.path.join('..','Resources','budget_data.csv')
csvpath = os.path.join('..\\Resources\\budget_data.csv')
csvpath
Months = []
Net = []
change= []
with open(csvpath,mode='r') as file:
    csvreader = csv.reader(file, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        Months.append(row[0])
        Net.append(float(row[1]))
        
    for i in range(1,len(Net)):
        change.append(Net[i] - Net[i-1])   
        avg_net_change = sum(change)/len(change)
        max_net_change = max(change)
        min_net_change = min(change)
        max_net_change_Months = str(Months[change.index(max(change))])
        min_net_change_Months = str(Months[change.index(min(change))])




print("Financial Analysis")
print("------------------------------------------------------------")
print(f'Total Months: {len(Months)}')
print(f'Total: $ {sum(Net)}')
print(f'Average Profit/Loss Change: $ {(round((avg_net_change),2))}')
print(f'Greatest Increase in Profits: {max_net_change_Months} (${(round(max_net_change))})')
print(f'Greatest Decrease in Profits: {min_net_change_Months} (${(round(min_net_change))})')

with open("Financial_Analysis.txt","w") as file:
    file.write(" Financial Analysis")
    file.write("\n------------------------------------------------------------")
    file.write(f'\n Total Months: {len(Months)}') 
    file.write(f'\n Total: $ {sum(Net)}')
    file.write(f'\n Average Profit/Loss Change: $ {(round((avg_net_change),2))}')
    file.write(f'\n Greatest Increase in Profits: {max_net_change_Months} (${(round(max_net_change))})')
    file.write(f'\n Greatest Decrease in Profits: {min_net_change_Months} (${(round(min_net_change))})')