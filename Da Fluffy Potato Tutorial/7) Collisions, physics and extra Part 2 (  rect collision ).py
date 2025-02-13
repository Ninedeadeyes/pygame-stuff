import pygame

pygame.init()

screen=pygame.display.set_mode((640,640))

knight_img= pygame.image.load("hero.gif").convert()    # can use convert.alpha if it has a transparent background

knight_img=pygame.transform.scale(knight_img,
                                   (knight_img.get_width()*2,       
                                    knight_img.get_height()*2))

knight_img.set_colorkey((0,0,0))  
                                  
running=True
x= 0
clock=pygame.time.Clock()  # Creates a clock object to control frame rate 

delta_time=0.1   # measure the time between frames 

font=pygame.font.Font(None,size=30)  # Font(file_path, size)


while running:

    screen.fill((255,255,255))


    screen.blit(knight_img,(x,30))

    hitbox= pygame.Rect(x,30,knight_img.get_width(),knight_img.get_height())  # provide knight with hitbox 

    target=pygame.Rect(300,0,160,280)   # image in 'memory

    collision=hitbox.colliderect(target)  

    pygame.draw.rect(screen,(255*collision,255,0),target)  # target will change colour when it collides with knight 


    text=font.render("Hello World",True,(0,0,0))  #render(text, antialias, color, background=None)  False for antialias for pixel art text ( rougher edge)
    screen.blit(text,(300,100))


    x+=50*delta_time    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()
 
    delta_time =clock.tick(60)  # Limits game to 60 frames per second , regardless of computer speed.
    delta_time=max(0.001, min(0.1, delta_time)) 


pygame.quit 

