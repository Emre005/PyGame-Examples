import pygame
import sys

# Pygame'ı başlat
pygame.init()

# Ekranın boyutunu belirle
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Dikdörtgenin özelliklerini belirle
x, y, w, h = 50, 50, 64, 64
vx, vy = 0, 0
speed = 2

clock = pygame.time.Clock()

running = True
while running:
    # FPS ayarla
    clock.tick(60)

    # Olayları kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vx = -speed
    elif keys[pygame.K_RIGHT]:
        vx = speed
    else:
        vx = 0

    if keys[pygame.K_UP]:
        vy = -speed
    elif keys[pygame.K_DOWN]:
        vy = speed
    else:
        vy = 0

    x += vx
    y += vy

    # Ekrana çizim yap
    screen.fill((0, 0, 0))  # Ekranı siyahla doldur
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, w, h))  # Dikdörtgeni çiz

    # Ekranı güncelle
    pygame.display.flip()

# Oyun döngüsü bittiğinde Pygame'ı kapat
pygame.quit()
sys.exit()
