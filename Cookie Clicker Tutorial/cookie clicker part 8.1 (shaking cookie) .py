import pygame
import sys
import math
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Cookie Clicker")
        
        # Game state
        self.cookies = 0
        self.cookie_per_click = 1
        self.cookies_per_second = 0
        
        # UI elements
        self.cookie = pygame.Rect(110, 120, 300, 300)
        self.cookie_color = "brown"
        self.upgradeBtn = pygame.Rect(10, 50, 120, 70)
        self.autoBtn = pygame.Rect(10, 140, 120, 70)
        
        # Separate costs for each upgrade type
        self.click_upgrade_cost = 5
        self.auto_upgrade_cost = 5
        
        # Font setup
        self.game_font = pygame.font.Font(None, 15)
        
        # State tracking
        self.last_update_time = pygame.time.get_ticks()
        self.last_click_time = pygame.time.get_ticks()
        
        # Shake animation variables
        self.shake_intensity = 0
        self.shake_duration = 0
        self.original_cookie_pos = [110, 120]  # Store original position

    def handle_events(self):
        """Process all events including mouse clicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos, event.button)
        return True

    def handle_mouse_click(self, pos, button):
        """Handle mouse click events"""
        if button == 1:  # Left mouse button
            if self.cookie.collidepoint(pos):
                current_time = pygame.time.get_ticks()
                if current_time - self.last_click_time > 200:  # Debounce clicks
                    self.cookies += self.cookie_per_click
                    self.last_click_time = current_time
                    
                    # Start shake animation
                    self.shake_intensity = 5  # Adjust this value to change shake intensity
                    self.shake_duration = 10   # Number of frames to shake
            elif self.upgradeBtn.collidepoint(pos):
                if self.cookies >= self.click_upgrade_cost:
                    self.cookies -= self.click_upgrade_cost
                    self.click_upgrade_cost *= 2
                    self.cookie_per_click += 1
            elif self.autoBtn.collidepoint(pos):
                if self.cookies >= self.auto_upgrade_cost:
                    self.cookies -= self.auto_upgrade_cost
                    self.auto_upgrade_cost *= 2
                    self.cookies_per_second += 1

    def update_shake(self):
        """Update shake animation"""
        if self.shake_duration > 0:
            # Generate random offset within shake_intensity range
            x_offset = random.uniform(-self.shake_intensity, self.shake_intensity)
            y_offset = random.uniform(-self.shake_intensity, self.shake_intensity)
            
            # Update cookie position temporarily
            self.cookie.x = self.original_cookie_pos[0] + x_offset
            self.cookie.y = self.original_cookie_pos[1] + y_offset
            
            # Decrease duration until shake ends
            self.shake_duration -= 1
        else:
            # Reset cookie position when shake ends
            self.cookie.x = self.original_cookie_pos[0]
            self.cookie.y = self.original_cookie_pos[1]

    def update_cookies(self):
        """Update cookies based on time passed"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time >= 1000:  # Update every second
            self.cookies += self.cookies_per_second
            self.last_update_time = current_time

    def draw_score(self):
        """Draw the current cookie count"""
        self.display_cookies = self.game_font.render(f"Cookies: {str(int(self.cookies))}", True, "black")
        self.screen.blit(self.display_cookies, (0, 450))
        
        # Show auto-cookie generation rate
        if self.cookies_per_second > 0:
            self.auto_text = self.game_font.render(f"+{self.cookies_per_second}/sec", True, "black")
            self.screen.blit(self.auto_text, (0, 470))

    def draw_upgrades(self):
        """Draw both upgrade buttons and information"""
        # Click upgrade button
        pygame.draw.rect(self.screen, "grey", self.upgradeBtn, border_radius=15)
        self.upgrade1_description = self.game_font.render(f"+{self.cookie_per_click} cookie per click", True, "black")
        self.screen.blit(self.upgrade1_description, (15, 55))
        self.click_cost_text = self.game_font.render(f"Cost:{str(self.click_upgrade_cost)}", True, "black")
        self.screen.blit(self.click_cost_text, (15, 85))
        
        # Auto-click upgrade button
        pygame.draw.rect(self.screen, "lightblue", self.autoBtn, border_radius=15)
        self.auto_description = self.game_font.render(f"+1 cookie/sec", True, "black")
        self.screen.blit(self.auto_description, (15, 145))
        self.auto_cost_text = self.game_font.render(f"Cost:{str(self.auto_upgrade_cost)}", True, "black")
        self.screen.blit(self.auto_cost_text, (15, 175))

    def render(self):
        """Render all game elements"""
        # Update shake animation
        self.update_shake()
        
        pygame.draw.rect(self.screen, self.cookie_color, self.cookie, border_radius=150)
        self.update_cookies()
        self.draw_score()
        self.draw_upgrades()

    def run(self):
        """Main game loop"""
        clock = pygame.time.Clock()
        running = True
        while running:
            self.screen.fill('white')
            running = self.handle_events()
            self.render()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()