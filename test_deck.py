import unittest, game_module
from deck_of_cards import shuffle_deck_of_cards, fisherYatesShuffling, generate_ordered_deck
from random import shuffle
from game_module import draw_top_card, Player, Game, compare_cards

def is_shuffled(original_deck, cards_in_newly_shuffled_deck):
   print("\tIn is shuffled:\n")
   print(original_deck)
   print(cards_in_newly_shuffled_deck)
   print("\n\n")
   for i in range(len(original_deck)):
         if original_deck[i] != cards_in_newly_shuffled_deck[i]:
               return True
   return False

def test_shuffling_with_parameter(original_deck, shuffled_deck):
      if is_shuffled(original_deck, shuffled_deck) == True:
         return True
      else:
         return False

class TestDeck(unittest.TestCase):
   def test_new_deck_contains_forty_cards(self):
      cards_amount = 40
      starting_deck = generate_ordered_deck()
      deck = shuffle_deck_of_cards(starting_deck, True)
      result = len(deck.cards)
      self.assertEqual(result, cards_amount)
   
   def test_shuffling_function(self):
      starting_deck = generate_ordered_deck()
      original_deck = shuffle_deck_of_cards(starting_deck, True)
      temp = original_deck.cards.copy()
      cards_in_newly_shuffled_deck = fisherYatesShuffling(original_deck.cards)
      original_deck.cards = temp
      print(original_deck.cards)
      print(cards_in_newly_shuffled_deck)
      self.assertTrue(is_shuffled(original_deck.cards, cards_in_newly_shuffled_deck))
      
   def test_drawing_card_if_empty_draw_pile(self):
      deck = generate_ordered_deck()
      empty_draw_pile = []
      player = Player(empty_draw_pile, deck[:20],1)
      initial_discard_pile = player.discard_pile.copy()
      card = draw_top_card(player)
      self.assertTrue(test_shuffling_with_parameter(initial_discard_pile, player.draw_pile))
      
   def test_comparing_cards(self):
      game = game_module.Game()
      deck = generate_ordered_deck()
      player1 = Player([1], [], 1)
      player_with_higher_card = Player([9], [], 2)
      self.assertEqual(2, compare_cards(player1, player_with_higher_card, game))

   def test_comparing_same_cards(self):
      game = game_module.Game()
      starting_deck = generate_ordered_deck()
      shuffled_deck = shuffle_deck_of_cards(starting_deck, True)
      player1 = Player(shuffled_deck.cards[:20],[], 1)
      player2 = Player(shuffled_deck.cards[20:],[], 2)
      player1.draw_pile[-1] = 1
      player2.draw_pile[-1] = 1
      player1.draw_pile[-2] = 5
      player2.draw_pile[-2] = 9
      print(f"{player1.draw_pile}")
      print(f"{player2.draw_pile}")
      result = compare_cards(player1, player2, game)
      self.assertEqual(0, result)
      print(f"Cards hold from the tie: {game.tie_cards}")
      self.assertEqual(2, compare_cards(player1, player2, game))
      player2.discard_pile.append(player1.card)
      player2.discard_pile.append(player2.card)
      self.assertEqual(4, len(player2.discard_pile))
      print(f"Winner discard pile: {player2.discard_pile}")   
      
if __name__ == '__main__':
   unittest.main()