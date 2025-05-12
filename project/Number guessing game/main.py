# random number genrate 
import random
# set the limit 
lower_bound = 1 
upper_bound = 200

#random number genration
random_num = random.randint(lower_bound , upper_bound)

#bound
print("lower_bound : 1")
print("upper_bound : 200")


# using while loop make game more attractive 
while True  : 
   try :
     user = int(input("Enter the number (-1 to quit) :"))
     if user == -1 :
      print(f"You exist from game! random_num : {random_num}")
      break 
     elif user < lower_bound or user > upper_bound :
       print("Please enter a number within the bounds!")
     elif user == random_num :
       print(f"You guessed it right! guess num : {user} random num :   {random_num}")
     else : 
       print("Too high!" if user > random_num else "Too low!")
   except ValueError : 
       print("please enter a valid number")
       
     



