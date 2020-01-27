import os
import csv
month_count = 0
profit_losses = 0
last_month = 0
this_month = 0
change = 0
greatest_inc = 0
greatest_dec = 0
average_change = 0
change_tally = 0

budget_data_path = os.path.join('Resources', 'budget_data.csv')

with open (budget_data_path, newline='') as budget_data:

    read_budget_data = csv.reader(budget_data, delimiter=',')

    data_header = next(read_budget_data)
    
    for row in read_budget_data:
        #budget(row)
        month_count += 1
        profit_losses += int(row[1])
        this_month = int(row[1])
        if last_month == 0:
            last_month = this_month
        change = this_month - last_month
        change_tally += change
        print (change)
        print (change_tally)
        print ("----------")
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_date = row[0]
        elif change < greatest_dec:
            greatest_dec = change
            greatest_dec_date = row[0]
        last_month = this_month
average_change = change_tally / month_count

print ("Financial Analysis")
print ("-------------------------------------------")
print (f"Total Months: {month_count}")
print (f"Total: ${profit_losses}")
print (f"Average Change: ${int(average_change)}")
print (f'Greatest Increase in Profits:  {greatest_inc_date}   |   ${greatest_inc}')
print (f'Greatest Decrease in Profits:  {greatest_dec_date}   |   ${greatest_dec}')