import pygame
import numpy as np

WIDTH = 256
HEIGHT = 256
SCALE = 4

pygame.init()

screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
clock = pygame.time.Clock()

frame = 0
running = True

def CreateFrame(offset):

    framebuffer = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            r = int((x / (WIDTH - 1))*255) + offset
            g = int((y / (HEIGHT - 1))*255) + offset

            framebuffer[y, x] = [g % 256, r % 256, 0]

    return(framebuffer)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frameBuffer = CreateFrame(frame)

    surface = pygame.surfarray.make_surface(frameBuffer)

    scaled = pygame.transform.scale(surface, (WIDTH * SCALE, HEIGHT * SCALE))

    screen.blit(scaled, (0, 0))

    pygame.display.flip()

    frame += 1
    clock.tick(60)

pygame.quit()