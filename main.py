import pygame


screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("The hero`s mistake")
icon=pygame.image.load("./pyweek1/assets/icon.png")
pygame.display.set_icon(icon)
background=pygame.image.load("./pyweek1/assets/background.png")
fps=60

class Hero:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load("./pyweek1/assets/hero.gif")    
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 640 - 60:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 480 - 60:
            self.rect.y += self.speed

hero = Hero(300, 300, 5)

def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        hero.draw()
        hero.move()
        pygame.display.update()


if __name__ == "__main__":
    main()