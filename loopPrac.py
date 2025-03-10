'''
Managing inventory efficiently is crucial for businesses to ensure they do not run out of key products. This exercise simulates a simple inventory management system where the user can see which items are below the minimum stock level and need reordering. Below you have two lists that stores product names and their inventory stock levels.Using that,

Check each item to see if its stock level is below a minimum threshold.
If the stock level is below the minimum, add the product's name to a reorder list.
Print a list of products that need to be reordered.

'''

# Lists to store product names and stock levels
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering

reorder_list = []

for i , stock_level in enumerate(stock_levels) :
  print(f'{i} {stock_level}') # it returns both index and value
  if stock_level < minimum_stock :
    reorder_list.append(product_names[i])

print("roerder list")
for product in reorder_list :
  print(product)



# zip() 
product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering

reorder_list = []
for (product , stock) in zip(product_names , stock_levels) :

  if stock < minimum_stock :
    reorder_list.append(product)

print("reorder list")
for reproduct in reorder_list :
  print(reproduct)

