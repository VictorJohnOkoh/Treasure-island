print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice
first_choice = input("You're at a crossroad, what direction do you want to take? Enter left or right. ")
first_choice = first_choice.lower()

while first_choice != "left" and first_choice != "right":
    first_choice = input("Enter left or right. ")
if first_choice == "right":
    second_choice = input("You have spotted the entrance to a dungeon across the lake, do you swim across or find another way? Enter swim or wait. ")
    # Second choice
    second_choice = second_choice.lower()
    while second_choice != "swim" and second_choice != "wait":
        second_choice = input("Enter swim or wait. ")
    if second_choice == "swim":
        third_choice = input("You see a glimmer underwater do you dive or keep swimming towards the dungeon? Enter dive or swim. ")
        # Third choice
        third_choice = third_choice.lower()
        while third_choice != "dive" and third_choice != "swim":
            third_choice = input("Enter dive or swim. ")
        if third_choice == "dive":
            fourth_choice = input("You find a shipwreck with three trapdoors, do you enter the red, green or blue trapdoor? Enter red, green or blue. ")
            # Fourth choice
            fourth_choice = fourth_choice.lower()
            while fourth_choice != "red" and fourth_choice != "green" and fourth_choice != "blue":
                fourth_choice = input("Enter red, green or blue. ")
            if fourth_choice == "red":
                print("A spike shot through your head and ended your pathetic life.")
            elif fourth_choice == "green":
                print("A black hole appeared and sucked you into the afterlife")
            else:
                print("You Win.\nGame Over.")
        else:
            print("You were eaten by a shark.\nGame Over.")
    else:
        print("You were ambushed by bandits and died.\nGame Over.")
else:
    print("You were met with bandits and killed.\nGame Over.")





