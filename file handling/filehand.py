# read txt file in python

f = open("text.txt" , "r")
for line in f :
  print(line)

f.close()

# reding another file
filereading = open("love.txt","r")
content =filereading.read()
print(content)
filereading.close() 

# open file with (with method)

with open("text.txt","r") as Fileread :
 content = Fileread.readlines()
print(content)

# create file using file handling 

with open("hello.txt", "w") as f :
  f.write("hello world\n")
  f.writelines("where are you from ")

# append the file in love.txt because when we appen the file it dosenot overrite it 

with open("love.txt", "a") as append :
 append.write("kasto xau hau timmi\n")

# using list as append mode 

with open("text.txt", "a") as f :
  f.writelines([
    "i am a king\n",
    "you are not a king\n" ,
    "tumhare bolne se kya hum king hai na babu\n"
  ])

