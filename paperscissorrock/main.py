import random
import time
import os

def rock() -> str:

    os.system("say Rock!")

    return """
    
      <@@@>
     <@@@@@@>   
    <@@@@@@@@>   
   <@@ #ROCK# @@>  
    <@@@@@@@@>
     <@@@@@@>
      <@@@>
    
    """

def scissors() -> str:

    os.system("say Scissors!")

    return """

          @@@@   @@@@        
          @@@@@ @@@@@         
           @@@@@@@@@          
            @@@@@@@           
             @   @            
        *@  @@@@@@@  @*       
     @@@@@@@@@@ @@@@@@@@@@    
    @@@     @@   @@     @@@   
     @@@@@@@@@   @@@@@@@@@
    
           #SCISSORS#
    
    """

def paper() -> str:

    os.system("say Paper!")
    return """

    @@@@@@@@@@@@@@
    @            @@
    @            @@@
    @            @@@
    @   #PAPER#  @@@
    @            @@@
    @@@@@@@@@@@@@@@@
    """

def play(player: int, ai: int):

    if player == ai:
        print("Almost close, no one wins!")
        os.system("say Almost close, no one wins!")
    if player == 1 and ai == 3:
        print("Paper power!!! You Win!!")
        os.system("say Paper power!!! You Win!!")
    elif player == 1 and ai == 2:
        print("Computer cut you in pieces!! You Lose!!")
        os.system("say Computer cut you in pieces!! You Lose!!")
    elif player == 2 and ai == 1:
        print("You cut him in pieces! you win!")
        os.system("say You cut him in pieces! you win!")
    elif player == 2 and ai == 3:
        print("The computer smash you down!!!")
        os.system("say The computer smash you down!!!")
    elif player == 3 and ai == 1:
        print("The computer has strangled you!!!")
        os.system("say The computer has strangled you!!!")
    elif player == 3 and ai == 2:
        print("You have smashed those scissors!!")
        os.system("say You have smashed those scissors!!")
    


def player_select() -> int:
    player_selection = 0
    while player_selection <=0 or player_selection > 3:
        try:
            player_selection = int(input("Select:  1 for paper, 2 for scissors, 3 for rock > "))
        except:
            player_selection = 0
    
    os.system("say You choose")
    print(f"you choose: {toWord(player_selection)}")
    
    return player_selection

def computer_select() -> int:
    computer_selection = random.randint(1,3)
    os.system("say Computer choose")
    print(f"the computer choose {toWord(computer_selection)}")
    return computer_selection


def toWord(i) -> str:
    if i == 1:
        return paper()
    elif i == 2:
        return scissors()
    elif i == 3:
        return rock()
    else:
        return "unkown"

def waitSeconds(seconds) -> None:
    pixel = "*"
    print("")
    print("...")

    for i in range(0,seconds  + 1):
        print(pixel * i)
        time.sleep(1)

    print("")

print("Welcome to paper, scissors and rock!")
print('*' * 50)


player = player_select()

print("Computer is playing ... ")
waitSeconds(1)

computer = computer_select()

waitSeconds(2)

play(player, computer)

input("Press enter to end")
    