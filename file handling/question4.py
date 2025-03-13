# Now stitch all of the above code together and create a function that takes file name as input and returns the customer_summary dictionary.

def process_coustomer_data(filename) :
  customer_dic= {}
  with open (filename , "r") as f :
    for line in f :
      customer_name , customer_data = line.strip().split(",")
      customer_data = int(customer_data)
      customer_dic[customer_name] = customer_data

    def reward_fun(total):
     if total >=500 :
      return "Gold"
     elif total >=300 :
      return "sliver" 
     elif total >=200:
      return "Brownze"
     else : 
      return "sorry No reward for  you"
    
    #customer summary 
    customer_summry = {}
    for name , total in customer_dic.items() :
     reward_item = reward_fun(total)
     customer_summry[name] = (total , reward_item)

    return customer_summry 


summary = "customer.txt"
customer_summary = process_coustomer_data(summary)
print(customer_summary)

    




  
