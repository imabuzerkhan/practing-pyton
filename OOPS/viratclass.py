import datetime

class cricketPlayer:
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.scores = []  # Initialize an empty list for scores

    def get_score(self, score):
        self.scores.extend(score)  # Append score to the list

    def get_average(self) :
        if not self.scores :
            return 0  
        return sum(self.scores)/len(self.scores)
    def get_age(self) : 
        current_year = datetime.datetime.now().year
        return current_year - self.year
              

# Creating an instance
virat = cricketPlayer("Virat", "Kohli", 1984)

# Calling the method correctly
virat.get_score([30, 40, 50])

# Printing the scores
print(virat.scores)  # Output: [[30, 40, 50]]
print(f'Average of virat kholi is {virat.get_average()}')
print(f"The age of virat kholi is {virat.get_age()}")


print(virat.first_name)
print(virat.last_name)
print(virat.year)
