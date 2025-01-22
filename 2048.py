import pygame

pygame.init()

# Constants
SCREEN_SIZE = 800

# Initialize Screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("2048")

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False

pygame.quit()
