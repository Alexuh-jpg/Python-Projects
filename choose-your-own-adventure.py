name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("There is a fork in the road. Do you go LEFT or RIGHT? ").lower()

if answer == "left":
    answer = input("There is a river. Do you SWIM or WALK around? ").lower()

    if answer == "swim":
        print("You swam across and got eaten by a shark! You lose.")
    elif answer == "walk":
        print("You walked around the river but got lost! You lose.")
    else:
        print("Not a vaild option you lose!")

elif answer == "right":
    answer = input("There is a wobbly bridge. Do you CROSS it or go BACK? ").lower()

    if answer == "cross":
        print("You went across the wobbly bridge and found a candybar! You win.")
    elif answer == "back":
        print("You went back and got lost! You lose.")
    else:
        print("Not a vaild option you lose!")
else:
    print("Not a vaild option you lose!")

