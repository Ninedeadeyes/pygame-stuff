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

game_active = True

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
player_gravity=0


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()

        if game_active: 
            if event.type==pygame.MOUSEBUTTONDOWN:   #   if you click on the player, player jumps 
                if player_rect.collidepoint((event.pos)) and player_rect.bottom>=300:   # check for mouse button first then collision for efficient
                        player_gravity=-24

            if event.type==pygame.KEYDOWN:              #2nd method of keyboard control 
                if event.key== pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-24

        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:   
                game_active=True
                snail_rect.left=800

                
    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))   
        pygame.draw.rect(screen,text_background,margin_rect)        #  Add back ground colour to score text (display surface, color, the actual rectangle)                                                     
        pygame.draw.rect(screen,text_background,border_rect,5,5)   #   Add border to the score text 

        screen.blit(score_surf,(score_rect))

        snail_rect.x-=4
        if snail_rect.right<=0:
            snail_rect.x=800

        screen.blit(snail_surf,(snail_rect))
        
        #Player
        player_gravity+=1
        player_rect.y+=player_gravity

        if player_rect.bottom >=300:
            player_rect.bottom=300

        screen.blit(player_surf,(player_rect))
        

        #collision 
        if snail_rect.colliderect(player_rect):
            game_active=False

    else:
        screen.fill("Yellow")



    pygame.display.update()  #update display surfaces  
    clock.tick(60)  