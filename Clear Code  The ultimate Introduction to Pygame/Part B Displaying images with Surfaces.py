import pygame 
from sys import exit 

pygame.init()
screen=pygame.display.set_mode((800,400))  #width and height  #Display Surface = Game Window  
clock=pygame.time.Clock()
test_font=pygame.font.Font("font/Pixeltype.ttf",50 )#font type, font size 

test_surface=pygame.Surface((100,200))  #width and height Regular Surface  
test_surface.fill("Red")  # can't be seen because it was blit before the sky hence hidden, 
                          # will show the latest blit surface on top of previous blit surface beefore it 

sky_surface=pygame.image.load("graphics/Sky.png")
ground_surface=pygame.image.load("graphics/ground.png")
text_surface=test_font.render("My game",False,"black")#text,AA (smooth the edge of text),color

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()  ## opposite of pygame.init()
            exit()

    screen.blit(test_surface,(200,100)) #surface,pos  #The Regular Surface need to be put on the display surface  ( the positin will always be top left of the surface)
                                                      #blit = block image transfer, Need to be 'blit' before image is shown. 
    screen.blit(sky_surface,(0,0))                     #pos=  'move the position of where the image will go on the Display Surface
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    pygame.display.update()  #update display surfaces 
    
    clock.tick(60)  # means that it should not run  more than 60
                    # framerate per second (setting maximum framerate)
                    # Don't need to worry about minimum because modern computer are powerful enough 


    # There are two type of surface 
   
    #Display Surface = Game Window  1 of 2 type of surface (canvas) can only have one, always  visible 
    #Regular Surface  = Essentially a single image  2 of 2 type of surface ( like a post it note), only display 
    # when it is connected to the display surface. eg: text, rect, image 



   #text surface
   # create a font ( text size and style )
   # write text on a surface
   # blit the text surface 