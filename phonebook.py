#Import Python modules for handling csv
import sys
import csv

#Open phonebook.csv file
myfile = csv.reader(open("phonebook.csv", 'rU'), delimiter=",", dialect=csv.excel_tab)

header=myfile.next()

class info():
	def __init__(self, first_name, last_name, phone1):
		self.first_name = first_name
		self.last_name = last_name
		self.phone1 = phone1
	def __cmp__(self,other):
		return cmp(self.last_name,other.last_name)

info_list = []
#Return information from file
for first_name, last_name, phone1 in myfile:
    info_list.append(info(first_name, last_name, phone1));

info_list.sort()

with open('newphonebook.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(header)
	for info in info_list:
		writer.writerow([info.first_name, info.last_name, info.phone1])