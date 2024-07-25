#!/usr/bin/env python

import pygame


pygame.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 640, 480

SPEED = 0
MAX_SPEED = 3

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.DOUBLEBUF)
screen = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.font.init()

# Create a list to hold sprites
sprites = []

# Define the Sprite class
class Sprite:
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

# Load the image and create the rect
image = pygame.image.load("images/car.png")
rect = image.get_rect()
rect.x = 10
rect.y = 10
car = Sprite(image, rect)
sprites.append(car)

def writeText():
    text = font.render(last_key_name, True, (255, 255, 255))
    screen.blit(text, (100, 100))

def update():
    screen.fill((0, 0, 0))
    for sprite in sprites:
        screen.blit(sprite.image, sprite.rect)
    display.blit(pygame.transform.scale(screen, (DISPLAY_WIDTH, DISPLAY_HEIGHT)), (0,0))
    pygame.display.flip()

# Set up font
font = pygame.font.Font(None, 70)

last_key_name = ""
last_key_copy = last_key_name

update()

keys = []

def handleInput(keys):
    global sprites
    global SPEED

    if pygame.K_LEFT in keys:
        if sprites[0].rect.x > 0:
            sprites[0].rect.x -= SPEED
    if SPEED < MAX_SPEED+1:
        SPEED += 0.2
        

    if pygame.K_RIGHT in keys:
        if sprites[0].rect.x < DISPLAY_WIDTH-sprites[0].rect.width:
            sprites[0].rect.x += SPEED
    if SPEED < MAX_SPEED+1:
        SPEED += 0.2


    if pygame.K_UP in keys:
        if sprites[0].rect.y > 0:
            sprites[0].rect.y -= SPEED
    if SPEED < MAX_SPEED+1:
        SPEED += 0.2


    if pygame.K_DOWN in keys:
        if sprites[0].rect.y < DISPLAY_HEIGHT-sprites[0].rect.height:
            sprites[0].rect.y += SPEED
    if SPEED < MAX_SPEED+1:
        SPEED += 0.2

    SPEED -= 0.1

    update()

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            else:
                if event.key not in keys:
                    keys.append(event.key)

        elif event.type == pygame.KEYUP:
            keys.remove(event.key)
            
    handleInput(keys)

# Quit Pygame
pygame.quit()


        
        #pressed = pygame.key.get_pressed()
        #if (pressed[pygame.K_a] or pressed[pygame.K_LEFT]) and self.player.position.x > 0:
        #    self.player.direction.x -= 1
        #    
        #if (pressed[pygame.K_d] or pressed[pygame.K_RIGHT]) and self.player.position.x < self.screen.get_width():
        #    self.player.direction.x += 1
        #    
        #if (pressed[pygame.K_w] or pressed[pygame.K_UP]) and self.player.position.y > 0:
        #    self.player.direction.y -= 1
        #    
        #if (pressed[pygame.K_s] or pressed[pygame.K_DOWN]) and self.player.position.y < self.screen.get_height():
        #    self.player.direction.y += 1
                
