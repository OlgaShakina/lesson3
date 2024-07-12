import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600))

pygame.display.set_caption("Игра Тир")
icon= pygame.image.load("images/3d33574fa603ff366e87dd06b942b713.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

running = True
while running:
    pass

pygame.quit()