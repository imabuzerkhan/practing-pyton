class Player:
    def __init__(self, fname, lname, year):
        self.first_name = fname
        self.last_name = lname
        self.year = year
        self.scores = []  # Common scores list sabke liye

    def get_average(self):
        if len(self.scores) == 0:  
            return 0  # ⚠️ Error na aaye, isliye check kar rahe hain
        return sum(self.scores) / len(self.scores)

class TennisPlayer(Player):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname, year)
        self.aces = []  # TennisPlayer ke liye extra field

    def get_aces(self, ace):
        self.aces.extend(ace)

class CricketPlayer(Player):
    def get_score(self, score):
        self.scores.extend(score)

# ✅ Object Banayein
virat = CricketPlayer("Virat", "Kohli", 1984)
roger = TennisPlayer("Roger", "Khan", 2000)

# ✅ Score aur Aces Add Karein
roger.get_aces([0, 45, 67, 89, 45])  # Roger ke liye aces
virat.get_score([40, 45, 67, 89, 45])  # Virat ke liye scores

# ✅ Data Print Karein
print("Virat Scores:", virat.scores)  # ✅ [40, 45, 67, 89, 45]
print("Roger Aces:", roger.aces)  # ✅ [0, 45, 67, 89, 45]

# ✅ Common get_average() method ka use karein
print("Virat's Average:", virat.get_average())  # ✅ 57.2
print("Roger's Average:", roger.get_average())  # ✅ 0 (kyunki Roger ke scores empty hain)
