import pygame

pygame.init()

screen=pygame.display.set_mode((640,640))

knight_img= pygame.image.load("hero.gif").convert()
running=True
x= 0
clock=pygame.time.Clock()  # This is needed because without 'clock' it will run as fast the computer can process 
                  
while running:

    screen.blit(knight_img,(x,30))
    
    x+=1
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()

    clock.tick(60)        # This is needed to slow it down by making the 'max' fps to 60.   note 1

pygame.quit 


### note 1
#simpler solution than delta time but doesn't guarantee:
#Exact timing between frames
#Consistent movement speed
# Smooth animation across different computers