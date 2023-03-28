import pygame
import os

# Display
pygame.init()
screen = pygame.display.set_mode((800, 800))
is_fullscreen = False

# Font
font = pygame.font.Font(None, 36)

# Colors
transparent_red = (255, 0, 0, 128)
black = (0, 0, 0)

# Score
score = 0
high_score = 0

# Load high score from file
if os.path.exists('high_score.txt'):
    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())

# Create the score box
score_box = pygame.Surface((400, 400))
score_box.set_alpha(128)
score_box.fill(transparent_red)

def update_score(new_score):
    global score, high_score
    score = new_score
    if score > high_score:
        high_score = score
        # Save the new high score to file
        with open('high_score.txt', 'w') as f:
            f.write(str(high_score))

def draw_score():
    # Draw the score box
    screen.blit(score_box, (200, 200))
    # Draw the high score
    high_score_text = font.render(f"High Score: {high_score}", True, black)
    screen.blit(high_score_text, (250, 250))
    # Draw the current score
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (250, 350))

def toggle_fullscreen():
    global screen, is_fullscreen
    is_fullscreen = not is_fullscreen
    if is_fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800, 800))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                toggle_fullscreen()

    # Update the game state here

    # Score is updated here

    
    screen.fill((255, 255, 255))
    draw_score()
    pygame.display.flip()
