#Import Python modules for handling csv
import sys
import csv
import operator
#Open phonebook.csv file
with open("phonebook.csv", "rU") as myfile:
    checkreader = csv.reader(myfile)
    header = next(checkreader)
    sorted_data = sorted(checkreader, key = operator.itemgetter(1))
with open("dileepPhoneBook.csv", "wb") as my_file:
    fileWriter = csv.writer(my_file, delimiter=',')
    if header:
        fileWriter.writerow(header)
    for row in sorted_data:
        fileWriter.writerow(row)
