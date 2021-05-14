from random import randint

# TODO: Define the Thrower class here.

class Dealer:
    """A class that stores dice data. It keeps track of the current 5 dice and the number of throws for a director.
    
    Attributes:
        dice (list): The last thrown set of dice
        num_throws (int): Stores the number of throws the player achieved. Once negative, the game is over.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of a Thrower.
        """
        self.dice = []
        self.num_throws = 0
    
    def throw_dice(self):
        """Generates 5 random integers between 1-6 that replicate real life dice. Stores the 
        generated dice to self.dice and adds 1 to self.num_throws.

        Args:
            self (Thrower): an instance of a Thrower.
        """
        #self.dice = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        self.dice = [randint(1, 6) for die in range(5)]
        self.num_throws += 1

    def get_points(self):
        """Scans through each dice. For each dice with a value of 1, 100 is added to the score. 
        For each dice with a value of 5, 50 is added to the score. The score is returned.
        
        Args:
            self (Thrower): an instance of a Thrower.
        """
        # score = 0
        # for dice in self.dice:
        #     if dice == 1: score += 100
        #     elif dice == 5: score += 50
        # return score
        return 100 * self.dice.count(1) + 50 * self.dice.count(5)
    
    def can_throw(self):
        """Checks to see if the last throw_dice included either a 1 or a 5. If not, False will be 
        returned. Otherwise, True will be returned, signaling to the director that the user is 
        able to continue rolling.
        
        Args:
            self (Thrower): an instance of a Thrower.
        """
        for dice in self.dice:
            if dice == 1 or dice == 5: return True
        return False