from timeit import default_timer as timer

def get_input():
    with open("./day22/22.in","r") as f:
        data = f.read().split("\n\n")
    data = [line.split("\n")for line in [player for player in data]]
    res = [[],[]]
    for n, player in enumerate(data):
        for card in player:
            if "Player" not in card:
                res[n].append(int(card))
    return res

def p1(data):
    while len(data[0]) > 0 and len(data[1]) > 0:
        a = data[0].pop(0)
        b = data[1].pop(0)
        if a > b:
            data[0].extend([a,b])
        elif b > a:
            data[1].extend([b,a])
        
    return max([calcScore(data[0]),calcScore(data[1])])

def calcScore(deck):
    res = 0
    for i, card in enumerate(deck[::-1]):
        res += card * (i+1)
    return res
    
class Game:
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.prev = set()

    def getWinnerDeck(self, playerNum):
        if playerNum == 1:
            return self.deck1
        if playerNum == 2:
            return self.deck2

    def play(self):
        while self.deck1 and self.deck2:
            # Deals with history. Prevents infiite recusion. Base case
            if (tuple(self.deck1), tuple(self.deck2)) in self.prev:
                return 1
            else:
                self.prev.add((tuple(self.deck1), tuple(self.deck2)))
            
            card1 = self.deck1.pop(0)
            card2 = self.deck2.pop(0)
            # Card is greater than cards in deck for at least 1 player
            if card1 > len(self.deck1) or card2 > len(self.deck2):
                if card1 > card2:
                    self.deck1.extend([card1, card2])
                elif card2 > card1:
                    self.deck2.extend([card2, card1])
            else:
                # Both decks are bigger than there top card. Recurse
                recursiveGame = Game(self.deck1[:card1], self.deck2[:card2]).play()
                if recursiveGame == 1:
                    self.deck1.extend([card1,card2])
                if recursiveGame == 2:
                    self.deck2.extend([card2, card1])
        return 1 if self.deck1 else 2

def p2(data):
    game = Game(data[0], data[1])
    winner = game.play()
    deck = game.getWinnerDeck(winner)
    return calcScore(deck)


print("Day 22: Crab Combat")
data = get_input()
p1start = timer()
p1 = p1(data)
p1end = timer()
print(f"Part 1: {p1} in {p1end-p1start}s.")
data = get_input()
p2start = timer()
p2 = p2(data)
p2end = timer()
print(f"Part 2: {p2} in {p2end-p2start}s.")