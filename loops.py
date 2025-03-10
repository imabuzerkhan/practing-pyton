#loop in python 
# for loop

list = [1,2,3,4,5,6,7,8,9,10]
for value in list :
  print(value)

  #problem one
total = 0
expenses = [200 , 400 , 600, 800 ,1000]
for expense in expenses :
  total += expense

print(f"the total expense is {expense}")

#problem two
totalval = 0
Expenses = [200 , 400 , 600, 800 ,1000]
for i in range(len(Expenses)) :
  expense = Expenses[i]
  totalval += expense
  print(f"month {i} is a {expense} ")
print(f'the total expense is {totalval}')

# using enumerate and zip() together
totalval = 0
Expenses = [200 , 400 , 600, 800 ,1000]
month = ['jan', 'feb', 'mar', 'april', 'may']
for i, (expenses,months) in enumerate(zip(Expenses, month)) :
  totalval += expenses
  print(f" {months} month expense is: {expenses} ")
print(f'the total expense is {totalval}')

#break 
Expenses = [200 , 400 , 600, 800 ,1000]
for i in range(len(Expenses)):
   if Expenses[i] >= 200 :
    print("it match our terms")
    break
   else :
    print("it doesnot match our terms")

    # break
for i in range(10):
    if i == 5:
        break  # Exits the loop when i equals 5
    print(i)

    # continue
for i in range(10):
    if i == 5:
        continue  # continue the loop 
    print(i)

# while loop
num = 0
while num <10 :
   print(num)
   num +=1
