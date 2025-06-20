import random 

# subject, action, place list
subject = [
  "Salman khan",
  "Sharukh khan",
  "Kp oli sharma",
  "Durga prasad", 
  "Abuzer khan", 
  "Zoya parween", 
  "Aaisha khatoon"
]

action = [
  "lunch khaana gaye",
  "yudh ghoshit kardiya gaya",
  "bhains ke saath sawaari karna gaya wo",
  "dushman ke saath taash khelna raha hai",
  "gadha ke saath shopping karna hai",
  "so rahi hai maja se",
  "logon se ladna hai"
]

places = [
  "India Gate, New Delhi",
  "Charminar, Hyderabad",
  "Gateway of India, Mumbai",
  "Howrah Bridge, Kolkata",
  "Amber Fort par, Jaipur",
  "Meenakshi Temple, Madurai",
  "Dal Lake, Srinagar"
]

# main loop
while True:
    subjects = random.choice(subject)
    actions = random.choice(action)
    place_or_thing = random.choice(places)

    Headline = f"Breaking News : {subjects} {actions} {place_or_thing} par!"
    print("\n" + Headline)

    user_input = input("Do you want more headlines? (yes/no): ").strip().lower()
    if user_input == "no":
        break

# goodbye
print("Thanks for using Fake Headline Generator!")
