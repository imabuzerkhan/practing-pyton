from pydantic import BaseModel
from typing import Optional
class user(BaseModel) :
  id : int 
  name : str 
  age : int 
  add : Optional[str] = None
abuzer = user(id=1 , name="Abuzer khan" , age="30" , add= "123 , patli gali" )

print(abuzer.name)
print(abuzer.age)
print(abuzer.add)