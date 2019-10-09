#! python3
#Import Python modules for handling csv
import sys
import csv
import operator
#Marly was here
#Amber was here
#Toby was here
#Samantha was here
#Open phonebook.csv file
with open("phonebook.csv", "r") as myfile:
    checkreader = csv.reader(myfile)
    header = next(checkreader)
    sorted_data = sorted(checkreader, key = operator.itemgetter(1))
with open("newphonebook.csv", "w") as my_file:
    fileWriter = csv.writer(my_file, delimiter=',')
    if header:
        fileWriter.writerow(header)
    for row in sorted_data:
        fileWriter.writerow(row)
#I don't know how to edit python in terminal
