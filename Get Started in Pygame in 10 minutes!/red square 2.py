import pygame

SCREEN_WIDTH =800
SCREEN_HEIGHT=600

#window 

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player=pygame.Rect((300,250,50,50))  #x,y, width and height 

                                     # a way to represent a rectangle in memory
                                     # essentially a lightweight data structure that stores just a few key pieces of 
                                     # information: position (left, top) and dimensions (width, height). 


run=True


#game loop 
while run:
    
    pygame.draw.rect(screen,(255,0,0),player) # This is needed to draw 'player' onto the screen 
                                               # function that draws rectangles onto surfaces in Pygame
                                               # pygame.draw.rect(surface, color, rect, width=0)
                                               

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.flip()      # make the display Surface actually appear on the user’s monitor.
                               # a fundamental function in Pygame that updates the entire display window to show any changes made during the frame
                               # It serves as the bridge between your game's internal state and what the player sees on screen.
pygame.quit()                  
                               #  can use  pygame.display.update() which can be used to update portions of the screens 

