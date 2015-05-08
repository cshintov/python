"""
exercise 18.6 To find the probability of each poker hand
"""

from Card import *

class PokerHand(Hand):
    
    def __init__(self):
        self.suits = {}
        self.ranks = {}
        self.cards = [] 
        self.label = 'pokerhand'

    def hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        #print self.suits
        #print self.ranks
    
    def has_pair(self):
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_twopair(self):
        count = 0
        for val in self.ranks.values():
            if val >= 2:
                count += 1
        if count >= 2:
          return True
        return False
    
    def has_threeofakind(self):
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        if 1 in self.ranks.keys():
            if all(rnk in self.ranks.keys() for rnk in range(13,9,-1)):
                return True
        for r in range(13,4,-1):
            if r in self.ranks.keys():
                if all(rnk in self.ranks.keys() for rnk in range(r-1,r-5,-1)):
                    return True
        return False

    def has_fullhouse(self):
        if self.has_twopair() and self.has_threeofakind():
            return True
        return False

    def has_fourofakind(self):
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
           Also stores the flush cards as a PokerHand object for later use in
           checking for straight flush
        """
        for val in self.suits.values():
            self.flushhand = PokerHand()
            if val >= 5:
                for k,v in self.suits.items():
                    if v == val:
                        suit = k
                for card in self.cards:
                    if card.suit == suit:
                        self.flushhand.cards.append(card)
                        self.flushhand.hist()
                return True
        return False
    
    def has_straightflush(self):
        if self.has_flush() and self.flushhand.has_straight():
                return True
        return False

    def classify(self):
        if self.has_pair():
            self.label = 'Pair'
        if self.has_twopair():
            self.label = 'Two Pair'
        if self.has_threeofakind():
            self.label = 'Three of a Kind'
        if self.has_straight():
            self.label = 'Straight'
        if self.has_flush():
            self.label = 'Flush'
        if self.has_fullhouse():
            self.label = 'Full House'
        if self.has_fourofakind():
            self.label = 'Four of a Kind'
        if self.has_straightflush():
            self.label = 'StraightFlush'
        return self.label

def probability(counts):
    total = sum(counts.values())
    prob = {}
    for key,val in counts.items():
        prob[key] = (val/float(total))*100
    return prob

def print_table(d):
    for key,val in d.items():
        print '{:^15}:{:4.3f}'.format(key,val)

def analyze(hands = 2598960):
    # make a deck
    deck = Deck()
    deck.shuffle()
    count = 0
    counts = {}
    # deal the cards and classify the hands
    while True:
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.hist()
            hand.sort()
            string = hand.classify()
            counts[string] = counts.get(string,0) + 1
            count += 1
            if count >= hands:
                break
        #for - else clause, executes after normal execution of the for loop, not if broken by if       
        else:
            deck = Deck()
            deck.shuffle()
            continue
        print_table( probability(counts))
        break

if __name__ == '__main__':
    analyze(2500000)
