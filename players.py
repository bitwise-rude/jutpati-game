
class Player:
    def __init__(self):
        self.cards = []
        self.isHuman = False

    def getCard(self,card):
        '''Recieves a card from probably the card manager'''
        self.cards.append(card)

class Human(Player):
    def __init__(self):
        super().__init__()
        self.isHuman = True


class AI(Player):
    def __init__(self):
        super().__init__()