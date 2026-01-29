import random
import ast
class Opp():

   def __init__(self, name, points, goalpoints):
      self.name = name
      self.points = points
      self.goalpoints = goalpoints
      self.betHistory = []
      self.choiceHistory = []

   def setName(self, name, goal, bets, choices):
       self.name = name
       self.goalpoints = goal
       self.betHistory = ast.literal_eval(bets)
       self.choiceHistory = ast.literal_eval(choices)
      
   def __str__(self):
      return f"Opponent Name: {self.name}\nOpponent Points: {self.points}\nOpponent Goal Points: {self.goalpoints}\nBet: {self.betHistory}\nChoice: {self.choiceHistory}"
      
   def insult(self, Human, Hchoice, Rchoice):
      self.insults = ["Oops, my bad. I could’ve sworn I was dealing with an adult.",
"I’m not insulting you, I’m describing you.",
"You’re not trash; you just have bad luck when thinking.",
"I’m sorry, were you raised by a mule?",
"You’re so trash, when your mom dropped you off at school she got a fine for littering.",
"Don’t worry, the first 40 years of childhood are always the hardest.",
"Were you born this bad, or did you have to take lessons?",
"If I were on a deserted island with you and a tin of corned beef, I’d rather eat you and talk to the corned beef.", #You can add in more insults here, just make sure to have a comma after each one. e.g "insult", "insult"
"You’re as useless as the ‘ueue’ in ‘queue’.",
"You’re the human embodiment of 'Ctrl + Alt + Delete'",
"If there was a class on overthinking, you’d be the professor.",
"Skill Issue.", f"EVERYONE knows that {Rchoice} is better than {Hchoice}",
"Easy Peazy", f"Of course you picked {Hchoice}", f"{Human} the not-so almighty.",
"So obvious.",
"You might as well be ChatGPT",
"If your this bad against a robot, imagine how bad you are against a human.",
"Git Gud"]
      print(f"\n{self.name}: {random.choice(self.insults)}")
      
   def update(self, points, bet, choice):
        self.points = points
        self.betHistory.append(bet)
        self.choiceHistory.append(choice)
   
   def getPoints(self):
      return self.points
   
   def getGoalPoints(self):
       return self.goalpoints
   
   