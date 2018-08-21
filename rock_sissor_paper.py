# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!


def rps(s1, s2):
    d = { 
        'rs': 'Player 1 won!',
        'rp': 'Player 2 won!',
        'ps': 'Player 2 won!',
        'pr': 'Player 1 won!',
        'sr': 'Player 2 won!',
        'sp': 'Player 1 won!',
        'ss': 'Draw!',
        'pp': 'Draw!',
        'rr': 'Draw!',
    }
    return d[s1[0] + s2[0]] if s1[0] + s2[0] in d else None

print(rps('paper','paper'))
