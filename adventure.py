name = input("Greeting Traveller, what is your name? ")
print("Welcome", name + ", To This Adventure!")

answer = input("You are on a dirt road, where would you like to go? (left, right, up, down) ").lower()

if answer == "left":
    print("You have chosen 'left'")
    answer = input("Now you are at a River. Walk around, or swim through? (type 'walk' or 'swim')")
    if answer == "walk":
        print("You walked aroun the river")
    elif answer == "swim":
        print("You swam through the river")
    else:
        print("Please pick a VALID option!")

elif answer == "right":
    print("You have chosen 'right'")
    answer = input("Now you are at a canyon. Walk around, or jump over? (type 'walk' or 'jump')")
    if answer == "walk":
        print("You walked around the canyon")
    elif answer == "jump":
        print("You jumped over the canyon")
    else:
        print("Please pick a VALID option!")

elif answer == "up":
    print("You have chosen 'up'")
    answer = input("Now you are at a mountain. Walk around, or climb over? (type 'walk' or 'climb')")
    if answer == "walk":
        print("You walked around the mountain")
    elif answer == "climb":
        print("You climbed over the mountain")
    else:
        print("Please pick a VALID option!")

elif answer == "down":
    print("You have chosen 'down'")
    answer = input("Now you are at a field. Walk around, or trek through? (type 'walk' or 'trek')")
    if answer == "walk":
        print("You walked around the field")
    elif answer == "trek":
        print("You trekked through the field")
    else:
        print("Please pick a VALID option!")

else:
    print("Please pick a VALID option!")

print("Thanks for playing",name + "!")