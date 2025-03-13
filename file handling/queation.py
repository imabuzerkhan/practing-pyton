'''
Task 1
You are given a file called customers.txt that contains the name of the customer and total amount they spent. Read this file line by line and save the customer name and total amount in a dictionary.

For example, customers.txt file will content the data in the following format,

Srinivas,120
John,250
Maria,150
Smith,510
Anjali,45
You will read this and build a dictionary like this,

{
    "Srinivas": 120,
    "John": 250,
    "Maria": 150,
    "Smith": 510,
    "Anjali": 45
}
'''

coustomer_data = {}
with open("coustomer.txt" , "r") as f :
  for line in f :
    coustomer_name , coustomers_data = line.strip().split(",")
    coustomers_data = int(coustomers_data)
    coustomer_data[coustomer_name] = coustomers_data
  
print( coustomer_data)


