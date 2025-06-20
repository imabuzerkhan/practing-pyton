print("Hello Welcome to our Fake Headline Generator Website!")
print("Category options:")
print("1. Sports")
print("2. Politics")
print("3. Superstar")
print("4. User_choice")

while True:

    # loop to get valid category
    while True:
        category_choice = input("Choose a category (1/2/3/4): ").strip().lower()

        if category_choice == "1":
            Filename = "Sports.txt"
            break
        elif category_choice == "2":
            Filename = "Politics.txt"
            break
        elif category_choice == "3":
            Filename = "Superstar.txt"
            break
        elif category_choice == "4":
            Filename = "User_choice.txt"
            break
        else:
            print("Please enter a valid category (1/2/3/4)")

    # takes input from user
    subjects = input("Enter the subject: ")
    actions = input("Enter the actions: ")
    places = input("Enter the place: ")

    # Create the headline
    category_line = f"I have chosen {Filename} category:"
    headline = f"Breaking News: {subjects}{actions}{places}!"
    print(category_line + "\n" + headline)

    # add output to txt file 
    if category_choice == "1" :
        with open("Sports.txt", "a") as file:
         file.write(category_line + "\n" + headline + "\n\n") 
    elif category_choice == "2" :
        with open("Politics.txt", "a") as file:
         file.write(category_line + "\n" + headline + "\n\n")
    elif category_choice == "4" :
        with open("Superstars.txt", "a") as file:
         file.write(category_line + "\n" + headline + "\n\n")
    else :
        with open("User_choice.txt", "a") as file:
         file.write(category_line + "\n" + headline + "\n\n")

    # Ask user if they want more headlines
    while True:
        user_input = input("Do you want more headlines? (yes/no): ").strip().lower()
        if user_input in ["yes", "no"]:
            break
        else:
            print("Please enter a valid response: yes or no")

    if user_input == "no":
        print("Thanks for using our Fake Headline Generator!")
        break

# last message after file saving
print("✅ Your data is saved in 'headline.txt'!")
