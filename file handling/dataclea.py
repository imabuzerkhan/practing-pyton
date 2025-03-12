player_score = {}

with open("score.csv", "r") as f:
    for line in f:
        player, score = line.strip().split(",")  # Remove '\n' and split
        score = int(score)

        if player in player_score:
            player_score[player].append(score)
        else:
            player_score[player] = [score]  # Create a new list

for player , score in player_score.items() :
    print(player , score)
    min_value = min(score)
    max_value = max(score)
    avg_value = sum(score)/len(score)
    
    print(f"{player} ==> min value: {min_value} max value: {max_value} avg value: {avg_value}")