import random

def game_pick(self):
    pick = self
    if  pick == 0:
        # Rock
        print("""1
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif pick == 1:
            # Paper
        print("""
            _______
        ---'    ____)____
                    ______)
                    _______)
                  _______)
        ---.__________)
        """)
    elif pick == 2:
            # Scissors
        print("""
            _______
        ---'   ____)____
                  ______)
              __________)
              (____)
        ---.__(___)
        """)
    else:
        print("Invalid choice pick again")
        
user_pick = int(input("what do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
game_pick(user_pick)
print("The cpu picks......")
cpu_pick = random.choice([0,2]) #also could of used random.randint(0,2)
game_pick(cpu_pick)

if user_pick == 0 and cpu_pick == 2:
    print ("You win!")
elif user_pick == 0 and cpu_pick == 1:
    print ("You Lose!")
elif user_pick == 1 and cpu_pick == 0:
    print ("You win!")
elif user_pick == 1 and cpu_pick == 2:
    print ("You Lose!")
elif user_pick == 2 and cpu_pick == 1:
    print ("You win!")
elif user_pick == 2 and cpu_pick == 0:
    print ("You lose!")
else:
    print ("Its a draw play again!!")