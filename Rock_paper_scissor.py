import random
import time
choice = str(input("""Make your choice. Rock or Paper or scissor """)).lower()

choices = ["Rock", "Paper", "scissor"]

bot_choice = random.choice(choices).lower()
if bot_choice == choice:
    print("Bot making move....")
    time.sleep(4)
    print(print(f"I was {bot_choice}"))
    print("It's a tie.")


elif bot_choice == "rock" and choice == "scissor" or bot_choice == "scissor" and choice == "paper" or bot_choice == "paper" and choice == "paper":
    print("Bot making move....")
    time.sleep(4)
    print(print(f"I was {bot_choice}"))
    print("You lost.")

elif bot_choice == "scissor" and choice == "rock" or bot_choice == "paper" and choice == "scissor" or bot_choice == "rock" and choice == "paper":
    print(print(f"I was {bot_choice}"))
    print("You won.")

else:
    print("I don't get it.")