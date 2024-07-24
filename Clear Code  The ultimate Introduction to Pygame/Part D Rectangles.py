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

player_surf=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()    # Surface for image information 
player_rect=player_surf.get_rect(midbottom=(80,300))                              # rect for placement position 

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x-=4       # To move, you move the rect not the image
    if snail_rect.right<=0:    # check if the right side of the snail is equal or lower than 0 
        snail_rect.x=800     

    screen.blit(snail_surface,(snail_rect))
    screen.blit(player_surf,(player_rect))
    pygame.display.update()  #update display surfaces 
    
    clock.tick(60)  


    # Rectangle has two functions 

    #1) Precise positioning of surfaces 
    #2) Basic Collision 

    # With Rectangle you can position it from the bottom rather top left
    # which is harder to position things. Positioning things from the bottom 
    # is the best. 

    # Image is place with two different viables  (eg : sprite class )  

    # Surface for image information 
    # Placement via rectangle  eg: screen.blit(snail_surface,(snail_rect))


      # tuple (x,y)
    # topleft    midtop     topright 
    # midleft     center      midright 
    # bottomleft  midbottom   bottomrigh

      #individual values 

      #x,y      top 
      # left    centerx, centery   right 
      #         bottom
    