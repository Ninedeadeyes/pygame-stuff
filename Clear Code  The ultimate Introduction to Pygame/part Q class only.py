import pygame 
from sys import exit 
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk_1=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()    # Surface for image information 
        self.player_walk_2=pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()    # Surface for image information 
        self.player_walk=[self.player_walk_1,self.player_walk_2]
        self.player_index=0
        self.player_jump=pygame.image.load("graphics/Player/jump.png").convert_alpha()   
        
        self.image=self.player_walk[self.player_index]
        self.rect=self.image.get_rect(midbottom=(80,300))
        self.gravity=0 

        self.jump_sound=pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>=300:
            self.gravity=-20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity+=1
        self.rect.y+=self.gravity 
        if self.rect.bottom>=300:
            self.rect.bottom=300

    def animation_state(self):
        if self.rect.bottom<300:
            self.image=self.player_jump
        else:
            self.player_index+=0.1
            if  self.player_index>=len(self.player_walk):
                self.player_index=0 
            self.image= self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type=="fly":
            fly_1=pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_2=pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames=[fly_1,fly_2]
            y_pos=210

        else:
            snail_1=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2=pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames=[snail_1,snail_2]
            y_pos=300
        
        self.animation_index=0
        self.image=self.frames[self.animation_index]
        self.rect=self.image.get_rect(midbottom=(randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index+=0.1
        if self.animation_index>=len(self.frames):
            self.animation_index=0
        self.image= self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x-=6
        self.destroy()

    def destroy(self):
        if self.rect.x<=-100:
            self.kill()
            
def display_score(text_color):

    current_time=int(pygame.time.get_ticks()/1000)-start_time   
    score_surf=test_font.render(f"Score:{current_time}",False,(text_color))  # current_time needs to be a string hence the f-string 
    score_rect= score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,(score_rect))
    return (current_time)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):   # sprite, group and boolean # player is not a sprite but a 'GroupSingle that contains ones, only work on indivdual   
        player.sprite.rect.midbottom = (80, 300)  # Reset the player position
        player.sprite.gravity = 0  # Reset gravity to 0       obstacle_group.empty()
        return  False                                                     # if player.spirte collide with obstacle_group,  if boolean True the 'obstacle' will be deleted. Doesn't matter in this game 
    return True       

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
bg_music=pygame.mixer.Sound("audio/music.wav")
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

#Group

player=pygame.sprite.GroupSingle()       # Have to place sprite in a group before you can draw/update 
player.add(Player())

obstacle_group=pygame.sprite.Group()

test_font=pygame.font.Font("font/Pixeltype.ttf",50 )#font type, font size 
title_font=pygame.font.Font("font/Pixeltype.ttf",60 )#font type, font size 
margin_font=pygame.font.Font("font/Pixeltype.ttf",75 )#font type, font size      ( controls the length of margin )
border_font=pygame.font.Font("font/Pixeltype.ttf",80 )#font type, font size     
sky_surf=pygame.image.load("graphics/Sky.png").convert()
ground_surf=pygame.image.load("graphics/ground.png").convert()


margin_surf=margin_font.render("DDDDD",False,"Light Blue")#text,AA,color                # controls the width of margin 
margin_rect= margin_surf.get_rect(center=(400,50))

border_surf=border_font.render("DDDDD",False,"Light Blue")#text,AA,color               
border_rect= border_surf.get_rect(center=(400,50))

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
                        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()

        if game_active: 
            if event.type==obstacle_timer:   
                obstacle_group.add(Obstacle(choice(["fly","snail","snail"])))    


        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:   
                game_active=True
                start_time=int(pygame.time.get_ticks()/1000)

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))   
        pygame.draw.rect(screen,text_background,margin_rect)        #  Add back ground colour to score text (display surface, color, the actual rectangle)                                                     
        pygame.draw.rect(screen,text_background,border_rect,5,5)   #   Add border to the score text 
        display_score(text_color)
        score= display_score(text_color)

        player.draw(screen)    # Draw the Sprite Class version 
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        # #collision 
        game_active=collision_sprite()
           
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
