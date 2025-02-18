import pygame, sys

class Game:
    def __init__(self):
        """
        Initialize the game state with basic properties.
        Sets up initial cookie counter, click multiplier, and cookie position.
        """
        self.cookies = 0                  # Starting cookie count
        self.cookie_per_click = 1         # Base cookies earned per click
        self.cookie = pygame.Rect(110,120,300,300)  # Cookie clickable area
        self.cookie_color = "brown"       # Cookie visual appearance
        self.clicked = False             # Track current click state

    def click_button(self):
        """
        Handle cookie click mechanics and drawing.
        Manages mouse interaction with the cookie.
        """
        # Get current mouse position for collision detection
        self.mouse_pos = pygame.mouse.get_pos()
        
        # Check if mouse is hovering over cookie area
        if self.cookie.collidepoint(self.mouse_pos):
            print("colliding")  # Debug output showing collision detection
            
        # Draw the cookie shape with rounded edges
        pygame.draw.rect(screen, self.cookie_color, self.cookie, border_radius=150)

    def render(self):
        """
        Update game state and redraw all elements.
        Currently only handles cookie rendering.
        """
        self.click_button()  # Handle user interaction

# Initialize Pygame and setup display
pygame.init()

# Create game instance
game = Game()

# Set up window dimensions (500x500 pixels)
screen = pygame.display.set_mode((500,500))

# Configure window title
pygame.display.set_caption("Cookie Clicker")

# Setup font for rendering text
text_font = pygame.font.Font(None, 50)

# Render main title text
title = text_font.render("Cookie Clicker", True, "black")

# Main game loop variables
running = True          # Controls game loop continuation
clock = pygame.time.Clock()  # Limits game to 60 FPS

# Main game loop
while running:
    # Clear screen with white background
    screen.fill('white')
    
    # Process events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw title at top of screen
    screen.blit(title, (130, 15))
    
    # Update and render game state
    game.render()
    
    # Update display
    pygame.display.flip()
    
    # Cap framerate at 60 FPS
    clock.tick(60)

# Cleanup
pygame.quit()


