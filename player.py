import ast

class Player():
   def __init__(self, name, points, goalpoints):
      self.name = name
      self.points = points
      self.goalpoints = goalpoints
      self.betHistory = []
      self.choiceHistory = []
   def __str__(self):
      return  f"Name: {self.name}\nPoints: {self.points}\nGoal Points: {self.goalpoints}\nBetting History: {self.betHistory}\nChoices: {self.choiceHistory}"
   def update(self, points, bet, choice):
      self.points = points
      self.betHistory.append(bet)
      self.choiceHistory.append(choice)
   def getPoints(self):
      return self.points
   def getGoalPoints(self):
       return self.goalpoints
   def getName(self):
       return self.name
   def setName(self, name, goal, bets, choices):
       self.name = name
       self.goalpoints = goal
       self.betHistory = ast.literal_eval(bets)
       self.choiceHistory = ast.literal_eval(choices)
   