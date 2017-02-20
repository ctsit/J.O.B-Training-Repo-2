#Import Python modules for handling csv
import sys
import csv

#Open phonebook.csv file
myfile = csv.reader(open("phonebook.csv", 'rU'), delimiter=",", dialect=csv.excel_tab)

contlist=[]
#Return information from file
for first_name, last_name, phone1 in myfile:
    contlist.append((first_name, last_name, phone1))

sortedlist = sorted(contlist, key=lambda tup: tup[1])
sortedlist = sortedlist[:-1]
with open('sorted.txt', 'w') as fp:
    fp.write('\n'.join('%s %s %s' % x for x in sortedlist))
