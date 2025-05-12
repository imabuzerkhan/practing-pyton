from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello():
  return "hello world"

@app.get("/hello")
def hello():
  return "hello abuzer khan"

@app.get("/hello/{name}")
def hello(name):
  return f"hello {name}"


food_items = {
  "indian" : ["pizza" , "biryani"] ,
  "america" : ["hot dog" , "apple"] ,
  "china" : ["chowmin" , "momo"]
}

@app.get("/get_item/{cusine}")
def hello(cusine):
  items = food_items.get(cusine)
  if not items :
    return f"{cusine} cusine is not avilable "
  else :

   return food_items.get(cusine)
