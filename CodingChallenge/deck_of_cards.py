import random

class Deck:
    def __init__(self, cards):
        self.cards = list(cards)

import random

def fisherYatesShuffling(deck_to_shuffle):
    shuffledDeck = deck_to_shuffle[:]
    for i in range(len(shuffledDeck) - 1, 0, -1):
        randomIdx = random.randint(0, i)
        shuffledDeck[i], shuffledDeck[randomIdx] = shuffledDeck[randomIdx], shuffledDeck[i]
    return shuffledDeck


def generate_ordered_deck():
    values = list(range(1, 11))
    deck_of_cards = []
    value_occurrence = 4
    while (value_occurrence != 0):
        for value in values:
            deck_of_cards.append(value)
        value_occurrence -= 1
    return deck_of_cards

def shuffle_deck_of_cards(deck_to_shuffle, isDeck):
    deck_to_shuffle = fisherYatesShuffling(deck_to_shuffle)
    if isDeck == True:
        deck = Deck(deck_to_shuffle)
        return deck
    else:
        return deck_to_shuffle

