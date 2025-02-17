

import pygame

class Game:
    def __init__(self):
        """
        Initialize the game state with starting values.
        Sets up cookie counter, click multiplier, and cookie position.
        """
        self.cookies = 0                  # Total cookies collected
        self.cookie_per_click = 1         # Cookies earned per click
        self.cookie = pygame.Rect(110,120,300,300)  # Cookie clickable area
        self.cookie_color = "brown"       # Visual appearance
        self.clicked = False             # Track current click state

    def draw_score(self):
        """Render and display the current cookie count on screen."""
        # Convert cookie count to text surface for rendering
        self.display_cookies = text_font.render(f"Cookies: {str(self.cookies)}", True, "black")
        # Place score at bottom-left corner of screen
        screen.blit(self.display_cookies, (0,450))

    def click_button(self):
        """
        Handle cookie click mechanics.
        Updates cookie count when valid clicks are detected.
        """
        # Get current mouse position
        self.mouse_pos = pygame.mouse.get_pos()
        
        # Check if mouse is hovering over cookie area
        if self.cookie.collidepoint(self.mouse_pos):
            # Detect left mouse button press
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                # Only increment cookies when releasing click
                if self.clicked:
                    self.cookies += 1
                    self.clicked = False
        
        # Draw the cookie shape with rounded edges
        pygame.draw.rect(screen, self.cookie_color, self.cookie, border_radius=150)

    def render(self):
        """Update game state and redraw all elements."""
        self.click_button()     # Handle user interaction
        self.draw_score()       # Update displayed score

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


