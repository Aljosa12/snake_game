
import pygame
import time
import random
pygame.init()   # Initializes all of the imported Pygame modules


dis = pygame.display.set_mode((800, 600))   # Takes a tuple or a list as its parameter to create a surface (tuple preferred)
pygame.display.set_caption('Greatest Snake Game')   # Will set the caption text on the top of the display screen

# initialize few color variables
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

dis_width = 800
dis_height = 600

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

# --------------------------------------------------------------------------------------------------------------------------------------------


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [80, 280])

# --------------------------------------------------------------------------------------------------------------------------------------------


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0)
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0)

    # --------------------------------------------------------------------------------------------------------------------------------------------

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

            # --------------------------------------------------------------------------------------------------------------------------------------------

        for event in pygame.event.get():   # event.get() returns all actions that takes place
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change += 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

            # --------------------------------------------------------------------------------------------------------------------------------------------

            # we have to specify if snake reach border
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height:
                game_close = True

            # --------------------------------------------------------------------------------------------------------------------------------------------

            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)

            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

            pygame.display.update()

            # --------------------------------------------------------------------------------------------------------------------------------------------

            if x1 == foodx and y1 == foody:
                print("Yummy!!")
            clock.tick(snake_speed)

            # --------------------------------------------------------------------------------------------------------------------------------------------

    pygame.display.update()
    time.sleep(10)

    # --------------------------------------------------------------------------------------------------------------------------------------------

    pygame.quit()
    quit()

    # --------------------------------------------------------------------------------------------------------------------------------------------

gameLoop()

# --------------------------------------------------------------------------------------------------------------------------------------------
