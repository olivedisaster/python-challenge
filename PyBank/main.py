#Modules
import os
import csv

budget = "Desktop/Bootcamp/Homework/HW 2/python-challenge/PyBank/Resources/budget_data.csv"

csvpath = os.path.join("Resources","budget_data.csv")

#Define Variables
months_tot = 0
profit_tot = 0
profit_chg_tot = 0
chg_tot = 0
gr_inc = 0
gr_dec = 99999999999
gr_month_inc = ""
gr_month_dec = ""
firsttime = True

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #Adding total months
        months_tot = months_tot + 1
        
        #Adding and printing total profits
        profit_tot = profit_tot + int(row[1])
        
        #Average profit/losses
        if not firsttime:
            profit_chg = int(row[1]) - previous_value
            profit_chg_tot += profit_chg

            if profit_chg > gr_inc:
                gr_inc = profit_chg
                gr_month_inc = row[0]

            if profit_chg < gr_dec:
                gr_dec = profit_chg
                gr_month_dec = row[0]
            

        firsttime = False
        previous_value = int(row[1])

    profit_chg_tot = profit_chg_tot/(months_tot - 1)
    profit_chg_tot = round(profit_chg_tot, 2)

    print(f"Total Months: {(months_tot)}")
    print(f"Total: {(profit_tot)}")
    print(f"Average Change: ${profit_chg_tot}")
    print(f"Greatest Increase in Profits: {gr_month_inc} ${gr_inc}")
    print(f"Greatest Decrease in Profits: {gr_month_dec} ${gr_dec}")

output_path = os.path.join("analysis", "Financial_Analysis.txt")

f = open(output_path, 'w')

f.write("Financial Analysis\n")
f.write("_______________________________\n")
f.write(f"Total Months: {(months_tot)}\n")
f.write(f"Total: ${profit_tot}\n")
f.write(f"Total Change: ${profit_chg_tot}\n")
f.write(f"Greatest Increase in Profits: {gr_month_inc} (${gr_inc})\n")
f.write(f"Greatest Decrease in Profits: {gr_month_dec} (${gr_dec})\n")
    

  

