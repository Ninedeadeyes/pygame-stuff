import pygame

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

#window 

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 


#game loop 

run=True

while run:
    
    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False



pygame.quit()




    







