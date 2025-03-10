'''1. Find Low-Scoring Students
You have a list of students and their test scores. Print the names of students who scored below 50.
'''
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
scores = [75, 40, 85, 30, 50]

lessmark = []

for (student , score) in zip(students,scores):
  if score < 50 :
    print(student , score)
#     lessmark.append((student , score))
  

# for lessscore in lessmark :
#   print(lessscore)
  
print("---------------------------------------------------------------------")

#without zip function 
people = ["John", "Emma", "Liam", "Sophia", "Noah"]
weights = [55, 45, 60, 48, 50]
lightweight = 50
underwight = []
# Write your code here to find underweight people
for i in range (len(people)):
  if weights[i] < lightweight :
    underwight.append(people[i])

for underwei in underwight :
  print(underwei)

print("---------------------------------------------------------------------")

# enumarate 
cities = ["New York", "Los Angeles", "Dubai", "Mumbai", "Paris"]
temperatures = [30, 25, 40, 38, 20]
hightemp = 40
hotcities = []

# Write your code here to find hot cities

for i , temperature in enumerate(temperatures) :
  if temperature >= hightemp :
    hotcities.append(cities[i])

print(hotcities)
