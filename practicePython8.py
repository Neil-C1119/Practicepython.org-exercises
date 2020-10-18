# This program is a 2 player game of rock paper scissors

# Ask if the user would like to start a game or not
userQuit = input("Type 'start' to start a game, or 'quit' to quit the game. : ").lower()

# A loop that is continuous as long as the user answers "start" to start games
while userQuit != "quit":

    # Get both players' moves
    player1 = input("Player 1; rock, paper, or scissors? ").lower()
    player2 = input("Player 2; rock, paper, or scissors? ").lower()

    # Determine which user wins and print a congratulation for that user
    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    elif (player2 == "rock" and player1 == "scissors") or (player2 == "scissors" and player1 == "paper") or (player2 == "paper" and player1 == "rock"):
        print("Player 2 wins!")

    # Ask the user if they would like to play again after one wins
    userQuit = input("Type 'start' to start a game, or 'quit' to quit the game. : ").lower()

    # If the user answers "quit" to whether they'd like to play again, the loop will break
    if userQuit == "quit":
        break
