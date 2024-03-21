import unittest,copy
from deck_of_cards import Deck, shuffle_deck_of_cards, fisherYatesShuffling, generate_ordered_deck
from random import shuffle
import game_module

def main():
   
   game = game_module.Game()
   player1 = game_module.Player(game.deck.cards[:20], [], 1)
   player2 = game_module.Player(game.deck.cards[20:], [], 2)
   game_module.start_game(game, player1, player2)

if __name__ == "__main__":
   main()