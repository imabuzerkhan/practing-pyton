# function in python 
Abuzer_expense = [23,345, 678, 980,789]
Danish_expense = [32,543,876, 98, 987] 

# making one function total expense of both
def Total_Expenses(expense):
  total = 0 
  for expenses in expense :
    total += expenses 
  return total  

# call the function
print(Total_Expenses(Abuzer_expense))
print(Total_Expenses(Danish_expense))






# finding the volume of cylinder 
def Volumeofcylinder(radius , height) :

  volume = 3.14 * (radius *2) * height
  return volume

Volumeofcylinders = Volumeofcylinder(radius=23 , height=6)
print(f"The volume of cylinder is: {Volumeofcylinders}")