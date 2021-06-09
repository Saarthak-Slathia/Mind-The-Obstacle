import pygame
import random
from pygame import mixer
import math

pygame.init()
# Variables
over_font = pygame.font.Font('Technology-Bold.ttf', 100)

# Images
background = pygame.image.load("road.png")
bg = pygame.transform.scale(background, (900, 600))
car = pygame.image.load("car.png")

# Sound
mixer.music.load("Soft-techno-music.mp3")
mixer.music.play(-1)

# Screen
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption(" Racing Car")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

# Enemy Car
enemy = []
enemyX = []
enemyY = []
enemyYchange = []
enemiesNum = 7

for i in range(enemiesNum):
    enemy.append(pygame.image.load("barrier.png"))
    enemyX.append(random.randint(200, 700))
    enemyY.append(600)
    enemyYchange.append(0)

over = pygame.image.load("over.jpg")
score_value = 0
font = pygame.font.Font('Technology-Italic.ttf', 30)
font2 = pygame.font.Font('Technology-BoldItalic.ttf', 50)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))

def show_score_total(x, y):
    score = font2.render("Score : " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))

def enemyfun(x, y, j):
    screen.blit(enemy[j], (x, y))

def isCollision(enemyX, enemyY, carX, carY):
    distance = math.sqrt(math.pow(enemyX - carX, 2) + (math.pow(enemyY - carY, 2)))
    if distance < 64:
        return True
    else:
        return False

# Car
carX = 370
carY = 350
carXchange = 0
carYchange = 0

def carfun(x, y):
    global car
    screen.blit(car, (x, y))

height = 600
i = 0
running = True
while running:
    clock = pygame.time.Clock()
    # clock.tick(10000)

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, i))
    screen.blit(bg, (0, height + i))

    if i == -height:
        screen.blit(bg, (0, height - i))
        i = 0

    i -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                carXchange = -5
            if event.key == pygame.K_RIGHT:
                carXchange = 5
            if event.key == pygame.K_UP:
                carYchange = -5
            if event.key == pygame.K_DOWN:
                carYchange = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                carXchange = 0
                carYchange = 0

    show_score(10, 10)
    carfun(carX, carY)

    for j in range(enemiesNum):
        enemyYchange[j] = 5
        if enemyY[j] < -10:
            enemyY[j] = random.randint(600, 800)
            score_value += 1
            enemyX[j] = random.randint(200, 700)

        collision = isCollision(enemyX[j], enemyY[j], carX, carY)
        if collision:
            screen.fill((252, 234, 0))
            over_text = over_font.render ("GAME OVER", True, (255, 255, 255))
            screen.blit(over_text, (250, 250))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carXchange = 0
                if event.key == pygame.K_RIGHT:
                    carXchange = 0
                if event.key == pygame.K_UP:
                    carYchange = 0
                if event.key == pygame.K_DOWN:
                    carYchange = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        carXchange = -5
                    if event.key == pygame.K_RIGHT:
                        carXchange = 5
                    if event.key == pygame.K_UP:
                        carYchange = -5
                    if event.key == pygame.K_DOWN:
                        carYchange = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        carXchange = 0
                        carYchange = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    carXchange = 0
                    carYchange = 0
            break


        enemyfun(enemyX[j], enemyY[j], j)
        enemyY[j] -= enemyYchange[j]

    carX += carXchange
    carY += carYchange
    clock.tick(100)
    pygame.display.update()
