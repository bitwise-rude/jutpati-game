import visuals,cards,players

# generating cards and card manager
allCards = cards.Card.loader()
players = [players.Human(),players.AI()]

cardManager = cards.CardManager(allCards,players)

# making players

cardManager.startGame()


#Main window
visual = visuals.Window()
visual.start_game(players,cardManager)

visual.mainloop()