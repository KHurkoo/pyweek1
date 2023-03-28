import pygame
import sys

class Character:
    def __init__(self, image_path, x, y):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error:
            print("Error: could not load image {}".format(image_path))
            sys.exit()
        self.image = pygame.transform.smoothscale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.x = x
        self.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

def create_characters():
    promo_animated_character = Character("PromoAnimated2x.gif", 0, 0)
    run_character = Character("__Run.gif", 200, 0)
    hero_character = Character("hero.gif", 400, 0)
    other_character = Character("character.gif", 0, 200)
    return [promo_animated_character, run_character, hero_character, other_character]

# Set up the screen
screen_width = 640
screen_height = 480
fullscreen = False

# Initialize Pygame
pygame.init()

# Enable video driver on Mac
if sys.platform == "darwin":
    pygame.display.init()

# Set the window caption
pygame.display.set_caption("Anti-Aliasing Characters")

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

# Create characters
characters = create_characters()

# Control the framerate 
clock = pygame.time.Clock()

# Loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    if sys.platform == "win32":
                        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN) # Set fullscreen mode on Windows
                    elif sys.platform == "darwin":
                        pygame.display.toggle_fullscreen() # Toggle fullscreen mode on Mac
                else:
                    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the characters on the screen
    for character in characters:
        character.draw(screen)

    # Update display
    pygame.display.update()

    # Control the framerate
    clock.tick(60)
