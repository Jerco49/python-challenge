import os
import csv

# default values of variables used
total_net = 0
previous_row = 0
current_net = 0
net_changes = []
net_change_month = []
total_net_change = 0
average_change = 0
greatest_increase = 0
greatest_increase_month = "none"
greatest_decrease = 0
greatest_decrease_month = "none"
month_count = 0
ifFirst = True

# imports the file
csv_file = os.path.join('budget_data.csv')

# opens and reads the file
with open(csv_file, 'r') as text:
    csvreader = csv.reader(text, delimiter = ',')

    # omits the column titles from csvreader
    csv_header = next(csvreader)

    for row in csvreader:
        # Counts the number of months
        month_count  = month_count + 1

        # Adds together the net profit and loss
        total_net = total_net + int(row[1])

        # Stores the changes in profits/losses in a list
        if ifFirst == True:
            current_net = 0
            ifFirst = False
        else:
            current_net = int(row[1]) - previous_row
            net_changes.append(current_net)
            net_change_month.append(row[0])
        
        previous_row = int(row[1])

        # Checks each row for the greatest increase and decrease
        #if int(row[1]) > greatest_increase:
         #   greatest_increase = int(row[1])
         #   greatest_increase_month = row[0]

        #elif int(row[1]) < greatest_decrease:
         #   greatest_decrease = int(row[1])
         #   greatest_decrease_month = row[0]

    # Checks each row for the greatest increase and decrease
    for net in net_changes:
        if net > greatest_increase:
            greatest_increase = net
            greatest_increase_month = net_change_month[net_changes.index(net)]

        elif net < greatest_decrease:
            greatest_decrease = net
            greatest_decrease_month = net_change_month[net_changes.index(net)]

# Calculates the average change
for net in net_changes:
    total_net_change = total_net_change + net
average_change = round(total_net_change / (month_count - 1),2)

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_net))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")