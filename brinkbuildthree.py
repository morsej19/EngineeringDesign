import random as rand
#neckless_gerald = "  o \n /|\ \n / \\"
# o
#/|\
#/ \

bottom=1

def GeraldExtender(neck_size):

    print("  o")
    for i in range(neck_size):
        print("  |")

def GeraldBottom(bottom):
    
    for i in range(bottom):
        print(" \|/")
        print(" / \\")

def GeraldArm(arm_size):

    for i in range(arm_size):
        print("          |")

print("Hello, Gerald has a bizarre disease called Giraffian Neck Syndrome. His neck can grown on command.")
print("How big should his neck be?")

user_neck_size = int(input())
GeraldExtender(user_neck_size)
GeraldBottom(bottom)
#print(user_input)

print("How big should arm be?")

arm_size = int(input())
GeraldExtender(user_neck_size)
GeraldBottom(bottom)
GeraldArm(arm_size)
#print(user_input)

print("Turns out Gerald's arm fell off. Oops.")
print("How many friends should Gerald have?")

gerald_no_friends = int(input())

if gerald_no_friends > 0:
    for i in range(gerald_no_friends):
        friend_neck_size = rand.randint(0,10)
        GeraldExtender(friend_neck_size)
else:
    print("Poor Gerlad!")
