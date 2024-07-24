import pygame 
from sys import exit 

pygame.init()
screen=pygame.display.set_mode((800,400))  #width and height  #Display Surface = Game Window 
pygame.display.set_caption("Knight Run")
clock=pygame.time.Clock()
test_font=pygame.font.Font("font/Pixeltype.ttf",50 )#font type, font size 

sky_surface=pygame.image.load("graphics/Sky.png").convert()
ground_surface=pygame.image.load("graphics/ground.png").convert()
text_surface=test_font.render("My game",False,"black")#text,AA,color
snail_surface=pygame.image.load("graphics/snail/snail1.png").convert_alpha()  # _alpha removes the background of the image 
snail_x_pos=600

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos-=4
    if snail_x_pos==0:
        snail_x_pos=800
    

    screen.blit(snail_surface,(snail_x_pos,250))
    pygame.display.update()  #update display surfaces 
    
    clock.tick(60)   # influence speed of game. 


# Always draw a proper background or you will see multiple copies 
# of the snail as it continously draws the snail each loop. 