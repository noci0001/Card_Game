import unittest
import sys
from deck_of_cards import Deck, shuffle_deck_of_cards, fisherYatesShuffling, generate_ordered_deck
from game_module import Player, start_game, Game
from debug_game_module import debug_start_game
import argparse
import test_deck

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_deck)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

def main(debug=False, test=False):
    game = Game()
    player1 = Player(game.deck.cards[:20], [], 1)
    player2 = Player(game.deck.cards[20:], [], 2)

    if debug:
        print("DEBUG MODE ENABLED")
        debug_start_game(game, player1, player2)

    if test:
        print("TEST MODE ENABLED")
        result = run_tests()
        if result.wasSuccessful():
            print("ALL TESTS PASSED")
        else:
            print("SOME TESTS FAILED")
    else:
        start_game(game, player1, player2)

    print("\nThank you for playing!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--test", action="store_true", help="Run tests")
    args = parser.parse_args()
    main(debug=args.debug, test=args.test)
