import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("images/3d33574fa603ff366e87dd06b942b713.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/target.png")
target_width = target_img.get_width()
target_height = target_img.get_height()

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
hits = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    screen.blit(target_img, (target_x, target_y))

    text_surface = font.render(f"Попаданий: {hits}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    pygame.display.update()

pygame.quit()