import pygame

SCREEN_WIDTH =800
SCREEN_HEIGHT=600

#window 

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player=pygame.Rect((300,250,50,50))


run=True


#game loop 
while run:
    
    pygame.draw.rect(screen,(255,0,0),player) # This is needed to draw 'player' onto the screen 
    
    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()    # make the display Surface actually appear on the user’s monitor.

pygame.quit()

