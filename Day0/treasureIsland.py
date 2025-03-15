print('''  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re at a crossroad, where do you want to go? Type "left" or "right":').lower()

if choice1 == "left":
    choice2=input ('You\'ve come to a lake. There is an island in '
                    'the middle of the lake. Type "wait" or "swim":').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. \nThere is a house with 3 doors. One red,\n one yellow and one blue.\n'
        'which color do you choose?').lower()
        if choice3 == "red":
            print("Room has spikes...GAME OVER")
        elif choice3 == "yellow":
            print("YOU HAVE FOUND THE TREASURE... YOU WIN!!!")
        elif choice3 == "blue":
            print("Room has fire...Youve been cooked...GAME OVER.")
        else:
            print("You chose a door that doesn't exist. GAME OVER....")
    else:
        print("You've been eaten by the Loch ness monster")

else:
    print("You fell into a pit of snakes...GAMEOVER")

#if you want to use an apostrophe in a print statement you need to use a \ ie: You\'re 