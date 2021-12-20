from random import shuffle

class Card:
    suits = ("pik","kier","karo","trefl")
    vals = (None, None, "2", "3", "4", "5",
            "6", "7", "8", "9", "10",
            "waleta", "damę", "króla", "asa")

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else: return False
        return False
    
    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else: return False
        return False

    def __repr__(self):
        w = self.vals[self.value] + " " + self.suits[self.suit]
        return w

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,14):
            for j in range(4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)

    def give_card(self):
        if self.cards == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0

class Game:
    def __init__(self):
        name1 = input("enter first players name: ")
        name2 = input("enter second players name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "This rounds winner is {}".format(winner)
        print(w)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p2.wins > p1.wins:
            return p2.name
        else: return "nikt"
        
    def draw(self,p1n,p1c,p2n,p2c):
        d = "player {} has {} meanwhile player {} has {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

    def game(self):
        cards = self.deck.cards
        print("lets get started")
        while len(cards)>=2:
            print("press q to exit or any other key to continue: ")
            response = input()
            if response == 'q':
                break
            p1c = self.deck.give_card()
            p2c = self.deck.give_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(p1n)
            else:
                self.p2.wins+=1
                self.wins(p2n)
        w = self.winner(self.p1,self.p2)
        print("zwycięzcą gry zostaje {}".format(w))

gam = Game()
gam.game()
