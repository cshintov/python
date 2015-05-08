'''
exercise 18.2 Implement dealing a hand from a deck
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
  
  def move_cards(self,hand,num):
    '''moves num number of cards from the deck to the hand'''

    for i in range(num):
      hand.add_card(self.pop_card())
  
  def deal_hands(self,hand_num,card_num):
  '''deals a number of hands containing given number of cards'''

    hands = []
    for i in range(hand_num):
      hand = Hand('hand '+str(i+1))
      self.move_cards(hand,card_num)
      hands.append(hand)
    
    return hands

class Hand(Deck):
  '''a hand of playing cards with attributes list of cards and a label'''
  
  def __init__(self,label):
    self.cards = []
    self.label = label

  def __str__(self):
    cards = []
    for card in self.cards:
      cards.append(str(card))
    string = ', '.join(cards)
    return self.label+'{ '+string+' }'+'\n'

def main():
  
  deck = Deck()
  hands = deck.deal_hands(3,2)
  for i in range(3):
    print hands[i]
  deck.shuffle()
  hands = deck.deal_hands(3,2)
  for i in range(3):
    print hands[i]

if __name__ == '__main__':
  
  main()
