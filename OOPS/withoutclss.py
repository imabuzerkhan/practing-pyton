import datetime

def getaverage(player) :
 return sum(player["scores"])/len(player["scores"])

def get_age(players) : 
 current_year = datetime.datetime.now().year
 return current_year - players["birth_year"]

virat = {
  "firstName" : "virat" ,
  "lastName" : "Kholi" ,
  "scores" : [] ,
  "birth_year" : int(1984)
  

}
virat["scores"].append(60)
virat["scores"].append(40)
virat["scores"].append(87)

warner = {
  "firstName" : "david" ,
  "lastName" : "warner" ,
  "scores" : [] ,
  "birth_year" : 1986

}
warner["scores"].append(40)
warner["scores"].append(70)
warner["scores"].append(57)

Average_of_plyer = getaverage(warner)
print(Average_of_plyer)

get_age_of_player = get_age(warner)
print(f" The age of {warner['firstName']} {warner['lastName']} is {get_age_of_player}")
