import pygame 
from sys import exit 
from random import randint

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

#obstacle 

snail_surf=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
fly_surf=pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

obstacle_rect_list=[]


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

#Timer

obstacle_timer=pygame.USEREVENT+1   #  step one define a custom event. By adding 1 to it (pygame.USEREVENT + 1), you're creating a unique identifier for a new event type, avoid conflict of existing event 
pygame.time.set_timer(obstacle_timer,1500)  #  The two arguments  are What you are triggering ( the custom event) and when ( higher the number the less frequent ) 

def display_score(text_color):

    current_time=int(pygame.time.get_ticks()/1000)-start_time   
    print(current_time)
    score_surf=test_font.render(f"Score:{current_time}",False,(text_color))  # current_time needs to be a string hence the f-string 
    score_rect= score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,(score_rect))
    return (current_time)

def obstacle_movement(obstacle_list):
    if obstacle_list:    # If python evalute an empty list it would equate to false 
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=5

            if obstacle_rect.bottom==300:
                screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)

        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x > -100]
        #example of list comprehension  ( concise way of creating lists based on existing list)
        # The above list comprehension remove 'obstacle with x below -100.
        # hence the new list will only contain obstacle with x over -100 
        # Assignment to obstacle_list effectely replaces the original list with the filter version

        return obstacle_list  # Make sure to target global 
                              # This new list will override the previous list  eg: obstacle_rect_list=obstacle_movement(obstacle_rect_list)
                              #  this way it will continous to update list and 
                              # not worried about scope. 
    else: 
        return[]   # if there nothing in the list (1st loop) then it will return empty list. If you do not do this there will be an error 


def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False 
            
    return True  

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
                start_time=int(pygame.time.get_ticks()/1000)


        if event.type==obstacle_timer and game_active:                      
            if randint(0,2):  # provide 0 or 1 so trigger true or false, In Python, all integers are considered truthy except for zero.  If it 1 or 2 it is True if 0 it is False. When used in an if statement, the result of randint(0, 2) is evaluated in a boolean context. 
                obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900,1100),300)))   
            else:  
                obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900,1100),210)))

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))   
        pygame.draw.rect(screen,text_background,margin_rect)        #  Add back ground colour to score text (display surface, color, the actual rectangle)                                                     
        pygame.draw.rect(screen,text_background,border_rect,5,5)   #   Add border to the score text 
        display_score(text_color)
        score= display_score(text_color)

      
        #Player
        player_gravity+=1
        player_rect.y+=player_gravity

        if player_rect.bottom >=300:
            player_rect.bottom=300

        screen.blit(player_surf,(player_rect))
        
        # Obstacle movement 

        obstacle_rect_list=obstacle_movement(obstacle_rect_list)

        #collision 

        game_active=collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()       # remove all items for new game 
        player_rect.midbottom=(80,300)  # always start on ground in new game 
        player_gravity=0
        
        score_surf=test_font.render(f"Score:{score}",False,title_color)#text,AA,color
        score_rect= score_surf.get_rect(center=(400,350))
        screen.blit(title_surf,title_rect)

        if score ==0:
             screen.blit(message_surf,message_rect)
        else:
            screen.blit(score_surf,score_rect)

    pygame.display.update()  #update display surfaces  
    clock.tick(60)  


# Timer 

# We create a customer user event that is triggered 
# in certain time intervals 

# 1) Create a custom event
# 2) Tell pygame to trigger that event continously 
# 3)  add code in the event loop 