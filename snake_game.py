import pygame
import sys
import random

# Pygame'ı başlat
pygame.init()

# Ekranın boyutunu belirle
width = 480
height = 480
cell_size = 20
cell_number = width // cell_size

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Yılan hücrelerini saklayan bir liste oluştur
snake = [(cell_number // 2, cell_number // 2)]
snake_dir = 'RIGHT'

# Yemin başlangıç konumunu rastgele belirle
food = (random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))

def draw_cell(x, y, color):
    pygame.draw.rect(screen, color, pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))

running = True
while running:
    # FPS ayarla
    clock.tick(10)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != 'RIGHT':
        snake_dir = 'LEFT'
    elif keys[pygame.K_RIGHT] and snake_dir != 'LEFT':
        snake_dir = 'RIGHT'
    elif keys[pygame.K_UP] and snake_dir != 'DOWN':
        snake_dir = 'UP'
    elif keys[pygame.K_DOWN] and snake_dir != 'UP':
        snake_dir = 'DOWN'

    # Yılanın hareket etmesini sağla
    if snake_dir == 'UP':
        new_head = (snake[0][0], snake[0][1] - 1)
    elif snake_dir == 'DOWN':
        new_head = (snake[0][0], snake[0][1] + 1)
    elif snake_dir == 'LEFT':
        new_head = (snake[0][0] - 1, snake[0][1])
    elif snake_dir == 'RIGHT':
        new_head = (snake[0][0] + 1, snake[0][1])

    # Yılanın kendine veya duvara çarpması durumunda oyunu bitir
    if (new_head in snake) or (new_head[0] < 0 or new_head[0] >= cell_number or new_head[1] < 0 or new_head[1] >= cell_number):
        running = False

    # Yılanın başını hareket ettir ve yemi yemesini kontrol et
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))
    else:
        snake.pop()

    # Ekrana çizim yap
    screen.fill((0, 0, 0))  # Ekranı siyahla doldur
    for cell in snake:
        draw_cell(cell[0], cell[1], (0, 255, 0))  # Yılanı çiz
    draw_cell(food[0], food[1], (255, 0, 0))  # Yemi çiz

    # Ekranı güncelle
    pygame.display.flip()

# Oyun döngüsü bitti
