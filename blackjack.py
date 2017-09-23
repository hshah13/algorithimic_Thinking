# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_hand = []
dealer_hand = []
deck = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []    # create Hand object

    def __str__(self):
        card_list_string = 'hand contains: '    # return a string representation of a hand
        for card in self.card_list:
            card_list_string += str(card)
            card_list_string += ' '
        return card_list_string
    
    def add_card(self, card):
        self.card_list.append(card)    # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        for card in self.card_list:
            value += VALUES[card.get_rank()]
        for card in self.card_list:
            if card.get_rank() == 'A' and value <= 11:
                value += 10
        return value
            
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []    # create a Deck object
        [self.cards.append(Card(suit, rank)) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)    # use random.shuffle()

    def deal_card(self):
        return self.cards.pop(0)    # deal a card object from the deck
    
    def __str__(self):
        deck_cards = 'Deck : '    # return a string representing the deck
        for card in self.cards:
            deck_cards += card.get_suit() + card.get_rank()
            deck_cards += ' '
        return deck_cards

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck
    in_play = True
    player_hand = Hand()
    dealer_hand = Hand() 
    deck = Deck()
    deck.shuffle()
    print deck
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    print player_hand
    print dealer_hand

    
    in_play = True

def hit():
    global in_play, player_hand, dealer_hand, deck, score
    if in_play:
        player_hand.add_card(deck.deal_hand())
    if player_hand.get_value() > 21:
        outcome = 'You are busted'
        in_play = False
        score -= 5
       
def stand():
    global in_play, player_hand, dealer_hand, deck, score
 
    while dealer_hand.get_value() <= 17 and in_play:
        dealer_hand.add_card(deck.deal_card())
    if dealer_hand.get_value() > 21:
        outcome = 'Dealer is busted, You win'
        in_play = False
        score += 5
    if in_play:
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome = 'Dealer Won'
            score -= 5
        else:
            outcome = 'You Won'
            score += 5
        in_play = False


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

'''
#testing hand class

card1 = Card('C', 'A')
card2 = Card('S' , 'T')
card3 = Card('D', '8')

test_hand = Hand()
print test_hand

test_hand.add_card(card1)
test_hand.add_card(card2)
test_hand.add_card(card3)

print test_hand
'''
'''
#testing deck class

test_deck = Deck()
print test_deck

test_deck.shuffle()
print test_deck
print str(test_deck.deal_card())
print test_deck

'''
'''
# test get value Method

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
c4 = Card("S", "K")
c5 = Card("C", "7")
c6 = Card("D", "A")

test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c2)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()



test_hand = Hand()
print test_hand
print test_hand.get_value()

test_hand.add_card(c1)
print test_hand
print test_hand.get_value()

test_hand.add_card(c6)
print test_hand
print test_hand.get_value()

test_hand.add_card(c4)
print test_hand
print test_hand.get_value()

test_hand.add_card(c5)
print test_hand
print test_hand.get_value()

test_hand.add_card(c3)
print test_hand
print test_hand.get_value()
'''