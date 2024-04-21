import pygame
from sys import exit
from random import randint, choice
from maze_generator import *
import time


FPS = 60
t0 = 60
pygame.init()
helvetica = pygame.font.Font('helvetica-255/Helvetica-Bold.ttf', 35)
helveticasmall = pygame.font.Font('helvetica-255/Helvetica-Bold.ttf', 20)
helveticasmaller = pygame.font.Font('helvetica-255/Helvetica-Bold.ttf', 15)
bg_surface = pygame.image.load("StarrySky.png")
bg_surface = pygame.transform.scale2x(bg_surface)
game_surface = pygame.Surface((WIDTH, HEIGHT))
surface = pygame.display.set_mode((RES[0] , RES[1]+100))
pygame.display.set_caption("The Labyrinth")
clock = pygame.time.Clock()
game_active = False
main_menu = True
game_over = False
levels = False
levelchosen = 0
won = False
score = 0


# images

spacebg = pygame.image.load('Spacebg.jpeg').convert_alpha()
spacebg = pygame.transform.scale(spacebg, (WIDTH, HEIGHT))
player_img = pygame.image.load('astronaut.png').convert_alpha()
player_img = pygame.transform.rotozoom(player_img, 0, 0.1)
# player_img = pygame.transform.scale(player_img, (TILE - 10 * thickness, TILE - 10 * thickness))
player_rect = player_img.get_rect()
player_rect.center = RES[0] // 2, RES[1] // 2

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if game_active:
            if event.type == game_timer:
                game_active = False
                game_over = True
                levels = False
                main_menu = False
                
        elif main_menu:
            if event.type == pygame.MOUSEBUTTONDOWN and abs(pygame.mouse.get_pos()[0] - 300) <= 60 and abs(pygame.mouse.get_pos()[1] - 350) <= 25 :
                maze = generate_maze()
                # maze_locx = (RES[0])/2 - TILE/2
                # maze_locy = (RES[1])/2 - TILE/2
                maze_locx = (RES[0]-WIDTH)/2
                maze_locy = (RES[1]-HEIGHT)/2
                won = False
                game_active = True
                main_menu = False
                score = 0
                # start_time = pygame.time.get_ticks()/1000
                start_time=time.time()
                game_timer = pygame.USEREVENT + 1
                pygame.time.set_timer(game_timer,t0*1000)

            if event.type == pygame.MOUSEBUTTONDOWN and abs(pygame.mouse.get_pos()[0] - 300) <= 60 and abs(pygame.mouse.get_pos()[1] - 390) <= 25 :
                levels = True
                main_menu = False

        elif levels:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if y<=250:
                    if x>0 and x<=200:
                        levelchosen = 0
                        set_wh(1300,1300)
                    elif x>200 and x<=400:
                        levelchosen = 1
                        set_wh(1500,1500)
                    else:
                        levelchosen = 2
                        set_wh(1700,1700)
                if abs(x-300)<=100 and abs(y-450)<20:
                    main_menu = True
                    levels = False           
            
        elif game_over:
            if won:
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if abs(pygame.mouse.get_pos()[0] - 300) <= 75 and abs(pygame.mouse.get_pos()[1] - 402.5) <= 15  :
                        maze = generate_maze()
                        maze_locx = (RES[0]-WIDTH)/2
                        maze_locy = (RES[1]-HEIGHT)/2
                        # maze_locx = (RES[0])/2 - TILE/2
                        # maze_locy = (RES[1])/2 - TILE/2
                        won = False
                        game_active = True
                        main_menu = False
                        score = 0
                        # start_time = pygame.time.get_ticks()/1000
                        start_time=time.time()
                        game_timer = pygame.USEREVENT + 1
                        pygame.time.set_timer(game_timer,t0*1000)

                    if abs(pygame.mouse.get_pos()[0] - 300) <= 75 and abs(pygame.mouse.get_pos()[1] - 444) <= 15  :
                        main_menu = True

            else:
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if abs(pygame.mouse.get_pos()[0] - 300) <= 112.5 and abs(pygame.mouse.get_pos()[1] - 407.5) <= 22.5  :
                        maze = generate_maze()
                        maze_locx = (RES[0]-WIDTH)/2
                        maze_locy = (RES[1]-HEIGHT)/2
                        # maze_locx = (RES[0])/2 - TILE/2
                        # maze_locy = (RES[1])/2 - TILE/2
                        won = False
                        game_active = True
                        main_menu = False
                        score = 0
                        # start_time = pygame.time.get_ticks()/1000
                        start_time=time.time()
                        game_timer = pygame.USEREVENT + 1
                        pygame.time.set_timer(game_timer,t0*1000)

                    if abs(pygame.mouse.get_pos()[0] - 300) <= 112.5 and abs(pygame.mouse.get_pos()[1] - 456) <= 22.5  :
                        main_menu = True


    if game_active:
        keys_pressed = pygame.key.get_pressed()
        bounce_back=5
        movement=5
        if keys_pressed[pygame.K_UP]:
            maze_locy += movement
            temp = [cell.get_rects(locx=maze_locx, locy=maze_locy) for cell in maze]
            walls_collide_list = []
            for x in temp:
                for y in x:
                    walls_collide_list.append(y)
            if player_rect.collidelist(walls_collide_list)!=(-1):
                maze_locy -= bounce_back
        elif keys_pressed[pygame.K_DOWN]:
            maze_locy -= movement
            temp = [cell.get_rects(locx=maze_locx, locy=maze_locy) for cell in maze]
            walls_collide_list = []
            for x in temp:
                for y in x:
                    walls_collide_list.append(y)
            if player_rect.collidelist(walls_collide_list)!=(-1):
                maze_locy += bounce_back
        elif keys_pressed[pygame.K_LEFT]:
            maze_locx += movement
            temp = [cell.get_rects(locx=maze_locx, locy=maze_locy) for cell in maze]
            walls_collide_list = []
            for x in temp:
                for y in x:
                    walls_collide_list.append(y)
            if player_rect.collidelist(walls_collide_list)!=(-1):
                maze_locx -= bounce_back
        elif keys_pressed[pygame.K_RIGHT]:
            maze_locx -= movement
            temp = [cell.get_rects(locx=maze_locx, locy=maze_locy) for cell in maze]
            walls_collide_list = []
            for x in temp:
                for y in x:
                    walls_collide_list.append(y)
            if player_rect.collidelist(walls_collide_list)!=(-1):
                maze_locx += bounce_back

        winx = RES[0]/2 + TILE/2 - WIDTH
        winy = RES[1]/2 + TILE/2 - HEIGHT
        if abs(maze_locx - winx) <= TILE/4 and abs(maze_locy - winy) <= TILE/4:
            won = True
            game_active = False
            levels = False
            game_over = True

        surface.blit(bg_surface, (0,0))
        surface.blit(game_surface, (maze_locx, maze_locy))
        game_surface.blit(spacebg, (0,0))
        [cell.draw(game_surface) for cell in maze]
        # rocket = pygame.image.load('rocket.png').convert_alpha()
        # rocket = pygame.transform.rotozoom(rocket, 45, 1)
        # game_surface.blit(rocket, (WIDTH, HEIGHT))
        surface.blit(player_img, player_rect)

        scoreboard = pygame.Rect((0,600),(600,100))
        pygame.draw.rect(surface, 'black', scoreboard)

        time_left = int(t0 - (int(time.time())-int(start_time))) 
        time_message = helvetica.render(f'Time left: {time_left}',False,'white')
        time_message_rect = time_message.get_rect(center = (150,650))
        score = int((t0 - ((time.time())-(start_time))) * 10) * 15
        score_msg = helvetica.render(f'Score: {score}', False, 'white')
        score_msg_rect = score_msg.get_rect(center = (450, 650))
        surface.blit(score_msg, score_msg_rect)
        surface.blit(time_message,time_message_rect)

    elif main_menu:
        bg = pygame.image.load('MainMenu.jpeg').convert_alpha()
        bg = pygame.transform.scale(bg,(RES[0], RES[1]+100))
        surface.blit(bg, (0,0))

    elif levels:
        # surface.fill('pink')
        levelspage = pygame.image.load('Levels.jpeg').convert_alpha()
        levelspage = pygame.transform.scale(levelspage, (RES[0], RES[1]+100))
        surface.blit(levelspage, (0,0))
        back = helvetica.render(f'Back to Menu',False,'black')
        back_rect = back.get_rect(center = (300,450))
        pygame.draw.rect(surface, 'white', back_rect)
        surface.blit(back,back_rect)
        if levelchosen == 0:
            box = pygame.image.load('WhiteBox.png').convert_alpha()
            box = pygame.transform.scale(box,(200, 250))
            surface.blit(box, (0,50))
        elif levelchosen == 1:
            box = pygame.image.load('WhiteBox.png').convert_alpha()
            box = pygame.transform.scale(box,(200, 250))
            surface.blit(box, (200,50))
        else:
            box = pygame.image.load('WhiteBox.png').convert_alpha()
            box = pygame.transform.scale(box,(200, 250))
            surface.blit(box, (400,50))

    elif game_over:

        if won:
            congrats = pygame.image.load('Congrats.jpeg').convert_alpha()
            congrats = pygame.transform.scale(congrats, (RES[0], RES[1]+100))
            score_msg = helveticasmaller.render(f'SCORE: {score}', False, '#f8fdff')
            score_msg_rect = score_msg.get_rect(center = (300, 370))
            
            surface.blit(congrats, (0,0))
            bgrect = pygame.Rect(265, 355, 70, 25)
            pygame.draw.rect(surface, '#1c2534', bgrect)
            surface.blit(score_msg, score_msg_rect)

        else:
            lost = pygame.image.load('Skill Issue.jpeg').convert_alpha()
            lost = pygame.transform.scale(lost, (RES[0], RES[1]+100))
            score_msg = helveticasmaller.render(f'SCORE: {score}', False, '#181818')
            score_msg_rect = score_msg.get_rect(center = (300, 360))
            
            surface.blit(lost, (0,0))
            bgrect = pygame.Rect(230, 345, 133, 25)
            pygame.draw.rect(surface, '#fcfcfc', bgrect)
            surface.blit(score_msg, score_msg_rect)

    pygame.display.flip()
    clock.tick(FPS)