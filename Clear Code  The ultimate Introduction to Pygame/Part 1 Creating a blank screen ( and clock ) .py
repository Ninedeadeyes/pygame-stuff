import pygame 
from sys import exit 


pygame.init()
screen=pygame.display.set_mode((800,400))  #width and height
pygame.display.set_caption("Knight Run")
clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()



    # draw all our elements
    # update everything 
    


    


    pygame.display.update()  #update display surfaces 
    
    clock.tick(60)  # means that it should not run  more than 60
                    # framerate per second (setting maximum framerate)