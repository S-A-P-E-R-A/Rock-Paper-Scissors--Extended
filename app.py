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
computer = None
player_quacks
opp_quacks

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

RPSLS = ["rock", "paper", "scissors", "lizard", "spock"] 

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

def rpsDictionary2(items):
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
    bet_choice = request.form.get("bet")
    oBet_choice = 1
    for i in range(save["RoboQuacks"]):
         chance = random.randint(1, 2)
         if chance == 1:
             oBet_choice += 1
    winn = 5
    win = 5
    if attack_choice:
        global player_quacks
        global opp_quacks
        Ring = {}
        for i in range(len(THEMODE)):
            Ring[THEMODE[i]] = i
        if THEMODE != "bait" and THEMODE != "car" and THEMODE != "nintendo" and THEMODE != "comic" and THEMODE != "norm":
            dynamics = rpsDictionary2(eval(THEMODE))
            if attack_choice in dynamics[computer]:
                winn = 1
            elif computer in dynamics[attack_choice]:
                winn = -1
            else:
              winn = 0
        if (Ring[str.lower(attack_choice)] - Ring[computer] == -1) or (Ring[str.lower(attack_choice)] - Ring[computer] == len(Ring) - 1) or (winn == 1):
          #self.color("green", "i")
          win = 1
          print(
                  "Wow, wow, wow, it looks like we have a lucky duck. Congrats on winning the round!"
              )
          player_quacks += bet_choice + oBet_choice
          opp_quacks -= oBet_choice
          #time.sleep(3)
          
        elif (Ring[str.lower(attack_choice)] - Ring[computer] == 1) or (Ring[str.lower(attack_choice)] - Ring[computer] == -(len(Ring) - 1)) or (winn == -1):
          #self.color("red", "i")
          win = -1
          print(
                  f"Whoopsies, it looks like {save['name']} lost their winning streak, if they had one HAHA. We know how unlucky you are, try again…"
              )  #Says that the player has lost
          opp_quacks += oBet_choice + bet_choice
          player_quacks -= bet_choice
          #time.sleep(3)
          #self.color("red", "b")
          #self.opponent.insult(save["name"], attack_choice, computer)
          #time.sleep(3)
          
        else:
            #self.color("gray", "b")
            win = 0
            print(f"Fool! Between {attack_choice} and {computer}, there is no winner, they are objectively and completely equal! \nChoose better!")
            
            #time.sleep(5)
            player_quacks -= round(bet_choice / 10)
            print("You have been penalized 10% of your bet for such foolishness")
            if P2:
                print(f"You too {save['RoboName']}!")
                opp_quacks -= round(oBet_choice / 10)
            #time.sleep(3)
        return render_template("clash.html", P1 = attack_choice, P2 = computer, result = win)

        
        
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
        global THEMODE
        THEMODE = eval(save[13])
        global computer
        computer = random.choice(eval(THEMODE))
        global player_quacks
        global opp_quacks
        player_quacks = save[2]
        opp_quacks = save[8]
        return render_template("mainGame.html", 
                               name=save[1], point=save[2], 
                               goalPoints=save[3], bets=save[4], 
                               picks=save[5], comments=save[6], 
                               roboName=save[7], roboPoints=save[8], 
                               roboGoalPoints=save[9], roboBets=save[10],
                               roboPicks=save[11], totalRounds=save[12],
                               mode=mode,
                               currentRound=save[14], computer_choice=computer)
    else:
        return render_template("FirstPage.html", P2 = P2, chance = user_choice)
if __name__ == "__main__":
    APP.run(debug=True)

