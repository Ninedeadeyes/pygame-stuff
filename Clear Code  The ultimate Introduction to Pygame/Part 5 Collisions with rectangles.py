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
snail_surface=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(600,300))

player_surface=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()    # Surface for image information 
player_rect=player_surface.get_rect(midbottom=(80,300))                              # rect for placement position 

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()
        if event.type==pygame.MOUSEMOTION:   # only active if you move the mouse
            if player_rect.collidepoint((event.pos)):   #event.pos= mouse position 
                print("collision")
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("Mouse down")
        if event.type==pygame.MOUSEBUTTONUP:
            print("Mouse up")

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x-=4
    if snail_rect.right<=0:
        snail_rect.x=800

    screen.blit(snail_surface,(snail_rect))
    screen.blit(player_surface,(player_rect))

   # if player_rect.colliderect(snail_rect):    #if player rect with snail collide print  
    #    print("collision")                     #print ("collision") 
          
    # mouse_pos=pygame.mouse.get_pos()            # collide point is usually use with mouse 
    # if player_rect.collidepoint((mouse_pos)):   # If mouse point collide with player rect
    #     #print("collision")                     # print collision   
    #     print (pygame.mouse.get_pressed())      #  print which mouse is pressed eg: true,false, false 


    pygame.display.update()  #update display surfaces  
    clock.tick(60)  