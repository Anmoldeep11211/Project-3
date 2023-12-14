import random

# Assign odd and even to the players
players = ['Player 1', 'Player 2']
odd_player = random.choice(players)
even_player = [player for player in players if player != odd_player][0]

print(f"{odd_player} is Odd Player and {even_player} is Even Player")

# Let odd_player choose their number
odd_number = int(input(f"{odd_player}, choose a number between 1 to 10: "))

# Generate a random number for even_player
even_number = random.randint(1, 10)
print(f"{even_player} chooses {even_number}.")

# Calculate sum of numbers
total = odd_number + even_number

# Determine winner
if total % 2 == 1:
    print(f"{odd_player} wins! {odd_number} + {even_number} is odd.")
else:
    print(f"{even_player} wins! {odd_number} + {even_number} is even.")
    import random

# Assign odd and even to the players
players = ['Player 1', 'Player 2']
odd_player = random.choice(players)
even_player = [player for player in players if player != odd_player][0]

print(f"{odd_player} is Odd Player and {even_player} is Even Player")

# Game loop for the first round
while True:
    # Players choose numbers
    odd_number = int(input(f"{odd_player}, choose a number between 1 to 10: "))
    even_number = random.randint(1, 10)
    print(f"{even_player} chooses {even_number}.")

    # Calculate sum of numbers
    total = odd_number + even_number

    # Determine winner
    if total % 2 == 1:
        print(f"{odd_player} wins the toss!")
        chosen_player = odd_player
        other_player = even_player
        break
    else:
        print(f"{even_player} wins the toss!")
        chosen_player = even_player
        other_player = odd_player
        break

# Choose batting or bowling
print(f"{chosen_player}, do you want to bat or bowl?")

while True:
    choice = input("Enter 'bat' or 'bowl': ")
    if choice == 'bat':
        batting_player = chosen_player
        bowling_player = other_player
        break
    elif choice == 'bowl':
        batting_player = other_player
        bowling_player = chosen_player
        break
    else:
        print("Invalid input. Please enter 'bat' or 'bowl'.")

# Batting loop
batting_score = 0
while True:
    # Player chooses a number
    batting_number = int(input(f"{batting_player}, choose a number between 1 to 10: "))
    bowling_number = random.randint(1, 10)
    print(f"{bowling_player} chooses {bowling_number}.")

    # Determine if the batting player is out
    if batting_number == bowling_number:
        print(f"{batting_player} is out!")
        break
    else:
        batting_score += batting_number

# Determine winner of the game
if batting_score > 0:
    print(f"{batting_player} scores {batting_score} runs.")
    print(f"{bowling_player} needs to score {batting_score+1} runs to win.")

    # Batting loop for the second player
    batting_score2 = 0
    while batting_score2 < batting_score:
        # Player chooses a number
        batting_number2 = int(input(f"{bowling_player}, choose a number between 1 to 10: "))
        bowling_number2 = random.randint(1, 10)
        print(f"{batting_player} chooses {batting_number2}.")

        # Determine if the batting player is out
        if batting_number2 == bowling_number2:
            print(f"{bowling_player} is out!")
            break
        else:
            batting_score2 += batting_number2

    # Determine winner of the game
    if batting_score2 >= batting_score:
        print(f"{bowling_player} wins!")
    else:
        print(f"{batting_player} wins!")
else:
    print(f"{bowling_player} wins without batting!")  