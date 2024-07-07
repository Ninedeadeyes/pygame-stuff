from random import randint
import pygame 

pygame.init()

screen=pygame.display.set_mode([600,600])
pygame.display.set_caption("Ball Bouncer")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255) 
black=(0,0,0) 
orange=(255,165,0)

background=blue
framerate=60

font=pygame.font.Font("freesansbold.ttf",20)
score=0
previous_score=0
high_score=0


game_over_font=pygame.font.Font("freesansbold.ttf",60)

timer=pygame.time.Clock()
score=0
game_over_boolean=False

speed_boost_available=False
speed_boost_x= -100
speed_boost_y= -100
last_grabbed=0 

circle_x=300
circle_y=300
circle_x_direction=2
circle_y_direction=5

player_width=30
player_height=50
player_x=300
player_y=500
player_x_direction=0
player_y_direction=0 
player_speed=3


def game_over():
    global game_over_boolean
    display_game_over= game_over_font.render("Game over man",True,red,black)
    screen.blit(display_game_over,(70,300))
    display_restart=font.render("Press Space to Restart",True,white,black)
    screen.blit(display_restart,(170,450))
    game_over_boolean=True

def check_collision(playerx,playery,ballx,bally):
    if abs(playerx-ballx)<45 and abs(playery-bally)<55:      # player width/2(15)+ radius (30)=45  whilst player height/2(25)+radius(30))=55
        global player_x_direction                            # The reason why it is 'and' is because it needs to overlap in both x and y axis for their to be a collision                   
        global player_y_direction                            # 45 is the width of the player and ball added together hence if playerx-ballx is greater than 45 it would not overlap 
        global circle_x_direction                            # For example if playerx=50x    whilst ballx=150x     50-150x= -100 but then abs convert it to 100 
        global circle_y_direction                            #  since 100 is greater than 45 , it will not collide even if playery-bally is lower than 55.     
        player_x_direction=0                                 #  Another word if the gap between player and ball x axis is less than 45 
        player_y_direction=0                                 # and the gap between player and ball y is less than 55, it will collide  
        circle_x_direction=0                                 # Don't forget abs 'absolute value' will turn - to +  since it can collide on either side. 
        circle_y_direction=0
        game_over()

def check_difficulty():
    global score
    global circle_x_direction
    global circle_y_direction
    x_mod=(score//9)
    y_mod=(score//10)
    if circle_x_direction>0:
        circle_x_direction=4+x_mod
    elif circle_x_direction<0:
        circle_x_direction=-4-x_mod
    if circle_y_direction>0:
        circle_y_direction=5+y_mod
    elif circle_y_direction<0:
        circle_y_direction=-5-y_mod
        
def speed_boost_check():
    global speed_boost_available
    global score
    global last_grabbed
    global speed_boost_x
    global speed_boost_y
    global player_speed
    if score-last_grabbed >10 and not speed_boost_available:
        speed_boost_available=True
        speed_boost_x=randint(0,580)  # to avoid it sticking to right stop a bit early from 600
        speed_boost_y=randint(0,580)


def update_player_position():
    global player_x
    global player_y
    global player_x_direction
    global player_y_direction

    if player_x_direction>0:
        if player_x <600 - player_width:
            player_x+=player_x_direction*player_speed

    if player_x_direction<0:
        if player_x >0:
            player_x+=player_x_direction*player_speed

    if player_y_direction>0:
        if player_y <600 - player_height:
            player_y+=player_y_direction*player_speed

    if player_y_direction<0:
        if player_y >0:
            player_y+=player_y_direction*player_speed

def update_ball_position():
    global circle_x
    global circle_y
    global circle_x_direction
    global circle_y_direction
    global score

    if circle_x_direction>0:
        if circle_x<570:
            circle_x+=circle_x_direction
        
        else:
            circle_x_direction*= -1
            score+=1
    
    elif circle_x_direction<0:
        if circle_x >30:
            circle_x+=circle_x_direction

        else:
            circle_x_direction*= -1
            score+=1

    if circle_y_direction>0:
        if circle_y<570:
            circle_y+=circle_y_direction
        
        else:
            circle_y_direction*= -1
            score+=1
    
    elif circle_y_direction<0:
        if circle_y >30:
            circle_y+=circle_y_direction

        else:
            circle_y_direction*= -1
            score+=1

running=True

while running :

    
    timer.tick(framerate)  # To run at 60 clicks per second ( standardise the speed of game)
    update_ball_position()
    update_player_position()
    check_difficulty()
    speed_boost_check()
    
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
      
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_x_direction=-1
            if event.key==pygame.K_RIGHT:
                player_x_direction=1
            if event.key==pygame.K_UP:
                player_y_direction=-1
            if event.key==pygame.K_DOWN:
               player_y_direction=1
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                player_x_direction=0
            if event.key==pygame.K_RIGHT:
                player_x_direction=0
            if event.key==pygame.K_UP:
                player_y_direction=0
            if event.key==pygame.K_DOWN:
               player_y_direction=0
            
            if event.key==pygame.K_SPACE and game_over_boolean:
                circle_x= 300
                circle_y=300 
                circle_x_direction=4
                circle_y_direction=5
                player_x=300
                player_y=500
                previous_score=score
                if score>high_score:
                    high_score=score
                score=0 
                last_grabbed=0
                player_speed=3
                game_over_boolean=False 


    screen.fill((background))
    
    
    ball=pygame.draw.circle(screen,green,(circle_x,circle_y),30,5)
    pygame.draw.circle(screen,red,(circle_x,circle_y),25)

    gamer=pygame.draw.rect(screen,orange,[player_x,player_y,player_width,player_height])
    
    check_collision(gamer.centerx,gamer.centery,ball.centerx,ball.centery)

    display_score=font.render("Score:"+str(score),True,white,black)   #render(text, antialias, color, background=None)
    
    screen.blit(display_score,(10,10))     # blit(source,(destination),area(optional),special_flags (optional) )

    display_previous_score=font.render("Previous Score:"+str(previous_score),True,white,black)  
    
    screen.blit(display_previous_score,(10,30))     
    
    display_high_score=font.render("High Score:"+str(high_score),True,white,black)   
    
    screen.blit(display_high_score,(10,50))   

    display_speed=font.render("Speed:"+str(player_speed-2),True,white,black)   
    
    screen.blit(display_speed,(450,10))   

    if speed_boost_available:
        speed_boost_item=pygame.draw.rect(screen,white,[speed_boost_x,speed_boost_y,20,20])
        if gamer.colliderect(speed_boost_item):
            player_speed+=1
            speed_boost_x=-100
            speed_boost_y=-100
            last_grabbed=score
            speed_boost_available=False


    pygame.display.flip()    # push everything you drew to push it on the screen 

pygame.quit()




    #explaining maths of collision 
    # Imagine you and your friend are standing at opposite ends of a room. You want to know if you're close enough to touch each other. To figure this out, you could measure the distance between you and your friend.
    #  If that distance is less than a certain number (like 10 steps), you'd say you're close enough to touch.

    # In the check_collision function, the game is doing something similar to see if the player (you) and the ball (your friend) are close enough to touch. Here's how it works:

    # Measuring Distance: The game uses the abs() function to find the absolute difference between your position (playerx and playery) a