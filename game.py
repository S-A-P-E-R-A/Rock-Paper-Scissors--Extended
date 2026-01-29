from opponent import Opp
from player import Player
import os
import random
import time
import ast
class Game():
  def __init__(self):
      self.rounds = 0
      self.commentList = []
      self.totalRounds = 0
      self.pastGame = False
      self.pin = 0
      self.mode = "none"
      self.player = Player("MegaMind", 0, 0)
      self.opponent = Opp("Haltmann", 0, 400)
      self.confirmation = ["yes", "yea", "y", "yep", "yup", "yeah", "yessir", "yessirree", "sure", "ok", "okay", "ya", "yah", "yuh"]
      self.bait = [
          "mickey mouse", "hulk", "jake the dog", "spider man", 'donald duck', 'daffy duck', 'wood pickaxe', 'netherite pickaxe', 'java', 'python', 'shopping cart', 'corvette', 'trash can', "batman", "tung tung tung sahour", "golden knight", "rey skywalker", "voldemort", "super man", "kryptonite", "dirt", "diamonds", "pneumonoultramicroscopicsilicovolcanoconiosis", "doctor strange", "bombadiro krokadiro", "lockheed martin f-35 lightning", "apple", 'gold bar'
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
          "batman with planning time", "superman","joker", "spiderman",
          "cyborg", "iron man", "green lanter", "alfred", "happy",
          "bruce banner", "hulk", "bruce wayne", "tony stark",
          "infinity gauntlet"
      ]
      self.norm = ["scissors", "paper", "rock"]
      
  def getMode(self, choice):
    choice = str.lower(choice)
    if choice == "bait\n" or choice == "bait":
        return self.bait
    elif choice == "cars\n" or choice == "cars":
        return self.car
    elif choice == "nintendo\n" or choice == "nintendo":
        return self.nintendo
    elif choice == "comic\n" or choice == "comic":
        return self.comic
    elif choice == "normal\n" or choice == "normal":
        return self.norm
    elif choice == "custom\n" or choice == "custom":
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
       file.write(f"\n\nPlayer: {save['name']}")
       file.write(f"\nOpponent: {save['RoboName']}")
       file.write(f"\nMeans of end: {endgame}")
       file.write(f"\n{save['name']} got {save['points']} points out of {save['goalpoints']}")
       file.write(f"\n{save['name']} chose: {self.player.choiceHistory}") 
       file.write(f"\n{save['name']} bet: {self.player.betHistory}")
       file.write(f"\n{save['RoboName']} got {save['RoboPoints']} points out of {save['RoboGoalPoints']}")
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
      pin = []
      while True:
         if x < 6 and not self.pastGame:
             pin.append(random.randint(0, 9))
             x += 1
             continue
         try:
             file = open("saveFile.txt", "a")
             break
         except FileNotFoundError:
             file = open("saveFile.txt", "w")
             file.write("SAVES")
             file.close()
             continue
      if self.pastGame:
          pin = save["pin"]    
      save["comments"] = self.commentList   
      file.write(f"\n\n{pin}")
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
          self.establishCommentList = ast.literal_eval(saveList[6])
          roundReset = False
          save = {"name" : saveList[1], "points" : int(saveList[2]), "goalpoints" : int(saveList[3]), "bets" : saveList[4], "choices" : saveList[5], "comments" : saveList[6], "RoboName" : saveList[7], "RoboPoints" : int(saveList[8]), "RoboGoalPoints" : int(saveList[9]), "RoboBets" : saveList[10], "RoboChoices" : saveList[11], "totalRounds" : saveList[12], "mode" : saveList[13], "roundsPlayed" : int(saveList[14])}
          os.system('clear')
          Ring = {}
          print("In this mode, you need to choose a character that you think will beat / is better than the computer’s choice.")
          time.sleep(4)
          mode = self.getMode(str.lower(save["mode"]))
          for i in range(len(mode)):
            Ring[mode[i]] = i
          time.sleep(1)
          self.color("green", "i")
          print(
              f"Welcome, it looks like you have {save['mode']} mode...good luck, you will indeed need it."
          )  #Welcome Player to the mode they chose
          time.sleep(5)
          self.color("red", "b")
          #Rounds so it cannot be endless
          print(f"{save['RoboName']} is your opponent, they have {save['RoboPoints']} points")
          time.sleep(4)
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
          while (int(save["points"]) > 0) and (int(save["points"]) < int(save["goalpoints"])) and (save['roundsPlayed'] < int(self.totalRounds) - 1) and (int(save["RoboGoalPoints"]) > int(save["RoboPoints"])) and (int(save["RoboPoints"]) > 0):
            save['roundsPlayed'] += 1
            for i in range(len(mode)):
              Ring[mode[i]] = i
                
            self.color("green")
            time.sleep(2)
            os.system('clear')
            if save['roundsPlayed'] != 1 and not roundReset:
                self.update(save['roundsPlayed'], save["points"], save["RoboPoints"], bet, choice, oBet, robo)
                
                menu = input("Would you like to access the game menu?\n\t")
                if str.lower(menu) in self.confirmation:
                    save["bets"] = self.player.betHistory
                    save["choices"] = self.player.choiceHistory
                    save["RoboBets"] = self.opponent.betHistory
                    save["RoboChoices"] = self.opponent.choiceHistory
                    self.menu(save)
            roundReset = False
            oBet = 0
            print("GAME SAVED")
            time.sleep(2)
            os.system('clear')
            self.color("blue","u")
            print(f"Round {save['roundsPlayed']}\nYour Points: {save['points']}\n{save['RoboName']}'s Points: {save['RoboPoints']}\nYour Goal: {save['goalpoints']}\n{save['RoboName']}'s Goal: {save['RoboGoalPoints']}")
            print(f"It looks like you have been playing for {save['roundsPlayed']} round(s), you have {int(self.totalRounds) - save['roundsPlayed']} round(s) left")
            time.sleep(3)
            robo = random.choice(list(Ring.keys()))
            oBet += 1
            for i in range(save["RoboPoints"]):
              chance = random.randint(1, 2)
              if chance == 1:
                oBet += 1
            self.color("purple","i")
            bet = input("Lets’ make this game a bit more interesting, are you willing to win or lose money? Lets’ start betting…insert money.\n\t")
            try:
                bet = int(bet)
                if bet > save["points"]:
                    self.color("red")
                    print(
                  "Woah, woah, woah, you are full of yourself, lets not bet too much of our money now, you don’t even have enough money to save yourself from going into debt"
              )
                    time.sleep(5)
                    save['roundsPlayed'] -= 1
                    roundReset = True
                    continue
                elif bet == save["points"]:
                    self.color("gray","b")
                    confirmation = input(
                  "Gaspsiess, are you sure you want to bet THAT MUCH money? I am only going to ask you this once…don’t make me repeat myself.\n\t"
              )
                    if str.lower(confirmation) in self.confirmation:
                        print(
                    "Ok, let’s see if you can win or lose, good luck, don’t go bankrupt"
                )
                        time.sleep(3)
                    elif str.lower(confirmation) == "no":
                        print(
                    "Ok, you don’t want to risk losing all of your money? What a noob, go ahead and continue playing"
                )
                        time.sleep(3)
                        save['roundsPlayed'] -= 1
                        roundReset = True
                        continue
                    else:
                        self.color("red")
                        print("Typo Detected:\n\tGit Gud")
                        time.sleep(1)
                        save['roundsPlayed'] -= 1
                        roundReset = True
                        continue
                elif bet <= 0:
                    print(
                  "Welp, this is awkward. Why would you try to bet…nothing? HAHAHAHA, go ahead and bet on something, you cannot play like a baby in this game"
              )
                    time.sleep(5)
                    save['roundsPlayed'] -= 1
                    roundReset = True
                    continue
            except ValueError:
                print("Typo Detected:\n\tGit Gud")
                time.sleep(1)
                save['roundsPlayed'] -= 1
                roundReset = True
                continue
            time.sleep(2)
            os.system('clear')
            save["points"] -= bet
            save["RoboPoints"] -= oBet
            self.color("yellow","i")
            print("Here is a list of all choices:\n"
                  )  # Says here are options
            random_options = random.sample(list(Ring.keys()), len(Ring))
            for i, option in enumerate(random_options):
              print(f"{i + 1} -\t{option}\n")
              time.sleep(0.6)
            time.sleep(2)
            self.color("red", "b")
            print("\t|\n\t|\n\t|\n\t|\n\t|")
            time.sleep(1.4)
            self.color("gray", "u")
            if "rock" in mode:
                print(f"{save['RoboName']} chose {robo}.")  #Says what the computer chose
                time.sleep(2)
            print(f"{save['RoboName']} bet {oBet} points.")
            time.sleep(3)
            self.color("blue", "b")
            choice = input("What do you think will beat/is better than your opponent:\t")
            time.sleep(3)
            if str.lower(choice) not in Ring:
              self.color("red", "b")
              print("Typo Detected:\n\tGit Gud")
              save['roundsPlayed'] -= 1
              save["points"] += bet
              save["RoboPoints"] += oBet
              save["points"] -= round(bet / 10)
              time.sleep(2)
              roundReset = True
              continue
            elif (Ring[str.lower(choice)] - Ring[robo] == -1) or (Ring[str.lower(choice)] - Ring[robo] == len(Ring) - 1):
              self.color("green", "i")
              print(
                  "Wow, wow, wow, it looks like we have a lucky duck. Congrats on winning the round!"
              )
              save["points"] += (bet * 2) + oBet
              time.sleep(3)
              continue
            elif (Ring[str.lower(choice)] - Ring[robo] == 1) or (Ring[str.lower(choice)] - Ring[robo] == -(len(Ring) - 1)):
              self.color("red", "i")
              print(
                  "Whoopsies, it looks like you lost your winning streak, if you had one HAHA. We know how unlucky you are, try again…"
              )  #Says that the player has lost
              save["RoboPoints"] += (oBet * 2) + bet
              time.sleep(3)
              self.color("red", "b")
              self.opponent.insult(save["name"], choice, robo)
              time.sleep(3)
              continue
            else:
                self.color("gray", "b")
                print(f"Fool! Between {choice} and {robo}, there is no winner, they are objectivly and completly equal! Choose better!")
                save["points"] += bet
                save["RoboPoints"] += oBet
                time.sleep(5)
                save["points"] -= round(bet / 10)
                print("You have been penalized 10% of your bet for such stupidity")
                self.color("red", "b")
                self.opponent.insult(save["name"], choice, robo)
                time.sleep(3)
                continue
          else:
            self.update(save['roundsPlayed'], save["points"], save["RoboPoints"], bet, choice, oBet, robo)
            if (save["points"] <= 0):
              self.color("gray", "b")
              print(
                  f"Yikes, {save['name']} you are not doing so well, you have lost to {save['RoboName']}…try again?"
              )
              time.sleep(3)
              endgame = "Bankruptcy" # says they went bankrupt - IS A SHORT DESCRIPTION
              self.creatEntry(save, endgame)
            elif (save['roundsPlayed'] > int(self.totalRounds) - 1):
                print("You have ran out of time, you have lost") #says they ran out of time
                endgame = "Ran out of Time" #says they ran out of time - IS A SHORT DESCRIPTION
                self.creatEntry(save, endgame)
                exit()
            elif save["RoboGoalPoints"] <= save["RoboPoints"]:
              self.color("red", "u")
              endgame = f"{save['RoboName']} reached their goal" #ENDGAME variable is a brief description of how the game ended
              print("It looks like the computer has won, try again noob!"
                    )  # Says that the computer has won
              self.creatEntry(save, endgame)
              time.sleep(3)
              exit()
            elif save["points"] >= save["goalpoints"]:
              self.color("green", "b")
              endgame = f"{save['name']} reached their goal"
              print(f"{save['name']}, good job, you have won!")
              self.creatEntry(save, endgame)
              time.sleep(3)
              exit()
            elif save["RoboPoints"] <= 0:
              self.color("blue", "u")
              endgame = f"{save['RoboName']} Bankruptcy"
              print("Let’s go, the noob is finally improving, great job.")
              self.creatEntry(save, endgame)
              time.sleep(3)
              exit()

  def runSavedGame(self):
    try:
        file = open("saveFile.txt", "r")
    except FileNotFoundError:
        file = open("saveFile.txt", "w")
        file.write("SAVES")
        file.close()
        print("No saved games found")
        time.sleep(2)
        return
    print(file.read())
    while True:
        try:
            pin = input("\nEnter the pin for the game\t(The Pin is found at the top of a game and include [] and ,)\n\t - ")
            pin = pin + "\n"
            with open('saveFile.txt', 'r') as file:
                for i in file:
                    if pin == i:
                        break
                else:
                    print(f"Game {pin} not found.")
                    continue
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
    save = []
    var = False
    with open('saveFile.txt', 'r') as file:
        for i in file:
            if pin == i:
                var = True
            if i != "~~~~~~~~~~" and var:
                save.append(i)
            elif i == "~~~~~~~~~~":
                break
    self.pastGame = True
    self.FunMode(save)

  def menu(self, save):
      self.color("yellow", "i")
      print("\n\nWelcom to the game menu!")
      choice = input("What would you like to do?\n\tView your stats: 'stats'\n\tView your past games: 'past'\n\tView your opponent: 'opp'\n\tAdd a comment: 'comment'\n\tView game progression: 'game'\n\tView entire game: 'full'\n\tSave and quit: 'save'\n\tEnd the game: 'end'\n")
      print("\n")
      if str.lower(choice) == "stats":
          print(self.player)
      elif str.lower(choice) == "past":
          self.viewPast()
      elif str.lower(choice) == "opp":
          print(self.opponent)
      elif str.lower(choice) == "comment":
          self.comment()
      elif str.lower(choice) == "game":
          print(self)
      elif str.lower(choice) == "save":
          
          self.createSave(save)
      elif str.lower(choice) == "end":
          self.endGame(save)
      elif str.lower(choice) == "full":
          self.fullGame()
      else:
          print("Typo Detected:\n\tGit Gud")
      time.sleep(4)
      goBack = input("\nWould you like to return to the game?\n\t")
      if str.lower(goBack) in self.confirmation:
          return
      self.menu(save)

  def update(self, rounds, gamePoints, gameOpPoints, pBet, pChoice, oBet, oChoice):
      self.rounds = rounds
      self.player.update(gamePoints, pBet, pChoice)
      self.opponent.update(gameOpPoints, oBet, oChoice)

  def setTotalRounds(self, rounds):
      self.totalRounds = rounds

  def checkMode(self, mode):
      if str.lower(mode) != "normal" and str.lower(mode) != "bait" and str.lower(mode) != "nintendo" and str.lower(mode) != "cars" and str.lower(mode) != "comic" and str.lower(mode) != "custom":
          print("Typo Detected:\n\tGit Gud")
          time.sleep(2)
          exit()
      else:
          self.mode = mode

  def endGame(self, save):
      self.color("red")
      self.ask = input("Are you sure you want to end the game?\n\t")
      if str.lower(self.ask) in self.confirmation:
          self.creatEntry(save, "quit")  
          exit()
      time.sleep(2)

  def viewPast(self):
      self.color("blue", "u")
      look = input("Would you like to see past games?    ('yes' or 'no')\n\t")
      if str.lower(look) in self.confirmation:
          try:
              file = open("Realm.txt", "r")
              print(file.read())
          except FileNotFoundError:
              print("There are no past games")

  def comment(self):
      comment = input("What would you like to say?\n\t")
      print("Comment added")
      self.commentList.append(comment)
    
  def color(self, color="reset", format="none"):
      return #Remove to add color
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

  def establishCommentList(self, comments):
      self.commentList = comments

  def customGame(self):
      custom = []
      print("Welcome to the custom game creator!")
      time.sleep(2)
      print("You will be able to create your own game mode, and save it to a file!")
      time.sleep(3)
      print("WHEN TOLD, simply type in anything you want")
      time.sleep(2)
      print("Every subsequent input is inferior to the previous one, with the last input beating the first!")
      time.sleep(3.2)
      print("Simply type 'i am finished' when you are done\n")
      time.sleep(1.7)
      while True:
           choice = input("What would you like to add?\n\t")
           choice = str.lower(choice)
           if str.lower(choice) == "i am finished":
               break
           elif choice in custom:
               print("You already have that choice, dummy!")
               time.sleep(2)
               continue
           elif choice == " " or choice == "":
               print("You cannot have a blank choice, dingo!")
               time.sleep(2)
               continue
           choice = choice.replace(" ", "_")
           custom.append(choice)
      print("\nDoes this look good?  'yes' or 'no'")
      sep = " \nwhich is better than "
      print(sep.join(custom))
      x = input("\t")
      if x == 'no':
          print("Oops. Well Bye")
          exit()
      else:
          nam = input("\nWhats its name?\n\t")
          nam = str.lower(nam)
          self.modeZone(custom, "push", nam)


  def modeZone(self, mode, what, name):
      self.color("green", "i")
      while True:
          try:
               file = open("modes.txt", "a+")
          except FileNotFoundError:
               file = open("modes.txt", "w")
               file.write("MODES")
               file.close()
               continue
          break
      if what == "pull":
         self.getMode(mode)
      elif what == "push":
         sep = " "
         custom = sep.join(mode)
         file.write(f"\n\n{name}\n")
         file.write(f"{custom}")
         print("Mode added")
         return
      elif what == "custom":
         print("Here are your custom modes")
         try:
              file = open("modes.txt", "r")
              print(file.read())
              file.close()
         except FileNotFoundError:
              print("There are no custom modes")
              exit()
         print("\n\n  Game modes 'normal', 'cars', 'comic', 'nintendo' and 'bait' are default modes")
         choice = input("What mode would you like to play?\n\t")
         if choice ==  "normal" or choice == "cars" or choice == "comic" or choice == "nintendo" or choice == "bait" or choice ==  "normal\n" or choice == "cars\n" or choice == "comic\n" or choice == "nintendo\n" or choice == "bait\n":
             print("Why are you here if you want to play a default mode?")
             time.sleep(2)
             return self.getMode(choice)
         else:
              var = False
              with open('modes.txt', 'r') as file:
                  for i in file:
                      if choice == i.strip():
                          var = True
                      elif var:
                          string = i
                          break
                  else:
                      print(f"Mode {choice} not found.")
                      exit()
                  return string.split()