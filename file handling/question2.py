'''
The rewards levels are defined below based on the total purchase amount. Using this define a function called calculate_rewards that takes total as input and returns the reward.

1. Bronze: Total purchases $100-$199
1. Silver: Total purchases $200-$499
1. Gold: Total purchases $500+

'''

def calculate_rewards(total_purchse) :
  if total_purchse >= 500 :
    return "Gold"
  elif total_purchse >=200 :
    return "Sliver"
  elif total_purchse >= 100 :
    return "Bronze"
  else :
    return "No rewards"


print(calculate_rewards(530))

  