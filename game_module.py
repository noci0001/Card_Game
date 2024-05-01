import deck_of_cards

class Player:
   def __init__(self, draw_pile, discard_pile, player_number):
      self.player_number = player_number
      self.draw_pile = draw_pile
      self.discard_pile = discard_pile
      self.won = False
      self.card = 0
      
   def num_player_cards(self):
      total_player_cards = len(self.draw_pile) + len(self.discard_pile)
      return total_player_cards

def draw_top_card(player):
   if len(player.draw_pile) == 0:
      player.draw_pile = deck_of_cards.shuffle_deck_of_cards(player.discard_pile, False)
      player.discard_pile = []
      print(player.draw_pile)
   player_cards = player.num_player_cards()
   player.card = player.draw_pile.pop()
   print(f"Player {player.player_number} ({player_cards} cards): {player.card}")

class Game:
   def __init__(self):
      self.turns_counter = 0
      starting_deck = deck_of_cards.generate_ordered_deck()
      self.deck = deck_of_cards.shuffle_deck_of_cards(starting_deck, True)
      self.tie_cards = []
      self.turn_winner = 0
      
def add_cards_to_discard_pile(player, cards):
   for card in cards:
      player.discard_pile.append(card)

def indentify_winner(player1, player2):
   if ((len(player1.discard_pile) == 0) and (len(player1.draw_pile) == 0)):
         return 2
   if ((len(player2.discard_pile) == 0) and (len(player2.draw_pile) == 0)):
         return 1

def compare_cards(player1, player2, game):
   draw_top_card(player1)
   draw_top_card(player2)
   prev_tie = False
   if (player1.card == player2.card):
      print("No winner in this round")
      game.tie_cards += [player1.card, player2.card]
      return (0)
   elif (player1.card > player2.card):
      print("Player 1 wins this round\n")
      if (len(game.tie_cards) > 1):
         for card in list(game.tie_cards):
               player1.discard_pile.append(game.tie_cards.pop())
      return (1)
   elif (player2.card > player1.card):
      print("Player 2 wins this round\n")
      if (len(game.tie_cards) > 1):
         for card in list(game.tie_cards):
            player2.discard_pile.append(game.tie_cards.pop())
      return (2)
   
def winner_gets_cards(game, turn_winner, player1, player2):
   if (turn_winner == 1):
      player1.discard_pile.append(player1.card)
      player1.discard_pile.append(player2.card)
      game.tie_cards = []
   elif (turn_winner == 2):
      player2.discard_pile.append(player1.card)
      player2.discard_pile.append(player2.card)
      game.tie_cards = []

def start_game(game, player1, player2):
   counter = 0
   while (1):
      if (player1.num_player_cards() == 0):
         if len(game.tie_cards) > 0:
            for card in game.tie_cards:
               player2.discard_pile.append(card)
               game.tie_cards.pop()
         break
      if (player2.num_player_cards() == 0):
         if len(game.tie_cards) > 0:
            for card in game.tie_cards:
               player1.discard_pile.append(card)
               game.tie_cards.pop()
         break
      game.turn_winner = compare_cards(player1, player2, game)
      winner_gets_cards(game, game.turn_winner, player1, player2)
      total_cards = player1.num_player_cards() + player2.num_player_cards() + len(game.tie_cards)
      if (total_cards != 40):
         break
      counter += 1
   winner = indentify_winner(player1, player2)
   if (winner == 1):
      player1.won = True
      player2.won = False
      print("Player 1 wins the game!\n")
   else:
      player1.won = False
      player2.won = True
      print("Player 2 wins the game!\n")


