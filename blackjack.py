import random

# Define global variables
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace' and self.value > 21:
            self.value -= 10
        
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
    def play(self):
        # Deal initial cards
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        
        # Show hands
        print(f"Dealer's Hand: {self.dealer_hand.cards[0]}, Hidden")
        print(f"Your Hand: {self.player_hand}")
        
        # Player's turn
        while self.player_hand.value < 21:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == 'hit':
                self.player_hand.add_card(self.deck.deal())
                print(f"Your Hand: {self.player_hand}")
            else:
                break
        
        # Dealer's turn
        if self.player_hand.value <= 21:
            print(f"Dealer's Hand: {self.dealer_hand}")
            while self.dealer_hand.value < 17:
                self.dealer_hand.add_card(self.deck.deal())
                print(f"Dealer's Hand: {self.dealer_hand}")
        
        # Determine winner
        if self.player_hand.value > 21:
            print("Bust! You lose.")
        elif self.dealer_hand.value > 21:
            print("Dealer busts! You win.")
        elif self.player_hand.value > self.dealer_hand.value:
            print("You win!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("You lose.")
        else:
            print("Push!")
            
if __name__ == "__main__":
    game = Game()
    game.play()
