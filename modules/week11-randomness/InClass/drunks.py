import random
class Drunk(object):
    def __init__(self, name=""):
        self.name = name
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name
        
    def __str__(self):
        if self != None:
            return self.name
        return "Anonymous"
    
    
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)
    
    
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
        
class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1.0,0.0), (-1.0,0.0)]
        return random.choice(stepChoices)