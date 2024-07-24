import pygame 
from sys import exit 

pygame.init()

screen=pygame.display.set_mode((800,400))  #width and height  #Display Surface = Game Window 
pygame.display.set_caption("Pixel Run")
clock=pygame.time.Clock()

game_active = False
start_time=0
text_color = (64, 64, 64)
title_color =(111,196,169)
text_background="#c0e8ec"  # hexadecimal colors
score=0


test_font=pygame.font.Font("font/Pixeltype.ttf",50 )#font type, font size 
title_font=pygame.font.Font("font/Pixeltype.ttf",60 )#font type, font size 
margin_font=pygame.font.Font("font/Pixeltype.ttf",75 )#font type, font size      ( controls the length of margin )
border_font=pygame.font.Font("font/Pixeltype.ttf",80 )#font type, font size     
sky_surf=pygame.image.load("graphics/Sky.png").convert()
ground_surf=pygame.image.load("graphics/ground.png").convert()

# score_surf=test_font.render("My game",False,text_color)#text,AA,color
# score_rect= score_surf.get_rect(center=(400,50))

margin_surf=margin_font.render("DDDDD",False,"Light Blue")#text,AA,color                # controls the width of margin 
margin_rect= margin_surf.get_rect(center=(400,50))

border_surf=border_font.render("DDDDD",False,"Light Blue")#text,AA,color               
border_rect= border_surf.get_rect(center=(400,50))

snail_surf=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect=snail_surf.get_rect(midbottom=(600,300))

player_surf=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()    # Surface for image information 
player_rect=player_surf.get_rect(midbottom=(80,300))                              # rect for placement position 
player_gravity=0

#intro screen 

title_surf=title_font.render("Pixel Run",False,title_color)#text,AA,color
title_rect= title_surf.get_rect(center=(400,50))

message_surf=test_font.render("Press Space Bar to Start",False,title_color)#text,AA,color
message_rect= message_surf.get_rect(center=(400,350))

player_stand=pygame.image.load("graphics/player/player_stand.png").convert_alpha() 
player_stand=pygame.transform.rotozoom(player_stand,0,2)               # rotozoom it rotates, it scales and it filter it   ( sufrace, rotates, scale )
player_stand_rect=player_stand.get_rect(center=(400,200))              # look below for your other two options to scale    

def display_score(text_color):

    current_time=int(pygame.time.get_ticks()/1000)-start_time   
    print(current_time)
    score_surf=test_font.render(f"Score:{current_time}",False,(text_color))  # current_time needs to be a string hence the f-string 
    score_rect= score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,(score_rect))
    return (current_time)

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
                start_time=int(pygame.time.get_ticks()/1000)

                
    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))   
        pygame.draw.rect(screen,text_background,margin_rect)        #  Add back ground colour to score text (display surface, color, the actual rectangle)                                                     
        pygame.draw.rect(screen,text_background,border_rect,5,5)   #   Add border to the score text 
        display_score(text_color)
        score= display_score(text_color)

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
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        score_surf=test_font.render(f"Score:{score}",False,title_color)#text,AA,color
        score_rect= score_surf.get_rect(center=(400,350))
        screen.blit(title_surf,title_rect)

        if score ==0:
             screen.blit(message_surf,message_rect)
        else:
            screen.blit(score_surf,score_rect)

    

    pygame.display.update()  #update display surfaces  
    clock.tick(60)  

    #Transforming Surfaces ( How to scale, rotate, flip  etc )


#scaling   

# player_stand=pygame.image.load("graphics/player/player_stand.png").convert_alpha() 
# player_stand=pygame.transform.scale(player_stand,(100,200))       #scale need 2 aug 
# player_stand_rect=player_stand.get_rect(center=(400,200))     #rotozoom more complex               


# player_stand=pygame.image.load("graphics/player/player_stand.png").convert_alpha() 
# player_stand=pygame.transform.scale2x(player_stand)       # scale2x only need 1 aug 
# player_stand_rect=player_stand.get_rect(center=(400,200))  
# 
# 

#  Showing score on introduction screen  

#  We need store the score in a function 
# Return statement for current_time  ( can use global too )
# blit the time  