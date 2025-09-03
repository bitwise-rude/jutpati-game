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
        self.human = None

    
    def start_game(self,players,cardManager):
        ''' Makes stuff initialize to make the game work'''
        self._running = True
        self.players = players
        self.cardManager = cardManager

        # Finding our player
        for p in self.players:
                if p.isHuman:
                    self.human = p
        
        # positioning themselves properly
        for i, card in enumerate(self.human.cards):
            x = SCREEN_WIDTH - CARD_SIZE[0] * (i+1)
            y = SCREEN_HEIGHT - CARD_SIZE[1] - 10
            card.x = x
            card.y = y
        size = self.human.cards[0].cardImage.get_rect()
        self.Imgwidth = size[2]
        self.Imgheight = size[3]
            
    
    def draw_player_cards(self,player):
        for card in player.cards:
            self.screen.blit(card.cardImage, (card.x,card.y))

    def clicked_card(self, pos):
        for card in self.human.cards:
            if (pos[0] >= card.x and pos[0] <= (card.x+self.Imgwidth)) and (pos[1] >= card.y and pos[1]<= (card.y+self.Imgheight)) :
                return card
        return False


    def mainloop(self):
        ''' The maingameloop '''
        self.holdingCard = None

        while self._running:
            self.screen.fill((0,0,0))

            for evs in pygame.event.get():
                if evs.type == pygame.QUIT:
                    self._running = False
                
                if evs.type == pygame.MOUSEBUTTONDOWN:
                        clicked = self.clicked_card(pygame.mouse.get_pos())
                        print(clicked)
                        if clicked:
                            self.holdingCard = clicked
                
                if evs.type == pygame.MOUSEBUTTONUP:
                    if evs.button == 1:
                        self.holdingCard = None
            
            # move the holding card with mouse within border
            if self.holdingCard:
                position = pygame.mouse.get_pos()
                if position[1] >= BORDER+self.Imgheight//2:
                    self.holdingCard.x = position[0]-self.Imgwidth//2
                    self.holdingCard.y  = position[1]-self.Imgheight//2
            
            # displaying the cards of the player:
            self.draw_player_cards(self.human)

            # show maal card
            self.screen.blit(self.cardManager.maalCard.cardImage,(50,50))

            # drawing borderLine
            pygame.draw.line(self.screen,(255,0,0),(0,BORDER),(SCREEN_WIDTH,BORDER),3)
                
            pygame.display.update()

        self.onExit()
    
    def onExit(self):
        print("Exiting")
        pygame.quit()
