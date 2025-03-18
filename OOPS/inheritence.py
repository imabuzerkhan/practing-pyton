class Animal :
  def __init__(self , name):
    self.name = name
  
  def speak(self) :
    return f"{self.name} makes a sound."

class Dog(Animal) :
  def __init__(self, name , breed):
    super().__init__(name)
    self.breed = breed 

  def bark(self) : 
    return f"{self.name} , the {self.breed} , barks loudly "
 
  
dog = Dog("buddy" , "Ishan")

print(dog.bark())
print(dog.speak())