import pygame

pygame.init()

screen=pygame.display.set_mode((640,640))

knight_img= pygame.image.load("hero.gif").convert()    # can use convert.alpha if it has a transparent background

knight_img=pygame.transform.scale(knight_img,
                                   (knight_img.get_width()*2,         # increase size of image by 2*  note 1
                                    knight_img.get_height()*2))

knight_img.set_colorkey((0,0,0))  # remove the black background ( This actually make ALL black pixels in an image transparent)
                                  # if you have black on the image change it to (1,1,1)




running=True
x= 0
clock=pygame.time.Clock()  # Creates a clock object to control frame rate 

delta_time=0.1   # measure the time between frames 


while running:

    screen.fill((255,255,255))

    screen.blit(knight_img,(x,30))

    x+=50*delta_time   
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()
 
    delta_time =clock.tick(60)  # Limits game to 60 frames per second , regardless of computer speed.
    delta_time=max(0.001, min(0.1, delta_time))  


pygame.quit 


## note 1 


# There are a few pixelart rendering methods 

# 1) image.load > transform.scale> screen blit   ( like the one above )

# 2) set_mode(dims,pygame.SCALED) (optimaized) 

# Passing SCALED to pygame.display.set_mode means the resolution depends
# on desktop size and the graphics are scaled.


# 3) image.load> intermediate.blit>transform.scale>screen blit ( older version)