#RULES
#0 is rock
#1 is paper
#2 is scissor
import random
user=int(input("enter value 0 is rock,1 is paper,2 is scissor:"))
computer=random.randint(0,2)
print(f"computer choice:={computer}")
if user==computer:
    print("game was draw")
elif user== 2 and computer==0:
    print("computer win")
elif user==0 and computer==2:
    print("user wins")
elif user>=3 or user<0:
    print("you enter wrong value")
elif user > computer:
    print("user wins")
elif computer > user:
    print("computer wins")