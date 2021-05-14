import random


class Dealer:

    """
        This class handles the deck. This included the full deck
        array as well as handling guesses.

        It has three methods:
            the constructor, which takes no arguments. It initializes self.deck

            guess(): which takes no arguments. It returns user input.

            want(): which takes no arguments. It returns true
    """


    # the deck
    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    # the dealer will be asked if it's higher or lower
    def guess(self):
        self.play = input("Higher or lower? [h/l] ")
        return self.play
        


    # if the dealer wants to play again, it will return true when he says "y"
    def want(self):
        
        return True