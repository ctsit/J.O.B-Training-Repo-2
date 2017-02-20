#Import Python modules for handling csv
import sys
import csv
import os

#Open phonebook.csv file
myfile = csv.reader(open("phonebook.csv", 'rU'), delimiter=",", dialect=csv.excel_tab)

#Return information from file
peoples_contacts = []
header=next(myfile)
for first_name, last_name, phone1 in myfile:
   peoples_contacts.append((first_name, last_name, phone1))

sorted_by_lastname = sorted(peoples_contacts, key=lambda tup: tup[1])

print sorted_by_lastname

with open('output_file.csv','w') as out:
   csv_out=csv.writer(out)
   csv_out.writerow(header)
   for row in sorted_by_lastname:
       csv_out.writerow(row)

