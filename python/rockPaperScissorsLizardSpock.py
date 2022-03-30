# Rock Paper Scissors Lizard Spock
# 
# Rules:
# - Scissors cuts Paper
# - Paper covers Rock
# - Rock crushes Lizard
# - Lizard poisons Spock
# - Spock smashes Scissors
# - Scissors decapitates Lizard
# - Lizard eats Paper
# - Paper disproves Spock
# - Spock vaporizes Rock
# - (and as it always has) Rock crushes Scissors
#
# Task: player1 vs player2, return an array of which player wins, eg.
# ["player1 wins", "player2 wins", "both players draw"..].

def vs(player1, player2):
    result = []
    rules = {
        "scissors": ["paper", "lizard"],
        "paperWin": ["rock", "spock"],
        "rock": ["lizard", "scissors"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    for i in range (len(player1)):
        if player1[i] == player2[i]: result.append("both players draw")
        if player2[i] in rules.get(player1[i]): result.append("player1 wins")
        if player1[i] in rules.get(player2[i]): result.append("player2 wins")
    return result

player1 = ["scissors", "paper", "rock", "lizard", "spock"]
player2 = ["scissors", "spock", "lizard", "rock", "paper"]
print(vs(player1, player2))
