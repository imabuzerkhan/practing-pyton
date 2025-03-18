import datetime

class cricketplayer :
  def __init__(self,fname,lname,year,country ):
    self.first_name = fname 
    self.last_name = lname
    self.year = year
    self.scores = []
    self.country = country 
  
  # add score in scores
  def get_score(self , score) :
    self.scores.extend(score) 
  
  # find averafge of david warner 
  def get_average(self) :
    if not self.scores :
      return 0
    return sum(self.scores)/len(self.scores)
  
  # find the age of david warner with the help of dob
  def get_age(self) : 
    curret_year = datetime.datetime.now().year
    return curret_year - self.year
  
  # we can return directly a string which will represent instance of a class
  def __str__(self):
    return f" My name is {warner.first_name} {warner.last_name} . I am {warner.get_age()} years old. and i am from {warner.country} and my average is {warner.get_average()} "
  
  # operator overlading for less than 
  def __lt__(self , other) :
    self_get_average = self.get_average()
    other_get_average  = other.get_average()
    return self_get_average < other_get_average
  
  def __eq__(self, other):
    self_get_age = self.get_age()
    other_get_age  = other.get_age()
    return self_get_age < other_get_age
  
    


warner = cricketplayer("david", "warner" , 1991, "Austrlia")
virat = cricketplayer("virat" , "kholi" , 1988, "India")

# add score in scores 
warner.get_score([60,70,56])
virat.get_score([78, 87, 67])


# print thefull deatil about david warner
print(f" My name is {warner.first_name} {warner.last_name} . I am {warner.get_age()} years old. and i am from {warner.country} and my average is {warner.get_average()} ")

# print thefull deatil about virat kholi
print(f" My name is {virat.first_name} {virat.last_name} . I am {virat.get_age()} years old. and i am from {virat.country} and my average is {virat.get_average()} ")

print(warner)

# operator overloading 
print(virat > warner)
print(virat == warner)
  