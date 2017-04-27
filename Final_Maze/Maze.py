# Imports//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import pygame
import intersects
from Walls import *
from Coins import *

# Initialize game engine///////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.init()


# Window//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
HEIGHT = 725
WIDTH = 1275
SIZE = (WIDTH, HEIGHT)
TITLE = "MAZE"

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)

END_SCREEN = pygame.image.load("START_SCREEN.jpg")
END_SCREEN = pygame.transform.scale(END_SCREEN, [1275, 725])
# Timer//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
clock = pygame.time.Clock()
refresh_rate = 60


# Colors//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
WHITE = (255, 255, 255)
GREEN = (68, 104, 4)
BLACK = (0, 0, 0)
RED = (68, 0, 0)

font = pygame.font.Font(None, 48)

# Make a player

player = [26, 26, 20, 20]
player_vx = 0
player_vy = 0
player_speed = 5

def update_coins(coins):
    for c in coins:
        if intersects.rect_rect(player, c):
            coins.remove(c)

    if len(coins) == 0:
        end_screen()

def end_screen():
    screen.blit(END_SCREEN, [0,0])

    done = True
    

def collision(player, walls):
    player[0] += player_vx #move horizontaly

    for w in walls:
        if intersects.rect_rect(player, w):
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    '''moves player in vertical direction'''
    player[1] += player_vy # move verticaly
    
    '''wall vertical collisions'''
    for w in walls:
        if intersects.rect_rect(player, w):
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]# Drawing Code
    
def draw_game():                
    screen.fill(BLACK)


    '''coin intersects'''
    update_coins(coins)

    for w in walls: #draw walls
        pygame.draw.rect(screen, GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, WHITE, c)


    pygame.draw.rect(screen, RED, player)

    # Update window
    pygame.display.update()
    clock.tick(refresh_rate)


# Game loop/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if up:
        player_vy = -player_speed
    elif down:
        player_vy = player_speed
    else:
        player_vy = 0

    if left:
        player_vx = -player_speed
    elif right:
        player_vx  = player_speed
    else:
        player_vx = 0

    collision(player, walls)
    
    draw_game()
    # Game Logic (Check for Collitions)
    ''' moves player in horizontal direction'''    

    '''wall horizontal collisions'''
    

    
    

# Close window and quit//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
pygame.quit()


    
