import pygame, sys

class Game:
    def __init__(self):
        self.cookies=0
        self.cookie_per_click=1
        self.cookie=pygame.Rect(110,120,300,300)
        self.cookie_color="brown"
        self.clicked=False
    
    def click_button(self):
        self.mouse_pos=pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            print("colliding")


        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)


    def render(self):
        self.click_button()    

     


pygame.init()

game=Game()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Cookie Clicker")
text_font=pygame.font.Font(None,50)
title=text_font.render("Cookie Clicker",True,"black")

running=True

clock=pygame.time.Clock()  
                  
while running:

    screen.fill('white')

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    screen.blit(title,(130,15))

    game.render()
    pygame.display.flip()

    clock.tick(60)       

pygame.quit 


