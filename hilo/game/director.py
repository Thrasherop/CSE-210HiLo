from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 0
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            # Restart option
            if not self.keep_playing:
                if input("Would you like to try again?\n[y/n] ") == "y":
                    self.keep_playing = True
                    self.score = 0
                    self.dealer = Dealer()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means dealing a card.

        Args:
            self (Director): An instance of Director.
        """
        self.dealer.draw_card()
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.score += self.dealer.get_points()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that was dealt and the score is shown.

        Args:
            self (Director): An instance of Director.
        """
        try:
            f = open("hilo_template/hilo/game/highscore.txt", "r")
            high_score = f.read().split("|")
            f.close()
        except:
            f = open("highscore.txt", "w")
            f.write("0|Nobody")
            f.close()
            high_score = ['0', 'Nobody']

        print("\n")
        print("-"*20)
        print(f"You dealt: {self.dealer.card}")
        print(f"Your score is: {self.score}")
        if self.dealer.can_deal():
            print(f"You've had {self.dealer.wins} correct guesses.")
            print(f"You've had {self.dealer.losses} incorrect guesses.")
            choice = input("Would you like to test your luck and guess again?\n[y/n] ")
            self.keep_playing = (choice == "y" or choice == "Y")
        else:
            self.keep_playing = False
            print(f"You had {self.dealer.wins - 1} correct guesses.. Better luck next time!")
            print(f"{high_score[1]} currently holds the high score of {high_score[0]}")
            
            # Game is over. Check to see if the player beat the high score!
            if self.score > int(high_score[0]):
                f = open('hilo_template/hilo/game/highscore.txt', 'w')
                print("\nYou beat the high score! Congratulations!")
                winner = input("What should we remember you by? ")
                f.write(str(self.score) + "|" + winner)
                f.close()