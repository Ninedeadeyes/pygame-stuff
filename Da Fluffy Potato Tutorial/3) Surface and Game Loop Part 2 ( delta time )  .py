import pygame

pygame.init()

screen=pygame.display.set_mode((640,640))

knight_img= pygame.image.load("hero.gif").convert()
running=True
x= 0
clock=pygame.time.Clock()  # Creates a clock object to control frame rate 

delta_time=0.1   # measure the time between frames 
print(delta_time)

while running:

    screen.blit(knight_img,(x,30))
    
    x+=50*delta_time    # note 1 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.display.flip()
 
    delta_time =clock.tick(60)  # Limits game to 60 frames per second (maximum it can go).
    delta_time=max(0.001, min(0.1, delta_time)) # Limits delta_time to safe range  note 2 
    print(delta_time)

pygame.quit 


#Delta time is a technique used in game programming to make your game
# run at the same speed on all computers. 


###  Basic concept 
# Delta time measures the time difference between frames, 
# ensuring your game's speed remains consistent regardless of
#  the computer's processing power.

### note 1 
# 60 FPS: knight moves 50 * (1/60) ≈ 0.83 pixels per frame
# At 30 FPS: knight moves 50 * (1/30) ≈ 1.67 pixels per frame
# Total movement speed remains constant: 50 pixels per second

###note 2 
# Prevents delta_time from being too small (minimum 0.001)
# Prevents delta_time from being too large (maximum 0.1)
# Ensures smooth movement even if frames take longer than expected

# eg:

#If delta_time = 0.0005:
#First comparison: min(0.1, 0.0005) → keeps 0.0005
#Second comparison: max(0.001, 0.0005) → uses 0.001
#Result: 0.001 (floored)

#If delta_time = 0.15:
#First comparison: min(0.1, 0.15) → uses 0.1
#Second comparison: max(0.001, 0.1) → keeps 0.1
#Result: 0.1 (capped)

