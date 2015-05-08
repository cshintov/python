'''
exercise 18.2 Implement sort method for a deck of cards
'''
from random import *

class Card(object):

  '''A playing card wiht attributes suit and rank'''
  ranks = [None,'Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
  suits = ['clubs','diamonds','hearts','spades']
  def __init__(self,suit=0,rank=2):
    self.rank = rank
    self.suit = suit
  
  def __str__(self):
    return '{} of {}'.format(Card.ranks[self.rank],Card.suits[self.suit])
  
  def __cmp__(self,other):
    cda = self.suit,self.rank
    cdb = other.suit,other.rank
    return cmp(cda,cdb) 

class Deck(object):
  '''Deck of 52 cards'''

  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1,14):
        card = Card(suit,rank)
        self.cards.append(card)
  
  def __str__(self):
    deck_cards=[]
    for card in self.cards:
      deck_cards.append(str(card))
    return '\n'.join(deck_cards)

  def pop_card(self):
    return self.cards.pop()

  def add_card(self,card):
    self.cards.append(card)

  def shuffle(self):
    shuffle(self.cards)    

  def sort(self):
    self.cards.sort()
        
def main():
  deck = Deck()
  print deck.cards[0],deck.cards[-1]
  deck.shuffle()
  print deck.cards[0],deck.cards[-1]
  deck.sort()
  print deck.cards[0],deck.cards[-1]

if __name__ == '__main__':
  main()
