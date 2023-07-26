import random

user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit: ").lower()
    if user_input == "q":
        break
        #exits while loop

    if user_input not in options:
        continue
        #none of the statment below will run
        #continue will make the program go back to the start of loop

    random_num = random.randint(0,2)
    #rock: 0, paper: 1, scissor: 2
    comp_pick = options[random_num]
    print("Computer picked", comp_pick + ".")

    if user_input == 'rock' and comp_pick == 'scissor':
        print("you won!")
        user_wins += 1
    elif user_input == 'paper' and comp_pick == 'rock':
        print("you won!")
        user_wins += 1
    elif user_input == 'scissor' and comp_pick == 'paper':
        print("you won!")
        user_wins += 1
    else:
        print("you lost!")
        comp_wins += 1


print("You won", user_wins, "times, and the computer won", comp_wins, "times.")
print("Goodbye!")
