import pygame
from board import Board

pygame.init()
game = Board()

# Constants
SCREEN_SIZE = 800
CELL_SIZE = SCREEN_SIZE // len(game.grid)
BACKGROUND_COLOR = (165, 148, 129)
TEXT_COLORS = { "white": (251, 246, 242), "black": (92, 84, 75)}
COLORS = {
  None: ((191, 176, 161), TEXT_COLORS["black"]),
  2:    ((238, 229, 218), TEXT_COLORS["black"]),
  4:    ((237, 226, 201), TEXT_COLORS["black"])
}
PADDING = 10

# Initialize Screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("2048")
font = pygame.font.Font(None, int(CELL_SIZE * 0.75))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
    if event.type == pygame.KEYDOWN: game.spawn()

  screen.fill(BACKGROUND_COLOR)
  
  for row in range(len(game.grid)):
    for col in range(len(game.grid[row])):
      value = game.grid[row][col]
      color, text_color = COLORS[value]

      x = col * CELL_SIZE + PADDING
      y = row * CELL_SIZE + PADDING
      w = CELL_SIZE - 2 * PADDING
      h = CELL_SIZE - 2 * PADDING

      pygame.draw.rect(screen, color, (x, y, w, h), border_radius=4)

      if value is not None:
        text_surface = font.render(str(value), True, text_color)
        text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
        screen.blit(text_surface, text_rect)

  # Update the display
  pygame.display.flip()

pygame.quit()
