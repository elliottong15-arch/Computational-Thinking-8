from utils import * 

import pygame

set_background("underwater") 

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
self = create_sprite("fish", 0, 40)
time.sleep(1)

window.update()

def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
        self.rect.x += self.speed
    if keys[pygame.K_UP]:
        self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.rect.y += self.speed

window.update()