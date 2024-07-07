import pygame

SCREEN_WIDTH =800
SCREEN_HEIGHT=600

#window 

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player=pygame.Rect((300,250,50,50))

#game loop 

run=True

while run:
    
    screen.fill((0,0,0))    # This refresh the screen 
    pygame.draw.rect(screen,(255,0,0),player)   # This is needed to draw 'player' onto the screen 

    #game logic
    key=pygame.key.get_pressed()
    if key[pygame.K_a]==True:
        player.move_ip (-1,0)
    elif key[pygame.K_d]==True:
        player.move_ip (1,0)
    elif key[pygame.K_w]==True:
        player.move_ip (0,-1)
    elif key[pygame.K_s]==True:
        player.move_ip (0,1)

    #event handling

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False



    pygame.display.update()   # make the display Surface actually appear on the user’s monitor.


pygame.quit()

