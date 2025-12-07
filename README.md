import os
import time
import random

comments = []

endgame = "Unknown"
look = input("Would you like to see past games?    (yes or no)\n\t")
if str.lower(look) == "yes":
    try:
        file = open("Realm.txt", "r")
        print(file.read())
        exit()
    except FileNotFoundError:
        print("There are no past games")
        exit()
def color(color="reset", format="none"):
  print(" ")  #remove for color
  pass  #remove for color
  """  remove for color
  print("\033[0m")
  if str.lower(color) == "yellow":
    print("\033[33m")

  elif str.lower(color) == "reset":
    print("\033[0m")

  elif str.lower(color) == "red":
    print("\033[31m")
  elif str.lower(color) == "green":
    print("\033[32m")
  elif str.lower(color) == "blue":
    print("\033[36m")
  elif str.lower(color) == "purple":
    print("\033[35m")
  elif str.lower(color) == "gray":
    print("\033[30m")
  else:
    print("\033[0m")
  if str.lower(format) == "b":  #Bold
    print("\033[1m")
  elif str.lower(format) == "i":  #Italic
    print("\033[3m")
  elif str.lower(format) == "u":  #Underline
    print("\033[4m")
  elif str.lower(format) == "none":
    pass
  else:
    print("\033[0m")
"""  #remove for color
    
bait = [
    "mickey mouse", "hulk", "jake the dog", "spider man", 'donald duck', 'daffy duck', 'wood pickaxe', 'netherite pickaxe', 'java', 'python', 'shopping cart', 'corvette', 'trash can', "batman", "tung tung tung sahour", "golden knight", "rey skywalker", "voldemort", "super man", "kryptonite", "dirt", "diamonds", "pneumonoultramicroscopicsilicovolcanoconiosis", "doctor strange", "bombadiro krokadiro", "lockheed martin f-35 lightning", "apple", 'gold bar'
]
car = [
    "gtr nismo 2020", "dodge charger", "f150", "silverado", "dodge viper",
    "jeep gladiator", "batmobile", "ferrari roma", "ferrari 488",
    "rolls royce phantom", "aston martin valkyrie", "dodge challenger",
    "lamborghini huracan", "chevrolet camaro zl1 1le 2018", "laferrari"
]
nintendo = [
    "kirby", "mario", "bowser", "peach", "todd the toad", "luigi", "king boo",
    "garchop", "samus aran", "link", "waddle dee", "red", "yoshi",
    "Hiroshi Yamauchi"
]
comic = [
    "Batman with Planning time", "superman","joker", "spiderman",
    "cyborg", "iron man", "green lanter", "alfred", "happy",
    "bruce banner", "hulk", "bruce wayne", "tony stark",
    "infinity gauntlet"
]

mode = []  #Stays blank

print("Welcome lucky or unlucky player, I see that you are ready for a rock, paper, scissors, challenge.\n")
time.sleep(5)
print("The modes you can play are: NORMAL, CARS, COMIC, NINTENDO, OR BAIT modes.")
time.sleep(2.3)
color("purple", "i")
gameMode = input(
    "We would like you to select and choose which game mode you would like to play.\n\t"
)
color("blue")
pointvaluegoal = int(input("Now, the amount you choose will determine how many rounds you play, good luck.\nPlease insert your point Goal (You start at 100):\n\t"
    ))
color("yellow","u")
Name = input("Now, what is your name?\t")

PlayerSettings = {
    "Points": 100,
    "GoalPoints": pointvaluegoal,
    "Rounds": round((pointvaluegoal / 100) * 1.85),
    "name": Name
}
color("green","b")
print("LOADING:\nFun Fact! You can make a comment at any time you can input a value!\n")
time.sleep(5)




def Comment(comment):
    choice = input("ERROR DETECTED:\n\tis that a typo or a comment?\n\t")
    if str.lower(choice) == "comment":
        print("Okay, we'll keep note of it") #Says they will note the comment
        comments.append(comment)
    elif str.lower(choice) == "typo":
        print("You need to practice you english.") #Acknowledges the typo
    else:
        print(f"...What is '{choice}' supposed to mean?")#Says something mean (nothing else happens)
    time.sleep(2)
    print("now RESTART!")# Says it will restart
    time.sleep(2)

        
def CreatEntry(goalpoints, points, robot, robgoal, rounds, robpoints, endgame, comments, gameMode):
    while True:
        try: 
            file = open("Realm.txt", "a")
            break
        except FileNotFoundError:
            file = open("Realm.txt", "w")
            file.write("REALM OF FORMER WARRIORS")
            file.close()
            continue
    file.write(f"\n\nPlayer: {Name}")
    file.write(f"\nOpponent: {robot}")
    file.write(f"\nMeans of end: {endgame}")
    file.write(f"\n{Name} got {points} points out of {goalpoints}")
    file.write(f"\n{robot} got {robpoints} points out of {robgoal}")
    file.write(f"\nRounds played: {rounds}")
    file.write(f"\nGame Mode: {gameMode}")
    var = 1
    for i in comments:
        file.write(f"\nComment {var}: \n\t{i}")
        var += 1
    print("\n\n\n")
        






def NormalMode(points, goalpoints, rounds, name="MegaMind"):
  os.system('clear')
  NormalOptions = ["rock", "paper", "scissors"]
  #Used so stRings can print duRing production
  # To insert variables, add an f"" before the quotation marks and put the variable in {curly brackets}

  time.sleep(3)
  RoboNames = [
      "Megatron", "R2D2", "C3PO", "Wall-E", "Spongebob", "10101010010",
      "001101110010101", "Optamous Prime", "Bumblebee", "Megatron", "Megatron",
      "Megatron", "Megatron", "Megatron", "Megatron", "Megatron"
  ]
  RoboInfo = {
      "RoboName": random.choice(RoboNames),
      "RoboPoints": 100,
      "RoboGoalPoints": 300,
      "RoboBet": 0
  }
  for i in range(400):
    RobGoal = random.randint(1, 3)
    if RobGoal == 3:
      RoboInfo["RoboGoalPoints"] += 1
  color("green", "i")
  print(
      '\nYou have selected "normal mode," meaning that you will be playing the basic old game of rock, paper, scissors'
  )
  time.sleep(4)
  color("red", "b")
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
    goalpoints += 300  #Multiplies the goal points by 3
    time.sleep(2)
  rounds = round(
      (goalpoints / 100) * 1.8)  # Can change to make rounds longer/shorter

  #Rounds so it cannot be endless
  rounds += 1
  while (points > 0) and (points < goalpoints) and (rounds > 1):
    color("blue","u")
    RoboInfo["RoboBet"] = 0
    rounds -= 1
    time.sleep(2)
    os.system('clear')
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
    color("purple","i")
    bet = input("Lets’ make this game a bit more interesting, are you willing to win or lose money? Lets’ start betting…insert money.\n\t")
    try:
        bet = int(bet)
        if bet > points:
            color("red")
            print(
          "Woah, woah, woah, you are full of yourself, lets not bet too much of our money now, you don’t even have enough money to save yourself from going into debt"
      )
            time.sleep(5)
            continue
        elif bet == points:
            color("gray","b")
            confirmation = input("Gaspsiess, are you sure you want to bet THAT MUCH money? I am only going to ask you this once…don’t make me repeat myself.\n\t")
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
                color("red")
                Comment(confirmation)
                time.sleep(1)
                rounds += 1
                continue
        elif bet <= 0:
            color("red")
            print(
          "Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game"
      )
            time.sleep(5)
            continue
    except ValueError:
        Comment(bet)
        time.sleep(2)
        rounds += 1
        continue
    points -= bet
    RoboInfo["RoboPoints"] -= RoboInfo["RoboBet"]
    color("yellow","b")
    RPS = input("Insert your liking: rock, paper, or scissors\n\t")
    time.sleep(1.5)
    color("green")
    print("Rock")
    color("blue")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    color("gray")
    print("Scissors")
    time.sleep(1)
    color("red")
    print("Shoot...")
    time.sleep(1)
    os.system('clear')
    time.sleep(3)
    color("purple","u")
    print(
        f"{RoboInfo['RoboName']} chose {robo}.")  #Says what the computer chose
    time.sleep(2)
    print(f"{RoboInfo['RoboName']} bet {RoboInfo['RoboBet']} points.")
    time.sleep(4)
    color("blue","b")
    if str.lower(RPS) == robo:
      color("yellow")
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
      color("green", "i")
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
      color("red", "i")
      print(
          "HAHAH, you must have lost all of your luck, according to my calculations, you have lost points…"
      )
      RoboInfo["RoboPoints"] += (RoboInfo["RoboBet"] * 2)
      time.sleep(3)
      continue
    else:
      color("red", "b")
      Comment(RPS)
      points += bet
      RoboInfo["RoboPoints"] += RoboInfo["RoboBet"]
      rounds += 1
      continue

  else:
    if (points <= 0) or (rounds == 0):
      color("gray", "b")
      print(
          f"Yikes, {name} you are not doing so well, you have lost to {RoboInfo['RoboName']}…try again?"
      )
      time.sleep(3)
      if points <= 0:
        endgame = "Bankruptcy" # says they went bankrupt
        CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      elif rounds == 0:
        endgame = "Ran out of Time" #says they ran out of time
        CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      exit()
    elif RoboInfo["RoboGoalPoints"] <= RoboInfo["RoboPoints"]:
      color("red", "u")
      endgame = f"{RoboInfo['RoboName']} reached their goal"
      print("HAHAH it looks like you lost…to a robot, what a loser."
            )  # Says that the computer has won
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()
    elif points >= goalpoints:
      color("green", "b")
      endgame = f"{PlayerSettings['name']} reached their goal"
      print(f"{name}, good job, you have won!")
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()
    elif RoboInfo["RoboPoints"] <= 0:
      color("blue", "u")
      endgame = f"{RoboInfo['RoboName']} Bankruptcy"
      print("Phew, what a game, it looks like you have won…Congrats!"
            )  #Says that the computer has lost
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()









def FunMode(points, goalpoints, rounds, ModeName, mode, name="MegaMind"):
  os.system('clear')
  Ring = {}
  print("In this mode, you need to choose a character that you think will beat / is better than the computer’s choice.")
  time.sleep(5)
  for i in range(len(mode)):
    Ring[mode[i]] = i
  time.sleep(1)
  RoboNames = [
      "Megatron", "R2D2", "C3PO", "Wall-E", "Spongebob", "10101010010",
      "001101110010101", "Optamous Prime", "Bumblebee", "Megatron", "Megatron",
      "Megatron", "Megatron", "Megatron"
  ]
  RoboInfo = {
      "RoboName": random.choice(RoboNames),
      "RoboPoints": 100,
      "RoboGoalPoints": 400,
      "RoboBet": 0
  }
  for i in range(300):
    RobGoal = random.randint(1, 3)
    if RobGoal == 3:
      RoboInfo["RoboGoalPoints"] += 1
  color("green", "i")
  print(
      f"Welcome, it looks like you have {ModeName} mode...good luck, you will indeed need it."
  )  #Welcome Player to the mode they chose
  time.sleep(5)
  color("red", "b")
  if goalpoints <= 0:
    print(
        "It looks like you are trying to go into the negatives. I thought that you knew better, come on noob. You CANNOT go into the negatives."
    )
    goalpoints *= -1
    time.sleep(3)
  if goalpoints < 400:
    print(f"Uh oh! It looks like {goalpoints} is too low in for a goal, you MUST be punished for falsely choosing your ‘goalpoints…’ enjoy the MEGA TROUBLE")
    time.sleep(6)
    while goalpoints < 350:
        goalpoints *= 4  #Multiplies the goal points by 4
  rounds = round(
      (goalpoints / 100) * 1.8)  # Can change to make rounds longer/shorter

  #Rounds so it cannot be endless
  rounds += 1
  print(f"{RoboInfo['RoboName']} is your opponent, they have {RoboInfo['RoboPoints']} points")
  time.sleep(4)

  while (points > 0) and (points < goalpoints) and (rounds > 1) and (
      RoboInfo["RoboGoalPoints"]
      > RoboInfo["RoboPoints"]) and (RoboInfo["RoboPoints"] > 0):
    for i in range(len(mode)):
      Ring[mode[i]] = i
    RoboInfo["RoboBet"] = 0
    rounds -= 1
    time.sleep(2)
    os.system('clear')
    color("blue","u")
    print(f"This is what your current points, {points}, looks like")
    time.sleep(2.5)
    print(f"Your goal is {goalpoints}, try not to go down")
    time.sleep(2.5)
    print(f"It looks like you have been playing for {-(rounds-(round((goalpoints / 100) * 1.8)))} round(s), you have {rounds} round(s) left")
    print(f"{RoboInfo['RoboName']} has {RoboInfo['RoboPoints']} points")
    time.sleep(3)
    robo = random.choice(list(Ring.keys()))
    for i in range(RoboInfo["RoboPoints"]):
      chance = random.randint(1, 2)
      if chance == 1:
        RoboInfo["RoboBet"] += 1
    color("purple","i")
    bet = input("Lets’ make this game a bit more interesting, are you willing to win or lose money? Lets’ start betting…insert money.\n\t")
    try:
        bet = int(bet)
        if bet > points:
            color("red")
            print(
          "Woah, woah, woah, you are full of yourself, lets not bet too much of our money now, you don’t even have enough money to save yourself from going into debt"
      )
            time.sleep(5)
            rounds += 1
            continue
        elif bet == points:
            color("gray","b")
            confirmation = input(
          "Gaspsiess, are you sure you want to bet THAT MUCH money? I am only going to ask you this once…don’t make me repeat myself.\n\t"
      )
            if str.lower(confirmation) == "yes":
                print(
            "Ok, let’s see if you can win or lose, good luck, don’t go bankrupt"
        )
                time.sleep(3)
            elif str.lower(confirmation) == "no":
                print(
            "Ok, you don’t want to risk losing all of your money? What a noob, go ahead and continue playing"
        )
                time.sleep(3)
                rounds += 1
                continue
            else:
                color("red")
                Comment(confirmation)
                time.sleep(1)
                rounds += 1
                continue
        elif bet <= 0:
            print(
          "Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game"
      )
            time.sleep(5)
            rounds += 1
            continue
    except ValueError:
        Comment(bet)
        time.sleep(1)
        rounds += 1
        continue
    time.sleep(2)
    os.system('clear')
    points -= bet
    RoboInfo["RoboPoints"] -= RoboInfo["RoboBet"]
    color("yellow","u")
    print("Here is a list of all choices:\n"
          )  # Says here are options
    random_options = random.sample(list(Ring.keys()), len(Ring))
    for i, option in enumerate(random_options):
      print(f"{i + 1} -\t{option}\n")
      time.sleep(1)
    time.sleep(3)
    color("red", "b")
    print("\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|")
    time.sleep(3)
    color("gray", "u")
    print(
        f"{RoboInfo['RoboName']} chose {robo}.")  #Says what the computer chose
    time.sleep(2)
    print(f"{RoboInfo['RoboName']} bet {RoboInfo['RoboBet']} points.")
    time.sleep(3)
    color("blue", "b")
    choice = input("What do you think will beat/is better than your opponent:\t")
    time.sleep(3)
    if str.lower(choice) not in Ring:
      color("red", "b")
      Comment(choice)
      rounds += 1
      points += bet
      RoboInfo["RoboPoints"] += RoboInfo["RoboBet"]
      points -= round(bet / 10)
      time.sleep(2)
      continue
    elif (Ring[str.lower(choice)] - Ring[robo] == -1) or (Ring[str.lower(choice)] - Ring[robo] == len(Ring) - 1):
      color("green", "i")
      print(
          "Wow, wow, wow, it looks like we have a lucky duck. Congrats on winning the round!"
      )
      points += (bet * 2)
      time.sleep(3)
      continue
    elif (Ring[str.lower(choice)] - Ring[robo] == 1) or (Ring[str.lower(choice)] - Ring[robo] == -(len(Ring) - 1)):
      color("red", "i")
      print(
          "Whoopsies, it looks like you lost your winning streak, if you had one HAHA. We know how unlucky you are, try again…"
      )  #Says that the player has lost
      RoboInfo["RoboPoints"] += (RoboInfo["RoboBet"] * 2)
      time.sleep(3)
      continue
    else:
        color("gray", "b")
        print(f"Fool! Between {choice} and {robo}, there is no winner, they are objectivly and completly equal! Choose better!")
        points += bet
        RoboInfo["RoboPoints"] += RoboInfo["RoboBet"]
        time.sleep(5)
        points -= round(bet / 10)
        print("You have been penalized 10% of your bet for such stupidity")
        time.sleep(3)
        continue
  else:
    if (points <= 0) or (rounds == 0):
      color("gray", "b")
      print(
          f"Yikes, {name} you are not doing so well, you have lost to {RoboInfo['RoboName']}…try again?"
      )
      time.sleep(3)
      if points <= 0:
          endgame = "Bankruptcy" # says they went bankrupt
          CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      elif rounds == 0:
        endgame = "Ran out of Time" #says they ran out of time
        CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      exit()
    elif RoboInfo["RoboGoalPoints"] <= RoboInfo["RoboPoints"]:
      color("red", "u")
      endgame = f"{RoboInfo['RoboName']} reached their goal"
      print("It looks like the computer has won, try again noob!"
            )  # Says that the computer has won
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()
    elif points >= goalpoints:
      color("green", "b")
      endgame = f"{PlayerSettings['name']} reached their goal"
      print(f"{name}, good job, you have won!")
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()
    elif RoboInfo["RoboPoints"] <= 0:
      color("blue", "u")
      endgame = f"{RoboInfo['RoboName']} Bankruptcy"
      print("Let’s go, the noob is finally improving, great job.")
      CreatEntry(goalpoints, points, RoboInfo["RoboName"], RoboInfo["RoboGoalPoints"], -(rounds-(round((goalpoints / 100) * 1.8))), RoboInfo["RoboPoints"], endgame, comments, gameMode)
      time.sleep(3)
      exit()


if str.lower(gameMode) == "normal":
  NormalMode(PlayerSettings["Points"], PlayerSettings["GoalPoints"],
             PlayerSettings["Rounds"], PlayerSettings["name"])
elif str.lower(gameMode) == "cars":
  for a in car:
    mode.append(a)
elif str.lower(gameMode) == "comic":
  for b in comic:
    mode.append(b)
elif str.lower(gameMode) == "nintendo":
  for c in nintendo:
    mode.append(c)
elif str.lower(gameMode) == "bait":
  for d in bait:
    mode.append(d)
else:
  color("red")
  print(
      "Uh oh, it looks like you have entered an option that is not available, please try again!"
  )  #Says that is not an option and now we restart
  time.sleep(3)
  exit()
FunMode(PlayerSettings["Points"], PlayerSettings["GoalPoints"],
        PlayerSettings["Rounds"], gameMode, mode, PlayerSettings["name"])
