# starting with dic 

student = {
  "name" : "abuzer khan" ,
  "age" : 20 ,
  "address" : "biratnagr-06" 
}
#change value 
student["name"] = "khan bhai"
#adding in dic
student["brother"] = "dansih khan"
# using in function to check value is exist or not 
check="khan bhai" in student
del student["address"]
print(check)
print(student) #its print whole dictionary 
# print(student["address"])
print(student.get("city")) # when value is not exist then it return none


# loop in dic or iterating to dic 
student = {
  "name" : "abuzer khan" ,
  "age" : 20 ,
  "address" : "biratnagr-06" 
}

for key , value in student.items() :
 print(key ,value)


# value nad key seprate

for key in student.keys() :
 print(key)

 # accesing only the value 

 for value in student.values() :
  print(value)

#nested dictionary 
country = {
 "india" : {
     "apple" : 8 ,
     "samsung" : 6 ,
     "redmi" : 10
    },
    "nepal" : {
     "apple" : 8 ,
     "samsung" : 6 ,
     "redmi" : 10
    }
  }

# value = country["nepal"]["redmi"] 
# value = country.get("nepal").get("redmi")
# print(value)
for countrys , product_data in country.items() :
  for product , rev in product_data.items() :
 
   print(f"{countrys} {product} : {rev}$")