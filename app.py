#Thanks to Claud AI for helping with the code and to David C. Lovelace for deciding the dynamic game connections
import random
from flask import Flask, render_template, request
import os
APP = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))
chance = False
P2 = False
THEMODE = None
dynamic = False


class Game():
  def __init__(self):
      self.rounds = 0
      self.commentList = []
      self.totalRounds = 0

      self.gameList = ["NORMAL", "CARS", "COMIC", "NINTENDO", "BAIT", "POKEMON", "BIG BANG", "RPS-7", "RPS-9", "RPS-11", "RPS-15", "RPS-25", "RPS-101", "CUSTOM"]

      self.poke = False
      self.chance = True
      self.pastGame = False 
      self.dynamic = False
      self.pin = 0
      self.dynamics = {}
      self.mode = "none"
      #self.player = Player("MegaMind", 0, 0)
      #self.opponent = Opp("Haltmann", 0, 400)
      #self.pics = Pics()
      #self.pics.setGame(self)
      self.confirmation = ["yes", "yea", "y", "yep", "yup", "yeah", "yessir", "yessirree", "sure", "ok", "okay", "ya", "yah", "yuh"]
      self.bait = [
          "mickey mouse", "hulk", "jake the dog", "spiderman", 'donald duck', 'daffy duck', 'wood pickaxe', 'netherite pickaxe', 'java', 'python', 'shopping cart', 'corvette', 'trash can', "batman", "tung tung tung sahour", "golden knight", "rey skywalker", "voldemort", "superman", "kryptonite", "dirt", "diamonds", "pneumonoultramicroscopicsilicovolcanoconiosis", "doctor strange", "bombadiro krokadiro", "lockheed martin f-35 lightning", "apple", 'gold bar'
      ]
      self.car = [
          "gtr nismo 2020", "dodge charger", "f150", "silverado", "dodge viper",
          "jeep gladiator", "batmobile", "ferrari roma", "ferrari 488",
          "rolls royce phantom", "aston martin valkyrie", "dodge challenger",
          "lamborghini huracan", "chevrolet camaro zl1 1le 2018", "laferrari"
      ]
      self.nintendo = [
          "kirby", "mario", "bowser", "peach", "todd the toad", "luigi", "king boo",
          "garchomp", "samus aran", "link", "waddle dee", "red", "yoshi",
          "hiroshi yamauchi"
      ]
      self.comic = [
          "batman", "superman","joker", "spiderman",
          "cyborg", "ironman", "green lantern", "alfred", "happy",
          "bruce banner", "hulk", "bruce wayne", "tony stark",
          "infinity gauntlet"
      ]
      self.norm = ["scissors", "paper", "rock"]

      self.RPSLS = ["rock", "paper", "scissors", "lizard", "spock"] #ADDITION

      self.pokemon = ["fire", "water", "electricity", "grass", "dragon", "fairy", "rock", "ground", "ice", "steel", "dark", "ghost", "fighting", "bug", "flying", "poison", "psychic"]

#Special thanks to David C. Lovelace on https://www.umop.com/rps.htm for deciding the dynamic game connections as seen below

      self.RPS7 = ["rock", "fire", "scissors", "sponge", "paper", "air", "water"]

      self.RPS9 = ["rock", "fire", "scissors", "human", "sponge", "paper", "air", "water", "gun"]
      
      self.RPS11 = ["rock", "fire", "scissors", "human", "wolf", "sponge", "paper", "air", "water", "devil", "gun"]

      self.RPS15 = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning", "gun"]

      
      self.RPS25 = ["rock", "sun", "fire", "scissors", "axe", "snake", "monkey", "woman", "man", "tree", "cockroach", "wolf", "sponge", "paper", "moon", "air", "bowl", "water", "spock", "dragon", "devil", "lightning", "nuke", "dynamite", "gun"]

      self.RPS101 = ["dynamite", "tornado", "quicksand", "pit", "chain", "gun", "law", "whip", "sword",
    "rock", "death", "wall", "sun", "camera", "fire", "chainsaw", "school", "scissors",
    "poison", "cage", "axe", "peace", "computer", "castle", "snake", "blood",
    "porcupine", "vulture", "monkey", "king", "queen", "prince", "princess", "police",
    "woman", "baby", "man", "home", "train", "car", "noise", "bicycle", "tree",
    "turnip", "duck", "wolf", "cat", "bird", "fish", "spider", "cockroach", "brain",
    "community", "cross", "money", "vampire", "sponge", "church", "butter", "book",
    "paper", "cloud", "airplane", "moon", "grass", "film", "toilet", "air", "planet",
    "guitar", "bowl", "cup", "beer", "rain", "water", "tv", "rainbow", "ufo", "spock",
    "prayer", "mountain", "satan", "dragon", "diamond", "platinum", "gold", "devil",
    "fence", "video game", "math", "robot", "heart", "electricity", "lightning",
    "medusa", "power", "laser", "nuke", "sky", "tank", "helicopter"
]
  def pokeCheck(self, player, robo):
    try:
        if player in self.dynamics[robo]:
            return 1
        elif robo in self.dynamics[player]:
            return -1
        else:
          print(f"Fool! Between {player} and {robo}, there is no winner, they are objectivly and completly equal! Choose better!")
          return 0
    except Exception as e:
        print("ERROWER ERREOR")
        print(e)
        exit()

  def rpsDictionary(self, items):
    size = len(items)
    numLosses = int(len(items) / 2) # Each item loses to 50 items
    theDictionary = {}
    for i, move in enumerate(items):
        # Finds the 50 items preceding the current move, wrapping around
        losers = [items[(i - j) % size] for j in range(1, numLosses + 1)]
        theDictionary[move] = losers
    return theDictionary


  def getMode(self, choice):
    choice = str.upper(choice)
    if choice == "BAIT\n" or choice == "BAIT":
        return self.bait
    elif choice == "CARS\n" or choice == "CARS":
        return self.car
    elif choice == "NINTENDO\n" or choice == "NINTENDO":
        return self.nintendo
    elif choice == "COMIC\n" or choice == "COMIC":
        return self.comic
    elif choice == "NORMAL\n" or choice == "NORMAL":
        return self.norm
    elif choice == "POKEMON\n" or choice == "POKEMON":
        self.dynamic = True
        self.dynamics = {"fire" : ["water"], "water" : ["grass", "electricity", "poison"], "electricity" : ["ground"], "grass" : ["steel", "fire", "ice", "poison", "bug"], "dragon" : ["ice", "steel", "fairy", "dragon"], "fairy" : ["ghost", "fighting", "steel"], "rock" : ["water", "fighting", "ground", "steel"], "ground" : ["flying", "water", "grass", "ice"], "ice" : ["fire", "rock", "steel"], "steel" : ["electricity", "poison", "fighting"], "dark" : ["fighting", "bug", "fairy"], "ghost" : ["dark", "ghost"], "fighting" : ["fairy", "psychic", "flying"], "bug" : ["rock", "flying", "fire"], "flying" : ["rock", "ice", "electricity"], "poison" : ["ground", "psychic"], "psychic" : ["dark", "ghost", "bug"]}
        return self.pokemon
    elif choice == "BIG BANG" or choice == "BIG BANG\n": #ADDITION
        self.dynamic = True
        self.dynamics = {"rock" : ["paper", "spock"], "paper" : ["scissors", "lizard"], "scissors" : ["rock", "spock"], "lizard" : ["scissors", "rock"], "spock" : ["lizard", "paper"]}
        return self.RPSLS
    elif choice == "RPS-7":
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS7)
        return self.RPS7
    elif choice == "RPS-9":
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS9)
        return self.RPS9
    elif choice == "RPS-11":
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS11)
        return self.RPS11
    elif choice == "RPS-15":
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS15)
        return self.RPS15
    elif choice == "RPS-25":
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS25)
        return self.RPS25
    elif choice == "RPS-101":
        #self.pics.big = True
        self.dynamic = True
        self.dynamics = self.rpsDictionary(self.RPS101)
        return self.RPS101
    elif choice == "CUSTOM\n" or choice == "CUSTOM":
        return self.modeZone("hi", "custom", "hi")
    else:
        print("ERROR WITH INPUT - TERMINATING PROGRAM")
        print(choice)
        exit()

  def __str__(self):
      return f"Rounds: {int(self.totalRounds)}\nIn Round: {self.rounds}\nMode: {self.mode}"

  def fullGame(self):
       print(self.player)
       print(self.opponent)
       print(self)

  def creatEntry(self, save, endgame):
       while True:
           try: 
               file = open("Realm.txt", "a")
               break
           except FileNotFoundError:
               file = open("Realm.txt", "w")
               file.write("REALM OF FORMER WARRIORS")
               file.close()
               continue
           except PermissionError:
               print("You do not have permission, get it in the terminal.\n Simply put 'cd ~'")
               exit()
       file.write(f"\n\nPlayer: {save['name']}")
       file.write(f"\nOpponent: {save['RoboName']}")
       file.write(f"\nMeans of end: {endgame}")
       file.write(f"\n{save['name']} got {save['Quacks']} Quacks out of {save['goalQuacks']}")
       file.write(f"\n{save['name']} chose: {self.player.choiceHistory}") 
       file.write(f"\n{save['name']} bet: {self.player.betHistory}")
       file.write(f"\n{save['RoboName']} got {save['RoboQuacks']} Quacks out of {save['RoboGoalQuacks']}")
       file.write(f"\n{save['RoboName']} chose: {self.opponent.choiceHistory}")
       file.write(f"\n{save['RoboName']} bet: {self.opponent.betHistory}")
       file.write(f"\nRounds played: {self.rounds}")
       file.write(f"\nGame Mode: {self.mode}")
       var = 1
       for i in self.commentList:
           file.write(f"\nComment {var}: \n\t{i}")
           var += 1
       file.close()
       print("\n\nGAME DOCUMENTED\n")

  def createSave(self, save):
      x = 0
      while True:
         try:
             file = open("saveFile.txt", "a")
             break
         except FileNotFoundError:
             file = open("saveFile.txt", "w")
             file.write("SAVES")
             file.close()
             continue
         except PermissionError:
             print("You do not have permission, get it in the terminal.\n Simply put 'cd ~'")
             exit()
      save["comments"] = self.commentList   
      file.write("\n\n")
      for i in save:
          file.write(f"\n{save[i]}")
      file.write("\n~~~~~~~~~~")
      file.close()
      print("\n\nGAME SAVED\n")
      exit()

  def FunMode(self, saveList):
          self.player.setName(saveList[1], saveList[3], saveList[4], saveList[5])
          self.opponent.setName(saveList[7], saveList[9], saveList[10], saveList[11])
          self.setTotalRounds(saveList[12])
          self.mode = saveList[13]
          P2 = False
          #self.establishCommentList = ast.literal_eval(saveList[6])
          roundReset = False
          save = {"pin" : saveList[0], "name" : saveList[1], "Quacks" : int(saveList[2]), "goalQuacks" : int(saveList[3]), "bets" : saveList[4], "choices" : saveList[5], "comments" : saveList[6], "RoboName" : saveList[7], "RoboQuacks" : int(saveList[8]), "RoboGoalQuacks" : int(saveList[9]), "RoboBets" : saveList[10], "RoboChoices" : saveList[11], "totalRounds" : saveList[12], "mode" : saveList[13], "roundsPlayed" : int(saveList[14])}
          print("\n\n")
          #self.pics.globalSave = save
          pTwo = input("Would you like to do 2 player mode?\n\t")
          if pTwo.lower() in self.confirmation:
            nam = input("What is p2's name?\t")
            #self.pics2 = Pics()
            save["RoboName"] = nam
            P2 = True


          Ring = {}
          chan = input("Would you like the game to be a game of chance?\n(If not, you will know your opponents move)\n\t")  #ADDITION
          if chan.lower() in self.confirmation:
              self.chance = False
          print("In this mode, you need to choose a character that you think will beat / is better than the computer’s choice.")
          #time.sleep(4)
          mode = self.getMode(str.lower(save["mode"]))
          for i in range(len(mode)):
            Ring[mode[i]] = i
          #time.sleep(1)
          self.color("green", "i")
          print(
              f"Welcome, it looks like you have {save['mode']} mode...good luck, you will indeed need it."
          )  #Welcome Player to the mode they chose
          #time.sleep(5)
          self.color("red", "b")
          #Rounds so it cannot be endless
          print(f"{save['RoboName']} is your opponent, they have {save['RoboQuacks']} Quacks")
          #time.sleep(4)
          if not self.pastGame:
              bet = 0
              oBet = 0
              robo = "none"
              choice = "none"
          else:
              bet = self.player.betHistory[-1]
              oBet = self.opponent.betHistory[-1]
              robo = self.opponent.choiceHistory[-1]
              choice = self.player.choiceHistory[-1]
          while (int(save["Quacks"]) > 0) and (int(save["Quacks"]) < int(save["goalQuacks"])) and (save['roundsPlayed'] < int(self.totalRounds) - 1) and (int(save["RoboGoalQuacks"]) > int(save["RoboQuacks"])) and (int(save["RoboQuacks"]) > 0):
            save['roundsPlayed'] += 1
            #self.pics.globalSave = save
            for i in range(len(mode)):
              Ring[mode[i]] = i

            self.color("green")
            
            print("\n")
            if save['roundsPlayed'] != 1 and not self.pastGame:
                self.update(save['roundsPlayed'], save["Quacks"], save["RoboQuacks"], bet, choice, oBet, robo)
                save["bets"] = self.player.betHistory
                save["choices"] = self.player.choiceHistory
                save["RoboBets"] = self.opponent.betHistory
                save["RoboChoices"] = self.opponent.choiceHistory
            self.pastGame = False
            roundReset = False
            oBet = 0
            print("GAME SAVED")
            #time.sleep(1)
            print("\n\n")
            self.color("blue","u")
            while save['Quacks'] % 5 != 0:
                save['Quacks'] += 1
            print(f"Round {save['roundsPlayed']}\nYour Quacks: {save['Quacks']}\n{save['RoboName']}'s Quacks: {save['RoboQuacks']}\nYour Goal: {save['goalQuacks']}\n{save['RoboName']}'s Goal: {save['RoboGoalQuacks']}")
            print(f"It looks like you have been playing for {save['roundsPlayed']} round(s), you have {int(self.totalRounds) - save['roundsPlayed']} round(s) left")
            #time.sleep(3)
            robo = random.choice(list(Ring.keys()))
            if not P2:
                oBet += 1
                for i in range(save["RoboQuacks"]):
                  chance = random.randint(1, 2)
                  if chance == 1:
                    oBet += 1
            self.color("purple","i")
            print(f"Lets’ make this game a bit more interesting, is {save['name']} willing to win or lose Quacks? Lets’ start betting…insert Quacks.\n\t")
            #time.sleep(2)
            #bet = self.pics.doPoints()
            try:
                bet = int(bet)
                if bet > save["Quacks"]:
                    self.color("red")
                    print(
                  "Woah, woah, woah, you are full of yourself, lets not bet too much of our Quacks now, you don’t even have enough Quacks to save yourself from going into debt"
              )
                    #time.sleep(5)
                    save['roundsPlayed'] -= 1
                    roundReset= True
                    continue
                elif bet == save["Quacks"]:
                    self.color("gray","b")
                    confirmation = input(
                  "Gaspsiess, are you sure you want to bet THAT MUCH Quacks? I am only going to ask you this once…don’t make me repeat myself.\n\t"
              )
                    if str.lower(confirmation) in self.confirmation:
                        print(
                    "Ok, let’s see if you can win or lose, good luck, don’t go bankrupt"
                )
                        #time.sleep(3)
                    elif str.lower(confirmation) == "no":
                        print(
                    "Ok, you don’t want to risk losing all of your Quacks? What a noob, go ahead and continue playing"
                )
                        #time.sleep(3)
                        save['roundsPlayed'] -= 1
                        roundReset= True
                        continue
                    else:
                        self.color("red")
                        print("Typo Detected:\n\tGit Gud")
                        #time.sleep(1)
                        save['roundsPlayed'] -= 1
                        roundReset= True
                        continue
                elif bet <= 0:
                    print(
                  "Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game"
              )
                    #time.sleep(5)
                    save['roundsPlayed'] -= 1
                    roundReset= True
                    continue
            except ValueError:
                print("Typo Detected:\n\tGit Gud")
                #time.sleep(1)
                save['roundsPlayed'] -= 1
                roundReset= True
                continue
            #time.sleep(1)
            if P2:
                print(f"Now its {save['RoboName']}'s turn, how much will you bet?\n\t")
                #time.sleep(2)
                #oBet = self.pics2.doPoints()
                self.opponent.name = save['RoboName']
                try:
                    oBet = int(oBet)
                    if oBet > save["RoboQuacks"]:
                        self.color("red")
                        print(
                  "Woah, woah, woah, you are full of yourself, lets not bet too much of our Quacks now, you don’t even have enough Quacks to save yourself from going into debt"
              )
                        #time.sleep(5)
                        save['roundsPlayed'] -= 1
                        roundReset= True
                        continue
                    elif oBet == save["RoboQuacks"]:
                        self.color("gray","b")
                        confirmation = input(
                  "Gaspsiess, are you sure you want to bet THAT MUCH Quacks? I am only going to ask you this once…don’t make me repeat myself.\n\t"
              )
                        if str.lower(confirmation) in self.confirmation:
                            print(
                    "Ok, let’s see if you can win or lose, good luck, don’t go bankrupt"
                )
                            #time.sleep(3)
                        elif str.lower(confirmation) == "no":
                            print(
                    "Ok, you don’t want to risk losing all of your Quacks? What a noob, go ahead and continue playing"
                )
                            #time.sleep(3)
                            save['roundsPlayed'] -= 1
                            roundReset= True
                            continue
                        else:
                            self.color("red")
                            print("Typo Detected:\n\tGit Gud")
                            #time.sleep(1)
                            save['roundsPlayed'] -= 1
                            roundReset= True
                            continue
                    elif oBet <= 0:
                        print("Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game")
                        #time.sleep(5)
                        save['roundsPlayed'] -= 1
                        roundReset= True
                        continue
                except ValueError:
                    print("Typo Detected:\n\tGit Gud")
                    #time.sleep(1)
                    save['roundsPlayed'] -= 1
                    roundReset= True
                    continue
                print("REMEMBER PLAYER 1, YOU ARE PICKING THE OPTIONS THAT PLAYER 2 MUST BEAT.\nTHE APPONENT PAY ALSO LOOK AWAY IF THEY DESIRE A GUESSING CHALLANGE")
                #time.sleep(3)

            save["Quacks"] -= bet
            save["RoboQuacks"] -= oBet
            self.color("yellow","i")
            self.color("red", "b")
            #time.sleep(1.4)
            self.color("gray", "u")
            if not P2:
                if self.chance:
                    print(f"{save['RoboName']} chose {robo}.")  #Says what the computer chose
                    #time.sleep(2)
                print(f"{save['RoboName']} bet {oBet} Quacks.")
            #time.sleep(3)
            random_options = random.sample(list(Ring.keys()), len(Ring))
            #self.pics.addMenu(random_options)
            self.color("blue", "b")
            #choice = self.pics.pick
            if P2:
                print("Player Two Now!")
                #time.sleep(2)
                random_options = random.sample(list(Ring.keys()), len(Ring))
                #self.pics.addMenu(random_options)
                #trobo = self.pics.pick
            #time.sleep(2)
            winn = 55
            if self.dynamic:
                winn = self.pokeCheck(str.lower(choice), robo)
            if str.lower(choice) not in Ring:
              self.color("red", "b")

              print("Typo Detected:\n\tGit Gud")
              save['roundsPlayed'] -= 1
              save["Quacks"] += bet
              save["RoboQuacks"] += oBet
              save["Quacks"] -= round(bet / 10)
              #time.sleep(2)
              roundReset= True
              continue
            if (Ring[str.lower(choice)] - Ring[robo] == -1) or (Ring[str.lower(choice)] - Ring[robo] == len(Ring) - 1) or (winn == 1):
              self.color("green", "i")
              print(
                  "Wow, wow, wow, it looks like we have a lucky duck. Congrats on winning the round!"
              )
              save["Quacks"] += (bet * 2) + oBet
              #time.sleep(3)
              continue
            elif (Ring[str.lower(choice)] - Ring[robo] == 1) or (Ring[str.lower(choice)] - Ring[robo] == -(len(Ring) - 1)) or (winn == -1):
              self.color("red", "i")
              print(
                  f"Whoopsies, it looks like {save['name']} lost their winning streak, if they had one HAHA. We know how unlucky you are, try again…"
              )  #Says that the player has lost
              save["RoboQuacks"] += (oBet * 2) + bet
              #time.sleep(3)
              self.color("red", "b")
              self.opponent.insult(save["name"], choice, robo)
              #time.sleep(3)
              continue
            else:
                self.color("gray", "b")
                print(f"Fool! Between {choice} and {robo}, there is no winner, they are objectivly and completly equal! \nChoose better!")
                save["Quacks"] += bet
                save["RoboQuacks"] += oBet
                #time.sleep(5)
                save["Quacks"] -= round(bet / 10)
                print("You have been penalized 10% of your bet for such foolishness")
                if P2:
                    print(f"You too {save['RoboName']}!")
                    save["RoboQuacks"] -= round(oBet / 10)
                else:
                    self.color("red", "b")
                    self.opponent.insult(save["name"], choice, robo)
                #time.sleep(3)
                continue
          else:
            self.update(save['roundsPlayed'], save["Quacks"], save["RoboQuacks"], bet, choice, oBet, robo)
            if (save["Quacks"] <= 0):
              self.color("gray", "b")
              print(
                  f"Yikes, {save['name']} you are not doing so well, you have lost to {save['RoboName']}…try again?"
              )
              #time.sleep(3)
              endgame = "Bankruptcy" # says they went bankrupt - IS A SHORT DESCRIPTION
              self.creatEntry(save, endgame)
              exit()
            elif (save['roundsPlayed'] > int(self.totalRounds) - 1):
                print("You have ran out of time, you have lost") #says they ran out of time
                endgame = "Ran out of Time" #says they ran out of time - IS A SHORT DESCRIPTION
                self.creatEntry(save, endgame)
                exit()
            elif save["RoboGoalQuacks"] <= save["RoboQuacks"]:
              self.color("red", "u")
              endgame = f"{save['RoboName']} reached their goal" #ENDGAME variable is a brief description of how the game ended
              print("It looks like the opponent has won, try again noob!"
                    )  # Says that the computer has won
              self.creatEntry(save, endgame)
              #time.sleep(3)
              exit()
            elif save["Quacks"] >= save["goalQuacks"]:
              self.color("green", "b")
              endgame = f"{save['name']} reached their goal"
              print(f"{save['name']}, good job, you have won!")
              self.creatEntry(save, endgame)
              #time.sleep(3)
              exit()
            elif save["RoboQuacks"] <= 0:
              self.color("blue", "u")
              endgame = f"{save['RoboName']} Bankruptcy"
              print("Let’s go, the noob is finally improving, great job.")
              self.creatEntry(save, endgame)
              #time.sleep(3)
              exit()

  def menu(self, save, action):
      #self.color("yellow", "i")
      choice = action
      print("\n\nWelcom to the game menu!")
      print("\n")
      if str.lower(choice) == "stats":
          print(self.player)
      elif str.lower(choice) == "past games":
          self.viewPast()
      elif str.lower(choice) == "opponent info":
          print(self.opponent)
      elif str.lower(choice) == "comment":
          self.comment()
      elif str.lower(choice) == "game info":
          print(self)
      elif str.lower(choice) == "save game":
          self.createSave(save)
      elif str.lower(choice) == "end game":
          self.endGame(save)
      elif str.lower(choice) == "all information":
          self.fullGame()
      else:
          print("Typo Detected:\n\tGit Gud")
      #time.sleep(2)
      goBack = input("\nIs there anything else you would like to do in the menu?\n\t")
      if str.lower(goBack) not in self.confirmation:
          return
      #self.pics.menu()

  def update(self, rounds, gameQuacks, gameOpQuacks, pBet, pChoice, oBet, oChoice):
      self.rounds = rounds
      self.player.update(gameQuacks, pBet, pChoice)
      self.opponent.update(gameOpQuacks, oBet, oChoice)

  def setTotalRounds(self, rounds):
      self.totalRounds = rounds

  def endGame(self, save):
      self.color("red")
      self.ask = input("Are you sure you want to end the game?\n\t")
      if str.lower(self.ask) in self.confirmation:
          #self.pics.clear()  
          self.creatEntry(save, "quit")
          exit()
      #time.sleep(2)

  def viewPast(self):
      self.color("blue", "u")
      look = input("Would you like to see past games?    ('yes' or 'no')\n\t")
      if str.lower(look) in self.confirmation:
          try:
              file = open("Realm.txt", "r")
              print(file.read())
          except FileNotFoundError:
              print("There are no past games")
          except PermissionError:
              print("You do not have permission, get it in the terminal.\n Simply put 'cd ~'")
              exit()

  def comment(self):
      comment = input("What would you like to say?\n\t")
      print("Comment added")
      self.commentList.append(comment)

  def color(self, color="reset", format="none"):
      pass

  def establishCommentList(self, comments):
      self.commentList = comments




bait = [
          "mickey mouse", "hulk", "jake the dog", "spiderman", 'donald duck', 'daffy duck', 'wood pickaxe', 'netherite pickaxe', 'java', 'python', 'shopping cart', 'corvette', 'trash can', "batman", "tung tung tung sahour", "golden knight", "rey skywalker", "voldemort", "superman", "kryptonite", "dirt", "diamonds", "pneumonoultramicroscopicsilicovolcanoconiosis", "doctor strange", "bombadiro krokadiro", "lockheed martin f-35 lightning", "apple", 'gold bar'
      ]
car = [
          "gtr nismo 2020", "dodge charger", "f150", "silverado", "dodge viper",
          "jeep gladiator", "batmobile", "ferrari roma", "ferrari 488",
          "rolls royce phantom", "aston martin valkyrie", "dodge challenger",
          "lamborghini huracan", "chevrolet camaro zl1 1le 2018", "laferrari"
      ]
nintendo = [
          "kirby", "mario", "bowser", "peach", "todd the toad", "luigi", "king boo",
          "garchomp", "samus aran", "link", "waddle dee", "red", "yoshi",
          "hiroshi yamauchi"
      ]
comic = [
          "batman", "superman","joker", "spiderman",
          "cyborg", "ironman", "green lantern", "alfred", "happy",
          "bruce banner", "hulk", "bruce wayne", "tony stark",
          "infinity gauntlet"
      ]
norm = ["scissors", "paper", "rock"]

RPSLS = ["rock", "paper", "scissors", "lizard", "spock"] #ADDITION

pokemon = ["fire", "water", "electricity", "grass", "dragon", "fairy", "rock", "ground", "ice", "steel", "dark", "ghost", "fighting", "bug", "flying", "poison", "psychic"]

#Special thanks to David C. Lovelace on https://www.umop.com/rps.htm for deciding the dynamic game connections as seen below

RPS7 = ["rock", "fire", "scissors", "sponge", "paper", "air", "water"]

RPS9 = ["rock", "fire", "scissors", "human", "sponge", "paper", "air", "water", "gun"]
      
RPS11 = ["rock", "fire", "scissors", "human", "wolf", "sponge", "paper", "air", "water", "devil", "gun"]

RPS15 = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning", "gun"]

      
RPS25 = ["rock", "sun", "fire", "scissors", "axe", "snake", "monkey", "woman", "man", "tree", "cockroach", "wolf", "sponge", "paper", "moon", "air", "bowl", "water", "spock", "dragon", "devil", "lightning", "nuke", "dynamite", "gun"]

RPS101 = ["dynamite", "tornado", "quicksand", "pit", "chain", "gun", "law", "whip", "sword",
    "rock", "death", "wall", "sun", "camera", "fire", "chainsaw", "school", "scissors",
    "poison", "cage", "axe", "peace", "computer", "castle", "snake", "blood",
    "porcupine", "vulture", "monkey", "king", "queen", "prince", "princess", "police",
    "woman", "baby", "man", "home", "train", "car", "noise", "bicycle", "tree",
    "turnip", "duck", "wolf", "cat", "bird", "fish", "spider", "cockroach", "brain",
    "community", "cross", "money", "vampire", "sponge", "church", "butter", "book",
    "paper", "cloud", "airplane", "moon", "grass", "film", "toilet", "air", "planet",
    "guitar", "bowl", "cup", "beer", "rain", "water", "tv", "rainbow", "ufo", "spock",
    "prayer", "mountain", "satan", "dragon", "diamond", "platinum", "gold", "devil",
    "fence", "video game", "math", "robot", "heart", "electricity", "lightning",
    "medusa", "power", "laser", "nuke", "sky", "tank", "helicopter"
]

# This creates the file if it's missing, but doesn't overwrite it if it's there - Gemini
with open('saveFile.txt', 'a') as f:
    pass

#saveFile = os.path.join(APP.root_path, 'static', 'saveFile.txt')

@APP.route('/read-file')
def read_file():
    content = []
    with open('saveFile.txt', 'r') as file:
        for i in file:
            content.append(i)
    String = ""
    for i in content:
        String += i + "\n"
    return render_template("savedGame.html", content=String)

@APP.route("/")
def FirstPage():
    return render_template("FirstPage.html", P2 = P2, chance = chance)

@APP.route("/")
def set_chance():
    global chance
    chance = not chance
    return render_template("FirstPage.html", P2 = P2, chance = chance)

@APP.route("/")
def set_P2():
    global P2
    P2 = not P2
    return render_template("FirstPage.html", P2 = P2, chance = chance)

def checkSave(pin):
    pin = pin + "\n"
    with open('saveFile.txt', 'r') as file:
        for i in file:
            if pin == i:
                break
        else:
            return read_file()
        return True

def rpsDictionary(items):
  size = len(items)
  numLosses = int(len(items) / 2) # Each item loses to 50 items
  theDictionary = {}
  for i, move in enumerate(items):
      # Finds the 50 items preceding the current move, wrapping around
      losers = [items[(i - j) % size] for j in range(1, numLosses + 1)]
      theDictionary[move] = losers
  return theDictionary

@APP.route("/app", methods=["POST"])
def app():
    user_choice = request.form.get("play")
    attack_choice = request.form.get("attack")
    global mode
    mode = request.form.get("mode")
    winn = 5
    if mode:
        global THEMODE
        THEMODE = (mode)
    if attack_choice:
        Ring = {}
        for i in range(len(mode)):
            Ring[mode[i]] = i
        computer = random.choice(eval(mode))
        if mode != "bait" and mode != "car" and mode != "nintendo" and mode != "comic" and mode != "norm":
            dynamics = rpsDictionary(eval(mode))
            if attack_choice in dynamics[computer]:
                winn = 1
            elif computer in dynamics[attack_choice]:
                winn = -1
            else:
              winn = 0
        if (Ring[str.lower(attack_choice)] - Ring[computer] == -1) or (Ring[str.lower(attack_choice)] - Ring[computer] == len(Ring) - 1) or (winn == 1):
          self.color("green", "i")
          print(
                  "Wow, wow, wow, it looks like we have a lucky duck. Congrats on winning the round!"
              )
          save["Quacks"] += (bet * 2) + oBet
          #time.sleep(3)
          
        elif (Ring[str.lower(attack_choice)] - Ring[computer] == 1) or (Ring[str.lower(attack_choice)] - Ring[computer] == -(len(Ring) - 1)) or (winn == -1):
          self.color("red", "i")
          print(
                  f"Whoopsies, it looks like {save['name']} lost their winning streak, if they had one HAHA. We know how unlucky you are, try again…"
              )  #Says that the player has lost
          save["RoboQuacks"] += (oBet * 2) + bet
          #time.sleep(3)
          self.color("red", "b")
          self.opponent.insult(save["name"], attack_choice, computer)
          #time.sleep(3)
          
        else:
            self.color("gray", "b")
            print(f"Fool! Between {attack_choice} and {computer}, there is no winner, they are objectivly and completly equal! \nChoose better!")
            save["Quacks"] += bet
            save["RoboQuacks"] += oBet
            #time.sleep(5)
            save["Quacks"] -= round(bet / 10)
            print("You have been penalized 10% of your bet for such foolishness")
            if P2:
                print(f"You too {save['RoboName']}!")
                save["RoboQuacks"] -= round(oBet / 10)
            #time.sleep(3)
        return render_template("clash.html", P1 = attack_choice, P2 = computer)

        
        
    if user_choice == "game.runSavedGame":
        return read_file()
    elif user_choice == "game.newGame":
        return render_template("mainGame.html")
    elif user_choice == "game.customGame":
        return render_template("customGame.html")
    elif user_choice == "P2":
        return set_P2()
    elif user_choice == "chance":
        return set_chance()
    elif checkSave(user_choice):
        pin = user_choice + "\n"
        save = []
        var = False
        with open('saveFile.txt', 'r') as file:
            for line in file:
                if pin == line or pin == line.strip():
                    var = True
                if (line != "~~~~~~~~~~" and var) or (line.strip() != "~~~~~~~~~~" and var):
                    save.append(line.strip())
                elif (line == "~~~~~~~~~~" or line.strip() == "~~~~~~~~~~") and var:
                    break
        mode = eval(save[13])
        return render_template("mainGame.html", 
                               name=save[1], point=save[2], 
                               goalPoints=save[3], bets=save[4], 
                               picks=save[5], comments=save[6], 
                               roboName=save[7], roboPoints=save[8], 
                               roboGoalPoints=save[9], roboBets=save[10],
                               roboPicks=save[11], totalRounds=save[12],
                               mode=mode,
                               currentRound=save[14])
    else:
        return render_template("FirstPage.html", P2 = P2, chance = user_choice)
if __name__ == "__main__":
    APP.run(debug=True)