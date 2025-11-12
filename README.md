import time
import random

print("Welcome lucky or unlucky player, I see that you are ready for a rock, paper, scissors, challenge.\n")
time.sleep(5)
print("The modes you can play are: NORMAL, [DLC - CARS], [DLC - COMIC], [DLC - NINTENDO], OR [DLC - ???] modes.")
time.sleep(2.3)
print(
    "We would like you to select and choose which game mode you would like to play."
)
print("\tnormal\n")
time.sleep(1.5)
pointvaluegoal = int(input("But first, the amount you choose will determine how many rounds you play, good luck.\nPlease insert your point Goal (You start at 100):\n\t"
    ))
Name = input("Now, what is your name?\t")

PlayerSettings = {
    "Points": 100,
    "GoalPoints": pointvaluegoal,
    "Rounds": round((pointvaluegoal / 100) * 1.85),
    "name": Name
}




def NormalMode(points, goalpoints, rounds, name="MegaMind"):
  print("\n\n")
  print(
      "WARNING: IF YOU ARE ASKED FOR A NUMBER, PUT A WHOLE NUMBER, AND NOTHING ELSE"
  )  #will remove for anti-buggy edition
  NormalOptions = ["rock", "paper", "scissors"]
  #Used so stRings can print duRing production

  time.sleep(3)
  RoboNames = [
      "Megatron", "R2D2", "[DLC]", "[DLC]", "10101010010",
      "001101110010101", "[DLC]", "Bumblebee", "Megatron", "Megatron",
      "Megatron", "[DLC]", "Megatron", "[DLC]", "[DLC]"
  ]
  RoboInfo = {
      "RoboName": random.choice(RoboNames),
      "RoboPoints": 100,
      "RoboGoalPoints": 300,
      "RoboBet": 0
  }
  for i in range(700):
    RobGoal = random.randint(1, 4)
    if RobGoal != 3:
      RoboInfo["RoboGoalPoints"] += 1
  print(
      '\nYou have selected "normal mode," meaning that you will be playing the basic old game of rock, paper, scissors'
  )
  time.sleep(4)
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
    goalpoints *= 3  #Multiplies the goal points by 3
    print("It looks like you have a new goalpoint, lets’ see what it is...")
    time.sleep(2)
  rounds = round(
      (goalpoints / 100) * 1.8)  # Can change to make rounds longer\shorter

  #Rounds so it cannot be endless
  rounds += 1
  while (points > 0) and (points < goalpoints) and (rounds > 0):
    RoboInfo["RoboBet"] = 0
    rounds -= 1
    time.sleep(2)
    print("\n\n")
    print(f"This is what your current points, {points}, looks like")
    time.sleep(2.5)
    print(f"Your goal is {goalpoints}, try not to go down")
    time.sleep(2.5)
    print(f"{RoboInfo['RoboName']} has {RoboInfo['RoboPoints']}.")
    time.sleep(2.5)
    print(
        f"It looks like you have been playing for {-(rounds-(round((goalpoints / 100) * 1.8)))} round(s), you have {rounds} round(s) left"
    )
    time.sleep(3)
    robo = random.choice(NormalOptions)
    for i in range(RoboInfo["RoboPoints"]):
      chance = random.randint(1, 2)
      if chance == 1:
        RoboInfo["RoboBet"] += 1
    bet = int(input("Lets’ make this game a bit more interesting, are you willing to win or lose money? Lets’ start betting…insert money.\n\t"))
    if bet > points:
      print(
          "Woah, woah, woah, you are full of yourself, lets not bet too much of our money now, you don’t even have enough money to save yourself from going into debt"
      )
      time.sleep(5)
      continue
    elif bet == points:
      confirmation = input(
          "Gaspsiess, are you sure you want to bet THAT MUCH money? I am only going to ask you this once…don’t make me repeat myself.\n\t"
      )
      if str.lower(confirmation) == "yes":
        print(
            "Ok, let’s see if you can win or lose, good luck, don’t go bankrupt"
        )
        time.sleep(2.3)
      elif str.lower(confirmation) == "no":
        print(
            "Ok, you don’t want to risk losing all of your money? What a noob, go ahead and continue playing"
        )
        time.sleep(3)
        continue
      else:
        print(
            "Oopsies, it looks like you missclicked, we automatically assume this error you have made means no…try to use your spelling skills correctly hehe"
        )
        time.sleep(4.4)
        continue
    elif bet <= 0:
      print(
          "Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game"
      )
      time.sleep(5)
      continue
    points -= bet
    RoboInfo["RoboPoints"] -= RoboInfo["RoboBet"]
    RPS = input("Insert your liking: rock, paper, or scissors\n\t")
    time.sleep(1.5)
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("[DLC]")
    time.sleep(1)
    print("\n\n")
    time.sleep(3)
    print(
        f"{RoboInfo['RoboName']} chose {RoboInfo['RoboPoints]}.")  #Says what the computer chose
    time.sleep(2)
    print(f"{RoboInfo['RoboName']} bet [DLC] points.")
    time.sleep(4)
    if str.lower(RPS) == robo:
      print(
          f"Well, well, well, it looks like we have two lucky players, {PlayerSettings['name']} and {RoboInfo['RoboName']}. Both of your pointvalues will go back"
      )
      points += bet
      RoboInfo["RoboPoints"] += RoboInfo["RoboBet"]
      time.sleep(3)
      continue
    elif (str.lower(RPS) == "rock" and robo == "scissors") or (
        str.lower(RPS) == "scissors"
        and robo == "paper") or (str.lower(RPS) == "paper" and robo == "rock"):
      print(
          "Okay, okay, no need to brag about this victory, get your double pointvalue and get out of here. You are indeed, one lucky duck"
      )
      points += (bet * 2)
      time.sleep(3)
      continue
    elif (str.lower(RPS) == "rock" and robo == "paper") or (
        str.lower(RPS) == "paper"
        and robo == "scissors") or (str.lower(RPS) == "scissors"
                                    and robo == "rock"):
      print(
          "HAHAH, you must have lost all of your luck, according to my calculations, you have lost points…"
      )
      RoboInfo["RoboPoints"] += (RoboInfo["RoboBet"] * 2)
      time.sleep(3)
      continue
    else:
      print(
          f"Uh, oh. It looks like you entered {RPS}, which is not an option in this gamemode"
      )
      time.sleep(3)
      points += bet
      RoboInfo["RoboPoints"] += RoboInfo["RoboBet"]
      continue
  else:
    if (points <= 0) or (rounds == 0):
      print(
          f"Yikes, {name} you are not doing so well, you have lost to {RoboInfo['RoboName']}…Buy the DLC for $179.99?"
      )
      time.sleep(3)
      exit()
    elif RoboInfo["RoboGoalPoints"] <= RoboInfo["RoboPoints"]:
      print("HAHAH it looks like you lost…to a robot, what a loser."
            )  # Says that the computer has won
      time.sleep(3)
      exit()
    elif points >= goalpoints:
      print(f"{name}, good job, you [DLC]!")
      time.sleep(3)
      exit()
    elif RoboInfo["RoboPoints"] <= 0:
      print("Phew, what a game, it looks like you have won…[DLC]!"
            )  #Says that the computer has lost
      time.sleep(3)
      exit()

NormalMode(PlayerSettings["Points"], PlayerSettings["GoalPoints"], PlayerSettings["Rounds"], PlayerSettings["name"])
