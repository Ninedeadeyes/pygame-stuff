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

game_over_font=pygame.font.Font("freesansbold.ttf",60)

timer=pygame.time.Clock()
score=0

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
    display_game_over= game_over_font.render("Game over man",True,red,black)
    screen.blit(display_game_over,(70,300))

def check_collision(playerx,playery,ballx,bally):
    if abs(playerx-ballx)<45 and abs(playery-bally)<55:      # player width/2(15)+ radius (30)=45  whilst player height/2(25)+radius(30))=55
        global player_x_direction
        global player_y_direction
        global circle_x_direction
        global circle_y_direction
        player_x_direction=0
        player_y_direction=0
        circle_x_direction=0
        circle_y_direction=0
        game_over()

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
        

    screen.fill((background))
    
    
    ball=pygame.draw.circle(screen,green,(circle_x,circle_y),30,5)
    pygame.draw.circle(screen,red,(circle_x,circle_y),25)

    gamer=pygame.draw.rect(screen,orange,[player_x,player_y,player_width,player_height])
    
    check_collision(gamer.centerx,gamer.centery,ball.centerx,ball.centery)

    display_score=font.render("Score:"+str(score),True,white,black)   #render(text, antialias, color, background=None)
    
    screen.blit(display_score,(10,10))     # blit(source,(destination),area(optional),special_flags (optional) )
    pygame.display.flip()    # push everything you drew to push it on the screen 

pygame.quit()




    #explaining maths of collision 
    # Imagine you and your friend are standing at opposite ends of a room. You want to know if you're close enough to touch each other. To figure this out, you could measure the distance between you and your friend.
    #  If that distance is less than a certain number (like 10 steps), you'd say you're close enough to touch.

    # In the check_collision function, the game is doing something similar to see if the player (you) and the ball (your friend) are close enough to touch. Here's how it works:

    # Measuring Distance: The game uses the abs() function to find the absolute difference between your position (playerx and playery) a
    # and your friend's position (ballx and bally). This gives us the straight-line distance between you and your friend.

