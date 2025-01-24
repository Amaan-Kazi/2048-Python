import pygame
from board import Board

pygame.init()
game = Board()

# Constants
SCREEN_SIZE = 600
CELL_SIZE = SCREEN_SIZE // len(game.grid)
BACKGROUND_COLOR = (165, 148, 129)
TEXT_COLORS = { "white": (251, 246, 242), "black": (92, 84, 75)}
STYLES = {
  None:   ((191, 176, 161), TEXT_COLORS["black"], pygame.font.Font(None, int(CELL_SIZE * 0.75))), 
  2:      ((238, 229, 218), TEXT_COLORS["black"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  4:      ((237, 226, 201), TEXT_COLORS["black"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  8:      ((242, 177, 121), TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  16:     ((245, 149, 100), TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  32:     ((241, 126, 94),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  64:     ((247, 94, 62),   TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.75))),
  128:    ((235, 206, 114), TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.65))),
  256:    ((237, 204, 97),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.65))),
  512:    ((236, 199, 84),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.65))),
  1024:   ((235, 195, 64),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.45))),
  2048:   ((235, 193, 45),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.45))),
  4096:   ((239, 103, 107), TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.45))),
  8192:   ((238, 78, 90),   TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.45))),
  16384:  ((225, 67, 56),   TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.35))),
  32768:  ((113, 180, 214), TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.35))),
  65536:  ((92, 160, 223),  TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.35))),
  131072: ((0, 123, 190),   TEXT_COLORS["white"], pygame.font.Font(None, int(CELL_SIZE * 0.30))),
}
PADDING = 10

# Initialize Screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("2048")

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
    if event.type == pygame.KEYDOWN:
      if   (event.key in (pygame.K_UP,    pygame.K_w)): game.up()
      elif (event.key in (pygame.K_LEFT,  pygame.K_a)): game.left()
      elif (event.key in (pygame.K_DOWN,  pygame.K_s)): game.down()
      elif (event.key in (pygame.K_RIGHT, pygame.K_d)): game.right()

  screen.fill(BACKGROUND_COLOR)
  
  for row in range(len(game.grid)):
    for col in range(len(game.grid[row])):
      value = game.grid[row][col]
      color, text_color, font = STYLES[value]

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
