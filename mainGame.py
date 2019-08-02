import pygame
import random
import Bullet
import Player
import Enemy
import GameOver

pygame.init()

WHITE = (255,255,255)
font = pygame.font.Font('freesansbold.ttf', 20)

GameOverState = False

window_width = 800
window_height = 600
fps = 30
mainGameCounter = 0
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

all_sprites = pygame.sprite.Group()

bg = pygame.image.load('space_bg.jpg')
gameOver = GameOver.GameOver(window_width/2, window_height/2)

p = Player.Player(window_width/2, window_height-100)
all_sprites.add(p)

bullets = []
bullet_cooldown_max = 7
bullet_cooldown = bullet_cooldown_max

enemyStartList = []
enemies = []

score = 0
enemyReleaseRate = 30



def releaseEnemies():
    global enemies
    global all_sprites
    global enemyReleaseRate

    if mainGameCounter % 300 == 0 and mainGameCounter != 0 and enemyReleaseRate >= 0:
        enemyReleaseRate -= 5

    randomNumber = random.randint(0, enemyReleaseRate)

    if randomNumber == enemyReleaseRate:
        random_x_pos = random.randint(1, window_width)
        enemies.append(Enemy.Enemy(random_x_pos))
        all_sprites.add(enemies[-1])

def moveEnemies():
	for enemy_counter in range(0,len(enemies)):
		enemies[enemy_counter].moveDown()

def enemiesAtBottomOfScreen():
        enemyCounter = 0
        while enemyCounter < len(enemies):
            if enemies[enemyCounter].rect.top > window_height:
                enemies[enemyCounter].setState("Off Screen")

            enemyCounter += 1


def captureKeyboardInput():
    global bullet_cooldown
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        p.moveUp()
    if pressed[pygame.K_DOWN]:
        p.moveDown()
    if pressed[pygame.K_LEFT]:
        p.moveLeft()
    if pressed[pygame.K_RIGHT]:
        p.moveRight()
    if pressed[pygame.K_SPACE]:
        if bullet_cooldown >= bullet_cooldown_max and GameOverState == False:
            x_position = p.rect.centerx
            y_position = p.rect.centery
            bullets.append(Bullet.Bullet(x_position, y_position))
            all_sprites.add(bullets[-1])
            bullet_cooldown = 0

def checkBulletsHitEnemies():
        global enemies
        global bullets
        global score

        for enemyCounter in range(0, len(enemies)):
                for bulletCounter in range(0, len(bullets)):
                        if enemies[enemyCounter].rect.colliderect(bullets[bulletCounter]):
                                bullets[bulletCounter].setState("Dead")
                                enemies[enemyCounter].setState("Dead")

                                score = score + 1

def moveBullets():
    global bullet_cooldown
    bullet_counter = 0
    while bullet_counter < len(bullets):
        if bullets[bullet_counter].rect.bottom < 50:
            bullets[bullet_counter].setState("Off Screen")
            #bullet_counter -= 1
        else:
            bullets[bullet_counter].moveUp()

        bullet_counter += 1
    bullet_cooldown += 1

def checkPlayerPostion():
    if p.rect.right < 0:
            p.rect.right = window_width
    elif p.rect.left > window_width:
        p.rect.left = 0

    if p.rect.top < 0:
        p.rect.top = 0
    if p.rect.bottom > window_height:
        p.rect.bottom = window_height

def tidyActiveSprites():
    counter = 0
    global enemies

    while counter < len(enemies):
        if enemies[counter].getState() == "Dead" or enemies[counter].getState() == "Off Screen":
            enemies[counter].kill()
            enemies.remove(enemies[counter])
        counter += 1

    counter = 0
    while counter < len(bullets):
        if bullets[counter].getState() == "Dead" or bullets[counter].getState() == "Off Screen":
            bullets[counter].kill()
            bullets.remove(bullets[counter])
        counter += 1

    enemiesAtBottomOfScreen()

def checkGameOver():
    global p
    global enemies
    global all_sprites
    global GameOverState

    counter = 0
    if len(enemies) > 0:
        while counter < len(enemies):
            if enemies[counter].rect.colliderect(p):
                print("Game Over")
                p.kill()

                GameOverState = True

                for counter in range(0, len(bullets)):
                    bullets[counter].kill()

                all_sprites.add(gameOver)
                break
            counter += 1




def gameLoop():
    global bullet_cooldown
    global mainGameCounter
    gameState = True

    while gameState == True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameState = False

        captureKeyboardInput()

        #Game Logic
        releaseEnemies()
        moveEnemies()
        checkPlayerPostion()
        moveBullets()

        checkBulletsHitEnemies()
        tidyActiveSprites()
        checkGameOver()


        #Draw
        gameDisplay.blit(bg, (0, 0))
        all_sprites.draw(gameDisplay)

        scoreText = font.render("Score: " + str(score), True, WHITE)
        gameDisplay.blit(scoreText, (650, 30))

        pygame.display.update()
        clock.tick(fps)
        mainGameCounter += 1

        print(all_sprites)


print("Starting Game")
gameLoop()
