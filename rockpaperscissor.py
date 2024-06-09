import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_choice = var.get()
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    label_result.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")

# Create GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

choices = ['rock', 'paper', 'scissors']
var = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Choose: ")
label.grid(row=0, column=0, padx=10)

radio_rock = tk.Radiobutton(frame, text="Rock", variable=var, value='rock')
radio_rock.grid(row=0, column=1)

radio_paper = tk.Radiobutton(frame, text="Paper", variable=var, value='paper')
radio_paper.grid(row=0, column=2)

radio_scissors = tk.Radiobutton(frame, text="Scissors", variable=var, value='scissors')
radio_scissors.grid(row=0, column=3)

btn_play = tk.Button(frame, text="Play", command=play_game)
btn_play.grid(row=1, columnspan=4, pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
