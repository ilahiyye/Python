import random

randomList = ["rock", "scissors", "paper"]
u = 0
comp = 0
def randomChoise():
    return random.shoise(randomList)

while True:
    user = input("input 'rock', 'scissors', 'paper' or 'exit'")
    computer = randomShoise()
    if ((user == 'rock' and computer == 'scissors') or (user == "scissors" and computer == "paper")):
        u = +1
        print("User wins!")
    elif (user == 'rock' and computer == "paper"):
        comp = +1
        print("Coputer wins!")
    elif (user == "exit"):
        break

    else:
        print("Error: Wrong input!")

    print(f'Result: User - {u} : Computer - {comp}')

    


