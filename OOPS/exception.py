
# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the number: "))

# try : 
#   division = num1 / num2 
# except :
#   print("it is not possible to divisble by zero")

# specific exceptation
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

try : 
  division = num1 / num2 
except ZeroDivisionError as ze :
  print("Exceptation occured" , ze)
finally :
  print("the code is excuted any how")
print(division)
  
