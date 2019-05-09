#Import Python modules for handling csv
import sys
import csv
import operator
#Open phonebook.csv file
myfile = csv.reader(open("phonebook.csv", 'rU'), delimiter=',', dialect=csv.excel_tab)
header=myfile.next()

#sort the data
sort = sorted(myfile, key=operator.itemgetter(1))

#Write result into a new csv file
with open("new_phonebook.csv", "wb") as f:
      fileWriter = csv.writer(f, delimiter = ',')
      for row in sort:
              fileWriter.writerow(row)

#return information from file
for first_name, last_name, phone1 in sort:
    print first_name, phone1


