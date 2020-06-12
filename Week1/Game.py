import random

randomList = ["rock", "scissors", "paper"]
u = 0
comp = 0
tie = 0
def randomChoise():
    return random.choice(randomList)

while True:
    user = input("input 'rock', 'scissors', 'paper' or 'exit':  ")
    computer = randomChoise()
    if ((user == 'rock' and computer == 'scissors') or (user == "scissors" and computer == "paper") or (user == 'paper' and computer == 'rock')):
        
        u += 1

        print(f'Your choise: {user}\nComputer choice: {computer}')
        print("Human wins!")
        print(f'Games Played: {u + comp + tie}, Human: {u}, Computer: {comp}, Tie: {tie}')
    
    elif ((user == 'rock' and computer == "paper") or (user == 'scissors' and computer == 'rock')or (user == 'paper' and computer == 'scissors')):
        
        comp += 1

        print(f'Your choise: {user}\nComputer choice: {computer}')
        print("Coputer wins!")
        print(f'Games Played: {u + comp + tie}, Human: {u}, Computer: {comp}, Tie: {tie}')
    
    elif ((user == computer)):
        
        tie += 1

        print(f'Your choise: {user}\nComputer choice: {computer}')
        print("Tie!")
        print(f'Games Played: {u + comp + tie}, Human: {u}, Computer: {comp}, Tie: {tie}')

    elif (user == "exit"):
        print("Your choice: Exit\nprint('Exiting program.')")
        break

    else:
        print("Error: Wrong input!")
