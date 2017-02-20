#Import Python modules for handling csv
import sys
import csv
import os

#Open phonebook.csv file
myfile = csv.reader(open("phonebook.csv", 'rU'), delimiter=",", dialect=csv.excel_tab)

#Return information from file
contacts = []
header = next(myfile)
for first_name, last_name, phone1 in myfile:
   contacts.append((first_name, last_name, phone1))

sorted_by_last = sorted(contacts, key=lambda tup: tup[1])

print sorted_by_last

f = open(os.getcwd() + "/contacts.sorted", "w")

with open('output.csv','w') as out:
   csv_out=csv.writer(out)
   csv_out.writerow(header)
   for row in sorted_by_last:
       csv_out.writerow(row)