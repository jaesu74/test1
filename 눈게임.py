import pygame
import random

pygame.init()

# Set up display
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fairy Dodge Game")

# Load images
fairy_img = pygame.image.load("재수1.jpg")  # 이미지 파일과 같은 폴더에 있어야 합니다.
fairy_img = pygame.transform.scale(fairy_img, (70, 70))

# Game variables
fairy_x = WIDTH // 2
fairy_y = HEIGHT - 60
fairy_speed = 10
snowflakes = []
snow_size = 15
stage = 1
score = 0
lives = 3
running = True
clock = pygame.time.Clock()

# Generate snowflakes
def create_snowflakes():
    global snowflakes
    snowflakes = [{"x": random.randint(0, WIDTH), "y": random.randint(-HEIGHT, 0), "speed": 6 + stage} for _ in range(10 + stage)]

create_snowflakes()

# Game loop
while running:
    screen.fill((135, 206, 250))  # Light blue background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and fairy_x > 0:
        fairy_x -= fairy_speed
    if keys[pygame.K_RIGHT] and fairy_x < WIDTH - 50:
        fairy_x += fairy_speed

    # Update and draw snowflakes
    for snow in snowflakes:
        snow["y"] += snow["speed"]
        pygame.draw.circle(screen, (255, 255, 255), (snow["x"], snow["y"]), snow_size // 1)
        
        if snow["y"] > HEIGHT:
            snow["y"] = random.randint(-HEIGHT, 0)
            snow["x"] = random.randint(0, WIDTH)
            score += 1
            if score >= 100:
                stage += 1
                score = 0
                create_snowflakes()
        
        if fairy_x < snow["x"] < fairy_x + 50 and fairy_y < snow["y"] < fairy_y + 50:
            lives -= 1
            snow["y"] = random.randint(-HEIGHT, 0)
            if lives <= 0:
                print("Game Over!")
                running = False
                
    # Draw fairy
    screen.blit(fairy_img, (fairy_x, fairy_y))

    # Display score, stage, and lives
    font = pygame.font.Font(None, 40)
    text = font.render(f"Stage: {stage}  Score: {score}  Lives: {lives}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
