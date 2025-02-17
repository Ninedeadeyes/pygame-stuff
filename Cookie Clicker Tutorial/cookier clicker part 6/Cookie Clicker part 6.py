import pygame, sys

class Game:
    def __init__(self):
        self.cookies=0
        self.cookie_per_click=1
        self.cookie=pygame.Rect(110,120,300,300)
        self.cookie_color="brown"
        self.clicked=False
        self.game_font=pygame.font.Font(None,15)
        
        self.upgradeBtn=pygame.Rect(10,50,160,70)
        self.upgrade1_cost=5 

    def upgrade(self):
        self.upgrade1_description=self.game_font.render(f"+{self.cookie_per_click} cookier per click.",True,"black")
        self.display_cost=text_font.render(f"Cost:{str(self.upgrade1_cost)}",True,"black")

        pygame.draw.rect(screen,"grey",self.upgradeBtn, border_radius=15)
        screen.blit(self.display_cost,(15,85))
        screen.blit(self.upgrade1_description,(15,55))

    
    def draw_score(self):
        self.display_cookies=text_font.render(f"Cookies: {str(self.cookies)}",True, "black" )
        screen.blit(self.display_cookies,(0,450))

    def click_button(self):
        self.mouse_pos=pygame.mouse.get_pos()
        if self.cookie.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked=True
            else:
                if self.clicked:
                    self.cookies+=1
                    click_sound.play()
                    self.clicked=False

        if self.upgradeBtn.collidepoint(self.mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked=True
            else:
                if self.clicked:
                    if self.cookies >=self.upgrade1_cost:
                        self.cookies-=self.upgrade1_cost
                        self.upgrade1_cost*=2
                        self.cookie_per_click+=1
                    click_sound.play()    
                    self.clicked=False

                
            


        pygame.draw.rect(screen,self.cookie_color,self.cookie,border_radius=150)


    def render(self):
        self.click_button()
        self.draw_score()
        self.upgrade()

pygame.init()

game=Game()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Cookie Clicker")
text_font=pygame.font.Font("assets/font.ttf", 23)
title=text_font.render("Cookie Clicker",True,"black")
background=pygame.image.load("assets/background.jpg").convert()

background=pygame.transform.scale(background,
                                   (background.get_width()*2,         # increase size of image by 2*  note 1
                                    background.get_height()*3))


click_sound=pygame.mixer.Sound("assets/click.wav")
running=True

clock=pygame.time.Clock()  
                  
while running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.blit(title,(130,15))

    game.render()
    pygame.display.flip()

    clock.tick(60)       

pygame.quit 


