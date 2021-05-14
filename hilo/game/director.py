import random 
from game.dealer import Dealer

class Director:
    

    def __init__(self):
        
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        
        self.count = 0
        while self.keep_playing:
            
            self.first = self.first_card()
            self.second = self.second_card()
            self.compare(self.first, self.second)
            self.get_inputs()
            self.do_updates()
            self.check_score()
            self.do_outputs()
            

    def first_card(self):
        
        if self.count == 0:
        
            
            i = random.randint(1, 13)
            first_card = int(self.dealer.deck[i-1])
            
            card_name = first_card
            suits = ['♠', '♣', '♥', '♦']
            
            self.current_suit = random.choice(suits)

            if card_name == 13:
                card_name = 'K'
            elif card_name == 12:
                card_name = 'Q'
            elif card_name == 11:
                card_name = 'J'
            elif card_name == 1:
                card_name = 'A'
            card_name = self.current_suit + str(card_name)
            print(f"\nThe card is: {card_name}")
            self.count = 1
        else:
            first_card = self.second
            card_name = first_card
            suits = ['♠', '♣', '♥', '♦']
            

            if card_name == 13:
                card_name = 'K'
            elif card_name == 12:
                card_name = 'Q'
            elif card_name == 11:
                card_name = 'J'
            elif card_name == 1:
                card_name = 'A'
            card_name = self.current_suit + str(card_name)
            print(f"\nThe card is: {card_name}")
            
        return first_card

    def second_card(self):
        i = random.randint(1,13)
        
        while True:
            second_card = self.dealer.deck[random.randint(0,len(self.dealer.deck)-1)]
            if second_card != self.first:
                break
        #print(f"\ncheat card is: {second_card}")
        return second_card
        

    
    def compare(self, first, second):
        if first > second:
            self.comparison = "l"
        elif first < second:
            self.comparison = "h"
        return self.comparison
            

    
    def get_inputs(self):
        
        self.dealer.guess()
        
    def do_updates(self):

        if (self.dealer.play == self.comparison):
            points = 100
            self.score += points
        else:
            points = -75
            self.score += points
            
        
    def do_outputs(self):
        

        card_name = self.second

        suits = ['♠', '♣', '♥', '♦']

        if card_name == 13:
            card_name = 'K'
        elif card_name == 12:
            card_name = 'Q'
        elif card_name == 11:
            card_name = 'J'
        elif card_name == 1:
            card_name = 'A'

        self.current_suit = random.choice(suits)
        card_name = self.current_suit + str(card_name)
        
        print(f"\nNext card is {card_name}")
        print(f"Your score is: {self.score}")
        
        print("")
        if self.dealer.want() and self.keep_playing:
            choice = input("Keep playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False

    def check_score(self):

        if self.score <= 0:
            self.keep_playing = False

        #return True if self.score <= 0 else False

    
