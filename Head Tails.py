import random
user_choice = input("Make Choice : ")
user_input = int(input("Select Any Number : "))
choices = ["Heads","Tails"]

def gen_rnd_no(start, end):
    return random.randint(start,end)

computer_gen_No = gen_rnd_no(1,5)


if user_choice not in choices:
    print("Exception Error: Select Correct Choice")
else: 
    print (f"Python Select {computer_gen_No}")

    results = user_input + computer_gen_No
    if results%2 == 0:
        res1 = "Heads"
        print(f"Result is {res1}")
        if res1 == user_choice :
            print("You Win")
        else:
            print("Python Wins")
    else:
        res2 = "Tails"
        print(f"Result is {res2}")
        if res2 == user_choice:
            print ("You Win")
        else: 
            print("Python wins")
    