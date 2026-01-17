import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
BULLET_WIDTH = 10
BULLET_HEIGHT = 15
BULLET_SPEED = 5
NUM_BALLS = 20

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Shooting Game")


class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
        self.y = random.randint(BALL_RADIUS, SCREEN_HEIGHT // 2)  # Start in top half
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.choice([-2, 2])
        self.speed_y = random.choice([-2, 2])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Bounce off walls
        if self.x <= BALL_RADIUS or self.x >= SCREEN_WIDTH - BALL_RADIUS:
            self.speed_x *= -1
        if self.y <= BALL_RADIUS or self.y >= SCREEN_HEIGHT - BALL_RADIUS:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), BALL_RADIUS)


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - BULLET_WIDTH // 2, y, BULLET_WIDTH, BULLET_HEIGHT)

    def move(self):
        self.rect.y -= BULLET_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


# Setup Game Objects
balls = [Ball() for _ in range(NUM_BALLS)]
bullets = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            bullets.append(Bullet(mx, my))

    # Update and Draw Bullets
    for b in bullets[:]:
        b.move()
        b.draw(screen)
        if b.rect.bottom < 0:  # Remove if off screen
            bullets.remove(b)

    # Update and Draw Balls
    for ball in balls:
        ball.move()
        ball.draw(screen)

        # Collision Detection
        ball_rect = pygame.Rect(ball.x - BALL_RADIUS, ball.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        for b in bullets[:]:
            if ball_rect.colliderect(b.rect):
                if b in bullets: bullets.remove(b)
                ball.reset()  # Replace ball by resetting it with a new color/pos

    pygame.display.flip()
    clock.tick(60)

pygame.quit()