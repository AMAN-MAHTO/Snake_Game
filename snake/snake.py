
# these is a snake game code

# here to many intretting code are written but in a comment
# so if you want to explore it just uncomment them
# if you use the music code to add music then also remembre your music file and these file are at same place


import pygame
import random
import os
import sys

current_path=os.path.dirname(sys.argv[0]).replace('/','\\\\')

pygame.mixer.init()

pygame.init()


# gamewindow
screen_width = 600
screen_height = 500
gamewindow=pygame.display.set_mode((screen_width,screen_height))
# game title
pygame.display.set_caption('Snake.Aman_code')

# image
bgimg= pygame.image.load(f"{current_path}\\bgi.png")
bgimg= pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# colours
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0,0,200)

clock = pygame.time.Clock()

# score font
font = pygame.font.SysFont(None, 55)
def score_screen(text, colour, x, y ):
    score_text = font.render(text, True, colour)
    gamewindow.blit(score_text, [x,y])

def plot_snk(gamewindow, color, snk_list ,snake_size,):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    pygame.mixer.music.load(f"{current_path}\\music.mp3")     
    pygame.mixer.music.play()
    while not exit_game:
        if pygame.mixer.music.get_busy()==0:
            pygame.mixer.music.load(f"{current_path}\\music.mp3")     
            pygame.mixer.music.play()
        
        gamewindow.blit(bgimg, (0, 0))
        score_screen("Welcome To Snakes", red, 100, 175)
        score_screen("Press Enter To Play", red, 100, 225)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        clock.tick(60)
        pygame.display.update()
#game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()

    while not exit_game:

        if game_over:
            with open("highscore.txt", "w") as f:
                 f.write(str(highscore))
            if pygame.mixer.music.get_busy()==0:
                    pygame.mixer.music.load(f"{current_path}\\music.mp3")     
                    pygame.mixer.music.play()
            gamewindow.blit(bgimg, (0, 0))
            score_screen("Game Over!.. ", red, 50, 200)
            score_screen("Press Enter to continue",red ,50 ,250)
            score_screen("Score: " + str(score), red, 50, 150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y =0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0


                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0  

                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score += 10
                snk_length += 5
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)

            if pygame.mixer.music.get_busy()==0:
                pygame.mixer.music.load(f"{current_path}\\music.mp3")     
                pygame.mixer.music.play()

            if int(highscore) <= score:
                highscore = score
            snake_y += velocity_y
            snake_x += velocity_x
            gamewindow.fill(black)
            

            # pygame.mixer.music.load("C:\\Users\\ashok mahato\\Desktop\\programing\\files\\game file\\snake\\music2.mp3")               # music code for play music during playing game
            # pygame.mixer.music.play()                           # and add your music file name

            score_screen("Score: "+str(score)+"  Highscore: "+ str(highscore) , white, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size] )

            #pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]


            if head in snk_list[:-1]:
                game_over = True
                if pygame.mixer.music.get_busy()==0:
                    pygame.mixer.music.load(f"{current_path}\\music.mp3")     
                    pygame.mixer.music.play()

            plot_snk(gamewindow, green, snk_list, snake_size)

            #codes for make boundery as a wall

            #if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                #game_over = True
                #pygame.mixer.music.load("music2.mp3")                          #music code for game over
                #pygame.mixer.music.play()
            
            #code to make boundery invisible
            if snake_x < 5:
                snake_x = screen_width-5
            if snake_x > screen_width-5:
                snake_x = 5
            if snake_y < 5:
                snake_y = screen_height-5
            if snake_y > screen_height-5:
                snake_y = 5

        clock.tick(60)
        pygame.display.update()

    pygame.quit()
    quit()
welcome()


