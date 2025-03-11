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





# function arguments 
def sumall(*args) :  #it recived argument as a tuple 
  print(args)
  total = 0

  for sum in args :
    total += sum
  return total

#call value
totalvalue = sumall(1,2,3,4,5,6,7,8,9,10)
print(f"The sum of all value is: {totalvalue}")
print(type(totalvalue))

#Example: Passing 1,000 Numbers to a Function

def Addingval(*args) :
  return sum(args)


number = range(1 , 1001)
result = Addingval(*number)
print(result)


# understanding the *kwargs
def Kwargs():
  pass

# understanding lambda 

x = lambda a : a * a 
print(x(5))

sub = lambda a ,b : b - a
print(sub(6 , 10))

mul = lambda a , b ,c : a*b*c
print(mul(2,4,6))

# lmabda is a quicly way to write a  function 
      