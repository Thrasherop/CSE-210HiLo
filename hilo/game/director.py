import random
from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.count = 0
        while self.keep_playing:
            
            self.first = self.first_card()
            self.second = self.second_card()
            self.compare(self.first, self.second)
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def first_card(self):
        
        if self.count == 0:
            i = random.randint(1, 13)
            first_card = int(self.dealer.deck[i-1])
            print(f"\nThe card is: {first_card}")
            self.count = 1
        else:
            first_card = self.second
            print(f"\nThe card is: {first_card}")
        return first_card

    def second_card(self):
        i = random.randint(1,13)
        second_card = int(self.dealer.deck[i-1])
        print(f"\nNext card is: {second_card}")
        return second_card

    
    def compare(self, first, second):
        if first > second:
            self.comparison = "l"
        elif first < second:
            self.comparison = "h"
        return self.comparison
            

    
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.dealer.guess()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """

        if (self.dealer.play == self.comparison):
            points = 100
            self.score += points
        else:
            points = -75
            self.score += points
            
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        
        print(f"next card is {self.second}")
        print(f"Your score is: {self.score}")
        
        print("")
        if self.dealer.want():
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False