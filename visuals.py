import pygame
from constant import *

# Initializing
pygame.init()
pygame.display.set_caption("JutPati Card Game")
pygame.display.init()



class Window():
    ''' Manages the main window '''
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self._running = False
        self.player_cards = None

    
    def start_game(self,players,cardManager):
        ''' Makes stuff initialize to make the game work'''
        self._running = True
        self.players = players
        self.cardManager = cardManager
    
    def draw_player_cards(self,player):

        for card,i in zip(player.cards,range(len(player.cards))):
            self.screen.blit(card.cardImage,(SCREEN_WIDTH-CARD_SIZE[0]*(i+1),SCREEN_HEIGHT-CARD_SIZE[1]-10))


    def mainloop(self):
        ''' The main gameloop '''
        while self._running:
            self.screen.fill((0,0,0))

            for evs in pygame.event.get():
                if evs.type == pygame.QUIT:
                    self._running = False
            
            # displaying the cards of the player:
            for p in self.players:
                if p.isHuman:
                    self.draw_player_cards(p)
                
            pygame.display.update()

        self.onExit()
    
    def onExit(self):
        print("Exiting")
        pygame.quit()
