import random



# TODO: Define the Thrower class here.
class Dealer:

    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    
    def guess(self):
        self.play = input("Higher or lower? [h/l] ")
        return self.play
        



    def want(self):
        
        return True