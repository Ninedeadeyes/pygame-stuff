import pygame 


pygame.init()

screen=pygame.display.set_mode([600,600])

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
background=blue

running=True

while running :
     
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        screen.fill((background))
        pygame.draw.circle(screen,red,(300,300),30,9)


        pygame.display.flip()    # push everything you drew to push it on the screen 

pygame.quit()






