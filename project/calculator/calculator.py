class inputNumber : 
  def __init__(self):
    self.num1 = float(input("Enter the first number:"))
    self.num2 = float(input("Enter the Scond number:"))

class Calculator(inputNumber) :
  
  def Add(self) :
    return self.num1 + self.num2

  def Sub(self):
    return self.num1 - self.num2 
   
  def mul(self) :
    return self.num1 * self.num2 
  
  def div(self) : 
    if self.num2 != 0 :
      return self.num1 / self.num2
    else : 
      return "cannot divisble by zero"

# calling the calculator class
calc = Calculator()

# Menu for operations
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# choice for calculation
choice = input("Enter the choice(1,2,3,4)")

if choice == "1" : 
  print("Result: " , calc.Add())
elif choice == "2" : 
  print("Result:" , calc.Sub())
elif choice == "3" : 
  print("Result:" , calc.mul())
elif choice == "4" :
  print("Result:" , calc.div())
else : 
  print("Enter valid Number")
