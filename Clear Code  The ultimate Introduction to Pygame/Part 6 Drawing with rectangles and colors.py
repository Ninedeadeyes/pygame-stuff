import pygame 
from sys import exit 

pygame.init()
text_color=(64,64,64)    #rgb color   ( probably use rgb as it is simpler )
text_background="#c0e8ec"  # hexadecimal colors

screen=pygame.display.set_mode((800,400))  #width and height  #Display Surface = Game Window 
pygame.display.set_caption("Knight Run")
clock=pygame.time.Clock()
test_font=pygame.font.Font("font/Pixeltype.ttf",50 )#font type, font size 
margin_font=pygame.font.Font("font/Pixeltype.ttf",75 )#font type, font size      ( controls the length of margin )
border_font=pygame.font.Font("font/Pixeltype.ttf",80 )#font type, font size     


sky_surf=pygame.image.load("graphics/Sky.png").convert()
ground_surf=pygame.image.load("graphics/ground.png").convert()

score_surf=test_font.render("My game",False,text_color)#text,AA,color
score_rect= score_surf.get_rect(center=(400,50))

margin_surf=margin_font.render("DDDDD",False,"Light Blue")#text,AA,color                # controls the width of margin 
margin_rect= margin_surf.get_rect(center=(400,50))

border_surf=border_font.render("DDDDD",False,"Light Blue")#text,AA,color               
border_rect= border_surf.get_rect(center=(400,50))

snail_surf=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect=snail_surf.get_rect(midbottom=(600,300))

player_surf=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()    # Surface for image information 
player_rect=player_surf.get_rect(midbottom=(80,300))                              # rect for placement position 

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()
        if event.type==pygame.MOUSEMOTION:   # only active if you move the mouse
            if player_rect.collidepoint((event.pos)):   #event.pos= mouse position 
                print("collision")


    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))   
    pygame.draw.rect(screen,text_background,margin_rect)        #  Add back ground colour to score text (display surface, color, the actual rectangle)                                                     
    pygame.draw.rect(screen,text_background,border_rect,5,5)   #   Add border to the score text 
    #pygame.draw.line(screen,"Gold",(0,0),(800,400),5)       # This is just practice,  this draws a line across the screen 
    #pygame.draw.line(screen,"Gold",(0,0),(pygame.mouse.get_pos()),5)       # This is just practice 
    #pygame.draw.ellipse(screen,"Brown",pygame.Rect(50,100,100,100))     # create a rect from scratch   (left,top,width,height )
    
    screen.blit(score_surf,(score_rect))

    snail_rect.x-=4
    if snail_rect.right<=0:
        snail_rect.x=800

    screen.blit(snail_surf,(snail_rect))
    screen.blit(player_surf,(player_rect))

   # if player_rect.colliderect(snail_rect):    #if player rect with snail collide print  
    #    print("collision")                     #print ("collision") 
          
    # mouse_pos=pygame.mouse.get_pos()            # collide point is usually use with mouse 
    # if player_rect.collidepoint((mouse_pos)):   # If mouse point collide with player rect
    #     #print("collision")                     # print collision   
    #     print (pygame.mouse.get_pressed())      #  print which mouse is pressed eg: true,false, false 


    pygame.display.update()  #update display surfaces  
    clock.tick(60)  


    # Can use rectangle to draw ( eg: rectangles, circles, lines, pointes, ellipses etc )