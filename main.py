import pygame
import time
import random

pygame.init()

white = (255,255,255)
yellow = (255,255,100)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

dis_w = 800
dis_h = 600
dis = pygame.display.set_mode((dis_w,dis_h))
pygame.display.set_caption('Игра змейка')
clock = pygame.time.Clock()
s_block = 10
s_speed = 15
font_style = pygame.font.SysFont('bahnschruft',25)
score_font = pygame.font.SysFont('comicsansms',35)

def Your_score(score):
    value = score_font.render('Ваш счёт:' + str(score),True,yellow)
    dis.blit(value,[0,0])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def mmmm(msg,color):
    mesg = font_style.render(msg, True,color)
    dis.blit(mesg,[dis_w/2,dis_h/2])

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_w/2
    y1 = dis_h/2
    x1_s = 0
    y1_s = 0
    snake_List = []
    len_of_snake = 1
    foodx = round(random.randrange(0,dis_w-s_block)/10.0)*10.0
    foody = round(random.randrange(0,dis_h-s_block)/10.0)*10.0
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            mmmm('Вы проиграли! Q - для выхода, C - для повотороения игры',red)
            Your_score(len_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key==pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_s = -s_block
                    y1_s = 0
                elif event.key==pygame.K_RIGHT:
                    x1_s = s_block
                    y1_s = 0
                elif event.key==pygame.K_UP:
                    y1_s = -s_block
                    x1_s = 0
                elif event.key==pygame.K_DOWN:
                    y1_s = s_block
                    x1_s = 0

        if x1>=dis_w or x1<0 or y1>=dis_h or y1<0:
            game_close = True
        x1 += x1_s
        y1 += y1_s
        dis.fill(blue)
        pygame.draw.rect(dis,green,[foodx,foody,s_block,s_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>len_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(s_block,snake_List)
        Your_score(len_of_snake-1)
        pygame.display.update()
        if x1 == foodx and y1==foody:
            foodx = round(random.randrange(0,dis_w-s_block)/10.0)*10.0
            foodx = round(random.randrange(0,dis_h-s_block)/10.0)*10.0
            len_of_snake+=1
        clock.tick(s_speed)
    pygame.quit()
    quit()
gameLoop()
