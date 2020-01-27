import os
import csv

total_vote_count = 0
kahn_tally = 0
correy_tally = 0
li_tally = 0
o_tooley_tally = 0

csv_path = os.path.join('Resources', 'election_data.csv')

with open (csv_path, newline='') as election_data:
    read_election_data = csv.reader(election_data, delimiter=',')
    election_header = next(read_election_data)

    for row in read_election_data:
        total_vote_count += 1
        if row[2] == "Khan":
            kahn_tally += 1
        elif row[2] == "Correy":
            correy_tally += 1
        elif row[2] == "Li":
            li_tally += 1
        else:
            o_tooley_tally += 1

kahn_percent = (100 * kahn_tally) / total_vote_count
correy_percent = (100 * correy_tally) / total_vote_count
li_percent = (100 * li_tally) / total_vote_count
o_tooley_percent = (100 * o_tooley_tally) / total_vote_count

if o_tooley_tally > li_tally:
    winner = "O'Tooley"
elif li_tally > correy_tally:
    winner = "Li"
elif correy_tally > kahn_tally:
    winner = "Correy"
else:
    winner = "Kahn"

print ("--------------------")
print ("Election Results")
print ("--------------------")
print (f'Total Votes: {total_vote_count}')
print ("--------------------")
print (f'Kahn Tally: {round(kahn_percent, 2)}% ({kahn_tally})')
print (f'Correy Tally: {round(correy_percent, 2)}% ({correy_tally})')
print (f'Li Tally: {round(li_percent, 2)}% ({li_tally})')
print (f"O'Tooley Tally: {round(o_tooley_percent, 2)}% ({o_tooley_tally})")
print ("--------------------")
print (f'Winner: {winner}')
print ("--------------------")

results_file = os.path.join('Election Results', 'Election Results.csv')

with open (results_file, "w", newline='') as election_results:
    writer = csv.writer(election_results)

    writer.writerow(["--------------------"])
    writer.writerow(["Election Results"])
    writer.writerow(["--------------------"])
    writer.writerow([f'Total Votes: {total_vote_count}'])
    writer.writerow(["--------------------"])
    writer.writerow([f'Kahn Tally: {round(kahn_percent, 2)}% ({kahn_tally})'])
    writer.writerow([f'Correy Tally: {round(correy_percent, 2)}% ({correy_tally})'])
    writer.writerow([f'Li Tally: {round(li_percent, 2)}% ({li_tally})'])
    writer.writerow([f"O'Tooley Tally: {round(o_tooley_percent, 2)}% ({o_tooley_tally})"])
    writer.writerow(["--------------------"])
    writer.writerow([f'Winner: {winner}'])
    writer.writerow(["--------------------"])

