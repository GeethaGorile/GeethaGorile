import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x200")

# Adding buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Running the main loop
root.mainloop()
