#PyBank Module 3 Python Challenge 

#Import dependencies 
import os
import csv

#Load file path 
file_to_load = os.path.join("Resources", "budget_data.csv")

#Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "budget_analysis.txt")

#Intialize parameters 
total_months = 0 
total_profit = 0 
profit = []
previous_profit = 0 
monthly_change = []
profit_change = 0 
greatest_decrease = ["", 99999999]
greatest_increase = ["", 0]
profit_change_list = []
profit_average = 0 

#Read csv file 
with open (file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)
    
    for row in reader:
        total_months += 1 
        total_profit = total_profit + int(row["Profit/Losses"])

        profit_change = float (row ["Profit/Losses"]) - previous_profit
        previous_profit = float (row ["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        monthly_change = [monthly_change] + [row["Date"]]

        if profit_change>greatest_increase[1]:
            greatest_increase[1] = profit_change
            greatest_increase[0] = row["Date"]
        
        if profit_change<greatest_decrease[1]:
            greatest_decrease[1] = profit_change
            greatest_decrease[0] = row["Date"]
    
    profit_average =round(sum(profit_change_list)/ len(profit_change_list))

    with open (file_to_save, "w") as txt_file:
        
        bank_data = (
        f"\nFinancial Analysis\n"
        f"------------------------\n"
        f"Total Months: {total_months:,}\n"
        f"Total Profit: ${total_profit}\n"
        f"Average Change: $ {profit_average}\n"
        f"Greatest Increase in Profits: $ {greatest_increase [0], greatest_increase[1]}\n"
        f"Greatest Decrease in Profits: $ {greatest_decrease [0], greatest_decrease[1]}\n"
        f"---------------------------------\n")
        print(bank_data)
        txt_file.write(bank_data)
   
