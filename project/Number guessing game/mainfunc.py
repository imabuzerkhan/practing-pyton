# random number genrate 
import random

#random number genration
def random_num(lower_bound , upper_bound) :
 return random.randint(lower_bound , upper_bound)
  

# Set bounds and generate random number
lower_bound = 1
upper_bound = 200
random_num_val = random_num(lower_bound, upper_bound)

# Display bounds
print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")


# using while loop make game more attractive 
while True  : 
   try :
     user = int(input("Enter the number (-1 to quit) :"))
     if user == -1 :
      print(f"You exist from game! random_num : {random_num}")
      break 
     elif user < lower_bound or user > upper_bound :
       print("Please enter a number within the bounds!")
     elif user == random_num_val :
       print(f"You guessed it right! guess num : {user} random num :   {random_num}")
     else : 
       print("Too high!" if user > random_num_val else "Too low!")
   except ValueError : 
       print("please enter a valid number")
       
     



