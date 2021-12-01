class Card: 
    suits = ["C", "D", "H", "S"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, suit = "C", rank = "A"):
        self.suit = suit
        self.rank = rank
        self.parent = None  
        self.left = None
        self.right = None
        self.count = 1

    def getSuit(self):
        return self.suit
    
    def setSuit(self, suit):
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def setRank(self, rank):
        self.rank = rank
    
    def getCount(self):
        return self.count
    
    def setCount(self, count):
        self.count = count 
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent 
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left
    
    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right
    
    def __str__(self): 
        return  str(self.suits) + " " + str(self.rank) + " | " + str(self.count) + "\n"