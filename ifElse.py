# Now start praticing if-else and elif

#print odd and even number
# n = input('enter the number:') 
# n = int(n) # it is called typecasting 
# if n%2==0 :
#   print(f"{n} is a even number")
# else :
#   print(f"{n} is a odd number")

# problrm no 2 
# ternary operatory

# n = input('enter the number:') 
# n = int(n) 
# message = f"{n} is even number" if n%2==0 else "f{n} is a odd number"
# print(message)

# # And operator & or operator

# money = 2000
# if money <= 1500 and money == 2000 :
#   print(f"{money} both re true then it return true")
# elif money >=2000 or money <= 2000 :
#   print(f"{money} one value is true than it return true ")
# else :
#   print("i dont now anythig about ths ")

#   # not operator

# vikas = "balckshirt"
# if vikas == "whiteShirt" :
#   print("vikas wear a whiteshirt ")
# elif not vikas == "greenshirt" :
#   print(f"vikas is wearing a {vikas}")
# else :
#   print("it wear nothing")



#nested if statement
age = int(input("enter your age please: "))
if age >= 28 :
  print("Eligible for full benefits")
else:
  if age>=24 :
     print("Eligible for half benefits")
  else :
    if age >=18 :
       print("Eligible for some benefits")
    else :
      print("you are not eligible for any benifits your age is too less")