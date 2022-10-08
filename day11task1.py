# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples 
# [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
# you can use a loop or use something from the library
# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html
import random
# def get_shuffled_cards():
#     ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
#     suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
#     card_deck=[]
#     for i in suits:
#         for j in ranks:
#             pair = (j, i)
#             card_deck.append(pair)
    
#     shuffled = random.sample(card_deck, 52)
#     return shuffled

# print(get_shuffled_cards())

# DAUGIAU INFO IKELE PRIE ANTRO PRATIMO
# 2. Deck - probably for homework, see how far you get
def get_cards():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] 
    suits = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    card_deck=[]
    for i in suits:
        for j in ranks:
            pair = (j, i)
            card_deck.append(pair)
    return card_deck
av_cards = get_cards()
spent= []
class Deck:
    def __init__(self, available = av_cards, spent = []):
        self.available = available
        self.spent = spent
        
    def shuffle(self):
        shuffled = random.sample(av_cards, len(av_cards))
        return self, shuffled

    def get_cards(self, count=1):
        spent = random.sample(av_cards, count)
        av_cards = av_cards - spent
        return self, spent, av_cards

# av_cards.shuffle()
print(get_cards(count=3))
print(spent)
# REVIEW

# # gets some number(default 1) of cards from available 

# write a class Deck with the following attributes(variables)
# available - contains list of card tuples that can be used
# spent - contains list of card tuples that have been used
# there should be following methods:
# constructor (__init__) method
# initializes available with full 52 card list of tuples
# initializes spent with empty list
# shuffle(self):
# # shuffles available cards - works just like 1st function but works on available
# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards
# # you can add other methods and/or attributes if you wish to Deck class


# 3. create a new deck in a different .py file from where Deck() is located, that means use import !