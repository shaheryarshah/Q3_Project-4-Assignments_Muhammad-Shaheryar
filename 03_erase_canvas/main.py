import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (225, 182, 193)

# Initialize the screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Erase Effect in Pygame")

# Create grid of cells
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Initialize eraser rectangle
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Main loop
running = True
while running:
    # Fill screen with white
    screen.fill(WHITE)

    # Draw grid cells (blue)
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Get mouse position and move the eraser
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

    # Remove cells covered by the eraser
    new_grid = [rect for rect in grid if not eraser.colliderect(rect)]
    grid = new_grid

    # Draw the eraser (pink color)
    pygame.draw.rect(screen, PINK, eraser)

    # Event handling (quit event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

    # Control frame rate
    time.sleep(0.05)

# Quit Pygame when the loop ends
pygame.quit()
