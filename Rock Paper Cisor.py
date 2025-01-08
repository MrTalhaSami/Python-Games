import random

computer = random.choice([0, 1, -1])

userDict = {
    "rock" : 1,
    "paper" :-1,
    "scissors": 0 
}
compDict ={
    1 : "rock",
    -1: "paper",
    0: "scissors"
}
#For Invalid input from user

user = input("Choose your Weapon [Rock, Paper , scissors] : ").lower()
userinput = userDict[user]
if user not in userDict:
    print("Invalid choice! Please select from Rock, Paper, or Scissors.")


print(f"You choose {user}")
print(f"Python is {compDict[computer]}")



if (computer == userinput):
    print("Draw!")
elif(computer!= userinput):
    if (computer == -1 and userinput == 1):
        print ("Python Wins")
    elif (computer == -1 and userinput == 0):
        print ("You Win")
    elif (computer == 1 and userinput == 0):
        print ("Python Wins")
    elif (computer == 1 and userinput == -1):
        print ("You Win")
    elif (computer == 0 and userinput == -1):
        print ("Python Win")
    elif (computer == 0 and userinput == 1):
        print ("You Win")        
else:
    print("Aww Snap!")
    
