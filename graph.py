# importing csv module 
import matplotlib.pyplot as plt 
import csv 

# csv file name 
filename = "graph.csv"

# initializing the titles and rows list 
fields = []
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	

	# extracting each data row one by one 
	for row in csvreader: 
		# get total number of rows 
		#print(row)
		fields.append(int(row[0]))
		rows.append(int(row[1]))

print(fields)
print(rows)
plt.bar(fields,rows)

plt.show()

'''
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 
'''