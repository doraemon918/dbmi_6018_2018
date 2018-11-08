import numbers
import math
import random
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if isinstance(value, numbers.Real):
            self.__x = value
        else:
            raise ValueError("location values must be real numbers")
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if isinstance(value, numbers.Real):
            self.__y = value
        else:
            raise ValueError("location values must be real numbers")
            
    def distFrom(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    
    def move(self, deltaX, deltaY):
        return Location(self.x+deltaX, self.y+deltaY)
    
    def __str__(self):
        return "<%s,%s>"%(str(self.x), str(self.y))
    def __add__(self, other):
        return  Location(self.x+other.x, self.y+other.y)
class Field(object):
    def __init__(self):
        self.__drunks = {}
        
    def drunks(self):
        return tuple(self.__drunks.keys())
    def hasDrunk(self, drunk):
        return drunk in self.__drunks
    
    def addDrunk(self, drunk, loc):
        
        if not isinstance(loc, Location):
            raise TypeError("loc must be an instance of location")
        if self.hasDrunk(drunk):
            raise ValueError("Duplicate drunk")
                            
        else:
            self.place(drunk, loc)
    
    def placeDrunk(self, drunk, loc):
        self.__drunks[drunk] = loc
        
    def moveDrunk(self, drunk):
        if drunk not in self.__drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.__drunks[drunk]
        self.placeDrunk(drunk, currentLocation.move(xDist, yDist))
        
        
    def getLoc(self, drunk):
        if drunk not in self.__drunks:
            raise ValueError("Drunk not in field")
        return self.__drunks[drunk]
                            
class OddField(Field):
    def __init__(self, numHoles, xRange, yRange):
        super(OddField, self).__init__()
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x,y)] = newLoc
            
    def moveDrunk(self, drunk):
        super(OddField, self).moveDrunk(drunk)
        l = self.getLoc(drunk)
        
        if (l.x, l.y) in self.wormholes:
            self.placeDrunk(drunk, self.wormholes[(l.x,l.y)])
                                    