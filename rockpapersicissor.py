import random
choices=["rock","paper","sicissor"]
# #user enters the input from rock , paper , sicissor 
a=input("enter your choice : ").lower() 
# it takes any random choice  
b=random.choice(choices)
print(f"your choice = {a}")
print(f"python_choice = {b}")
# checks the condition and gives the result as follows 
if a==b:
    print("it's a tie")
elif a=="paper" and b=="rock":
    print("you have won the game")
elif a=="rock" and b=="sicissor":
    print("you have won the game")
elif a=="sicissor" and b=="paper":
    print("you have won the game")
else:
    print("python won the game")

