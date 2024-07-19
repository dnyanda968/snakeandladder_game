# Snake and Ladder Game in Python

import random

def roll_dice():
    """Roll a dice and return the number"""
    return random.randint(1, 6)

def game():
    """Play the Snake and Ladder game"""
    player_position = 1
    ladder_positions = {3: 22, 5: 41, 11: 67, 20: 88}
    snake_positions = {25: 10, 43: 18, 54: 31, 62: 45}
    while player_position < 100:
        print(f"Current position: {player_position}")
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"You rolled a {dice_roll}")
        player_position += dice_roll
        if player_position in ladder_positions:
            print("You landed on a ladder!")
            player_position = ladder_positions[player_position]
        elif player_position in snake_positions:
            print("You landed on a snake!")
            player_position = snake_positions[player_position]
        if player_position > 100:
            player_position = 100
    print("Congratulations, you won!")

if __name__ == "__main__":
    game()
