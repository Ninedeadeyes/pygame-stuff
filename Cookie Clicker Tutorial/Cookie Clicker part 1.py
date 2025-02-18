import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

text_font=pygame.font.Font(None,50)
title=text_font.render("HI",True,"black")

running=True

clock=pygame.time.Clock()  
                  
while running:

    screen.fill('white')

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    screen.blit(title,(50,50))
    pygame.display.flip()

    clock.tick(60)       

pygame.quit 


