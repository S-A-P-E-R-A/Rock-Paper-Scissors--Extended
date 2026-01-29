import os
import time
import random
from game import Game
from player import Player
custom = "false"
confirmation = ["yes", "yea", "y", "yep", "yup", "yeah", "yessir", "yessirree", "sure", "ok", "okay", "ya", "yah", "yuh"]
game = Game()
commentList = []

saves = input("Would you like to continue a previous game?\n\t")
if str.lower(saves) in confirmation:
    game.runSavedGame()
else:
    pass
personal = input("Would you like to make a custom version of the game?\n\t")
if str.lower(personal) in confirmation:
    custom = game.customGame()
else:
    pass

endgame = "Unknown"

RoboNames = [
      "Megatron", "R2D2", "C3PO", "Wall-E", "Spongebob", "10101010010",
      "001101110010101", "Optamous Prime", "Bumblebee", "Megatron", "Megatron",
      "Megatron", "Megatron", "Megatron", "BB8", "T-800", "T-1000", "Ultron", "Baymax", "JARVIS", "RoboCop", "Iron Giant", "Vision", "MegaMan"
  ]#Names for the computer

x = 350
for i in range(200):
    x += random.randint(0, 1)
RoboInfo = {
      "RoboName": random.choice(RoboNames),
      "RoboPoints": 100,
      "RoboGoalPoints": x,
      "RoboBet": 0
  }


mode = []  #Stays blank

print("Welcome lucky or unlucky player, I see that you are ready for a rock, paper, scissors, challenge.\n")
time.sleep(5)
print("The modes you can play are: NORMAL, CARS, COMIC, NINTENDO, BAIT, CUSTOM modes.")
time.sleep(2)
game.color("purple", "i")
gameMode = input("We would like you to select and choose which game mode you would like to play.\n\t")
game.checkMode(gameMode)
game.color("blue")
goalpoints = int(input("Now, the amount you choose will determine how many rounds you play, good luck.\nPlease insert your point Goal (You start with 100 points):\n\t"
    ))
game.color("yellow","u")
Name = input("Now, what is your name?\t")

if goalpoints <= 0:
    print(
        "Uh oh! It looks like you are trying to go into the negative zone…that is not good, please try again."
    )  #Says that they cannot go negative
    goalpoints *= -1
    time.sleep(3)

while goalpoints < 300:
    print(
        "Uh oh! It looks like you have gone too low in your points, you MUST be punished for falsely choosing your ‘goalpoints…’ enjoy the triple trouble"
    )
    time.sleep(4)
    goalpoints = round(goalpoints * 3.5)  #Multiplies the goal points by 3
    time.sleep(2)
rounds = round((goalpoints / 100) * 1.8)

PlayerSettings = {
    "Points": 100,
    "GoalPoints": goalpoints,
    "TotalRounds": rounds,
    "name": Name
}
time.sleep(1.3)
os.system('clear')
game.color("green","b")
time.sleep(2)
xxx = str(input("What is your catchphrase?\n\t"))
    
game.commentList.append(str(xxx))
commentList.append(str(xxx))
player = Player(PlayerSettings["name"], PlayerSettings["Points"], PlayerSettings["GoalPoints"])

bets = []
choices = []
RoboBets = []
RoboChoices = []

save = ["000000"]
save.append(PlayerSettings["name"])
save.append(PlayerSettings["Points"])
save.append(PlayerSettings["GoalPoints"])
save.append(str(bets))
save.append(str(choices))
save.append(str(commentList))
save.append(RoboInfo["RoboName"])
save.append(RoboInfo["RoboPoints"]) 
save.append(RoboInfo["RoboGoalPoints"])
save.append(str(RoboBets))
save.append(str(RoboChoices))
save.append(PlayerSettings["TotalRounds"])
save.append(str(gameMode))
save.append("0")
game.FunMode(save)