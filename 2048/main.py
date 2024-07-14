import pygame
import random


pygame.init()


WIDTH = 400
HEIGHT = 400
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
FONT_SIZE = 20

BACKGROUND_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
FONT_COLOR = (119, 110, 101)

TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


font = pygame.font.Font(None, FONT_SIZE)

def draw_board():
    screen.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = board[row][col]
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if value == 0:
                pygame.draw.rect(screen, EMPTY_CELL_COLOR, cell_rect)
            else:
                color = TILE_COLORS.get(value, TILE_COLORS[2048])
                pygame.draw.rect(screen, color, cell_rect)
                
                text = font.render(str(value), True, FONT_COLOR)
                text_rect = text.get_rect(center=cell_rect.center)
                screen.blit(text, text_rect)
    
    pygame.display.flip()

def add_new_tile():
    empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if board[row][col] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2 if random.random() < 0.9 else 4

def move(direction):
    global board
    if direction == "up":
        board = [list(col) for col in zip(*board)]
    elif direction == "down":
        board = [list(reversed(col)) for col in zip(*board)]
    elif direction == "right":
        board = [row[::-1] for row in board]
    
    moved = False
    for row in range(GRID_SIZE):
        new_row = [tile for tile in board[row] if tile != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
                moved = True
        new_row = [tile for tile in new_row if tile != 0]
        new_row += [0] * (GRID_SIZE - len(new_row))
        if new_row != board[row]:
            moved = True
        board[row] = new_row
    
    if direction == "up":
        board = [list(col) for col in zip(*board)]
    elif direction == "down":
        board = [list(reversed(col)) for col in zip(*board)][::-1]
    elif direction == "right":
        board = [row[::-1] for row in board]
    
    if moved:
        add_new_tile()

def main():
    add_new_tile()
    add_new_tile()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move("up")
                elif event.key == pygame.K_DOWN:
                    move("down")
                elif event.key == pygame.K_LEFT:
                    move("left")
                elif event.key == pygame.K_RIGHT:
                    move("right")
        
        draw_board()
    
    pygame.quit()

if __name__ == "__main__":
    main()
