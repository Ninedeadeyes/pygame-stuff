import pygame

pygame.init()

screen=pygame.display.set_mode((640,640))

knight_img= pygame.image.load("hero.gif").convert()    # can use convert.alpha if it has a transparent background

knight_img=pygame.transform.scale(knight_img,
                                   (knight_img.get_width()*2,         # increase size of image by 2*  note 1
                                    knight_img.get_height()*2))

knight_img.set_colorkey((0,0,0))  # remove the black background ( This actually make ALL black pixels in an image transparent)
                                  # if you have black on the image change it to (1,1,1)


knights = pygame.Surface((64,64), pygame.SRCALPHA)  # SRCALPHA is a flag that enables per-pixel alpha transparency in Pygame surfaces
knights.blit(knight_img, (0,0))                     # pygame.Surface( size=(width, height),  flags=0, depth=0, masks=None   
knights.blit(knight_img, (20,0))
knights.blit(knight_img, (15,10))

running=True
x= 0
clock=pygame.time.Clock()  # Creates a clock object to control frame rate 

delta_time=0.1   # measure the time between frames 


while running:

    screen.fill((255,255,255))

    knights.set_alpha(max(0,255-x))  # use to fade image 

    screen.blit(knights,(x,30))

    x+=50*delta_time    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()
 
    delta_time =clock.tick(60)  # Limits game to 60 frames per second , regardless of computer speed.
    delta_time=max(0.001, min(0.1, delta_time)) 


pygame.quit 


