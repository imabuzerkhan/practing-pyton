customer_dict = {}

with open("customer.txt" , "r") as f :
  for line in f :
   Name , score = line.split(",")
   score = int(score)
   customer_dict[Name] = score

print(customer_dict)
def reward(total) :
  if total >=500:
    return "Gold"
  elif total >=200:
    return "Sliver"
  elif total >=100:
    return "Brownze"
  else :
    return "No reward"
print(reward(400))

customer_summary = {}
for name , total in customer_dict.items() :
  rewards_level = reward(total)
  customer_summary[name] = (total , rewards_level)
print(customer_summary)

