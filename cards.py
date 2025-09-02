import pygame
from constant import *
import random

class Card:
    suites = ['Clovers','Hearts','Pikes','Tiles']
    names = ['A',"King","Queen","Jack","10","9","8","7","6","5","4","3",'2']

    def loader():
        ''' Loads all of the cards '''
        all_cards = []

        for suite in Card.suites:
            for name in Card.names:
                card = pygame.image.load(PATH_CARDS+f"{suite}_{name}_white.png")
                card = pygame.transform.scale(card,CARD_SIZE)
                card = Card(card,suite,name)
                all_cards.append(card)
        
        return all_cards

    def __str__(self):
        return f"{self.suite}-{self.name}"
        

    def __init__(self,card,suite,name):
        self.cardImage = card
        self.suite = suite
        self.name = name


class CardManager():
    ''' Manages Stuffs Related to Cards'''
    def __init__(self,cards:list,players:list):
        self.deck = cards
        self.players = players
        
        self.maalCard = None
    
    def startGame(self):
        ''' Divides the cards and makes stuff ready for game'''

        # shuffling twice because i don't trust the computer
        random.shuffle(self.deck)
        random.shuffle(self.deck)
        
        # giving players their cards from the deck
        for i in self.players:
            for j in range(CARDS_PER_PLAYER):
                card_to_give = self.deck.pop()
                i.getCard(card_to_give)
        
        # getting the maal card
        self.maalCard = self.deck.pop()

