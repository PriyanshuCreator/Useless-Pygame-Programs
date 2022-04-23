
import pygame

# You can try reducing the speed of the particles so that multiple particles do not collide at a single position
import random
pygame.init()

display_width = 600
display_height = 600

MainWindow = pygame.display.set_mode((display_width, display_height))

fps = 60
clock = pygame.time.Clock()


colours_list = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),
                (255, 255, 0), (65, 105, 225), (245, 222, 179), (210, 105, 30), (205, 133, 63)]


def text_objects(msg,color,font_size,font_name):
    font = pygame.font.SysFont(font_name,font_size)
    textSurface = font.render(msg, True , color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg, color, X, Y, font_size):
    font = pygame.font.SysFont("Comicsans", font_size)
    screen_text = font.render(msg, True, color)
    MainWindow.blit(screen_text, [X, Y])

def message_to_screen_Center(msg,color,font_size,y_displace=0,font_name = None,x_displace = 0):
    textSurf,textRect = text_objects(msg,color,font_size,font_name)
    textRect.center = (display_width/2)+x_displace,(display_height/2) + y_displace
    MainWindow.blit(textSurf,textRect)

# def check_gameover():
    
#     while gameover:
#         for event in pygame.event.get():
#             if event.type == pygame.quit():
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     main()

#         message_to_screen("You Lose!",(255,0,0),230,230,30)
#         message_to_screen("Press Up Key to play again",(0,255,0),200,200,20)
        
#         pygame.display.update()
#         clock.tick(5)
    
def main():
    gameover = False
    pause = False
    gamewin = False
    Score = 0
    mainloop = True
    max_width = display_width - 50
    max_height = display_height - 50
    collision_radius = 20
    max_speed_x = 8
    max_speed_y = 8
    size_x = 10
    size_y = 10
    particles_amount = 30
    user_size_x = 20
    user_size_y = 20

    particles_color = [random.choice(colours_list[:3])
                       for i in range(particles_amount)]
    particles_speed = [[random.randint(1, max_speed_x), random.randint(
        1, max_speed_y)] for i in range(particles_amount)]
    particles_position = [[random.randint(1, max_width), random.randint(
        1, max_height)] for i in range(particles_amount)]

    user_ball_position = random.choice(particles_position)
    ball_remove_pos = particles_position.index(user_ball_position)
    user_ball_color = particles_color[ball_remove_pos]
    user_ball_speed = particles_speed[ball_remove_pos]


    user_ball_shadow_var = 0
    user_ball_shadow_max = 5
    

    particles_position.remove(user_ball_position)
    particles_speed.remove(user_ball_speed)
    particles_color.remove(user_ball_color)

    win_score = len([i for i in particles_color if i == user_ball_color ])

   

    while mainloop:
        if gamewin == True:
            message_to_screen_Center("You Won",(255,0,0),70)
            message_to_screen_Center("Press UP Key to Play Again",(0,255,0),40,y_displace = 70)
            pygame.display.update()
        while gamewin == True:     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mainloop = False
                        gamewin = False
                        main()

        if gameover == True:
            message_to_screen_Center("Game Over",(255,0,0),70)
            message_to_screen_Center("Press UP Key to Play Again",(0,255,0),40,y_displace = 70)
            pygame.display.update()
        while gameover == True:     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mainloop = False
                        gameover = False
                        main()

        if pause == True:
            message_to_screen_Center("Paused",(0,255,0),50)
            pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if  event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False

        mouse_position = pygame.mouse.get_pos()
        if user_ball_position[0] > mouse_position[0]:
            if not abs(user_ball_position[0] - mouse_position[0]) <= 5:
                user_ball_position[0] -= 5

        else:
            if not abs(user_ball_position[0] - mouse_position[0]) <= 5:
                user_ball_position[0] += 5

        if user_ball_position[1] > mouse_position[1]:
            if not abs(user_ball_position[1] - mouse_position[1]) <= 5:
                user_ball_position[1] -= 5

        else:
            if not abs(user_ball_position[1] - mouse_position[1]) <= 5:
                user_ball_position[1] += 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
    ##    keys = pygame.key.get_pressed()
    ##
    # if keys[pygame.K_UP]:
    ##       user_ball_position[1] -= move_amount
    ##
    # elif keys[pygame.K_DOWN]:
    ##       user_ball_position[1] += move_amount
    ##
    # elif keys[pygame.K_LEFT]:
    ##       user_ball_position[0] -= move_amount
    ##
    # elif keys[pygame.K_RIGHT]:
    ##       user_ball_position[0] += move_amount

        MainWindow.fill((0, 0, 0))

        for i in range(len(particles_position)):
            pygame.draw.circle(
                MainWindow, particles_color[i], particles_position[i], size_x, size_y)

     # Making the Particle Show on Screen
        pygame.draw.circle(MainWindow, (255, 255, 255), user_ball_position,
                           user_size_x + user_ball_shadow_var, user_size_y + user_ball_shadow_var)
        pygame.draw.circle(MainWindow, user_ball_color,
                           user_ball_position, user_size_x, user_size_y)

        message_to_screen(f"Score : {Score}", (255, 255, 0), 10, 10, 30)

        for i in range(len(particles_position)):

            new_pos_x = particles_position[i][0] + particles_speed[i][0]
            new_pos_y = particles_position[i][1] + particles_speed[i][1]

            if new_pos_x >= display_width or new_pos_x <= 0:
                particles_speed[i][0] = -particles_speed[i][0]

            else:
                particles_position[i][0] = new_pos_x

            if new_pos_y >= display_height or new_pos_y <= 0:
                particles_speed[i][1] = -particles_speed[i][1]
            else:
                particles_position[i][1] = new_pos_y

        user_ball_shadow_var += 1
        if user_ball_shadow_var > user_ball_shadow_max:
            user_ball_shadow_var = 0

        for b, a in enumerate(particles_position):
            if abs(user_ball_position[0]-particles_position[b][0]) <= collision_radius and abs(user_ball_position[1]-particles_position[b][1]) <= collision_radius:

                if particles_color[b] == user_ball_color:
                    particles_position.pop(b)
                    particles_speed.pop(b)
                    particles_color.pop(b)
                    user_size_x += 10
                    user_size_y += 10
                    collision_radius += 10
                    Score += 1

                else:
                    particles_position.pop(b)
                    particles_speed.pop(b)
                    particles_color.pop(b)
                    user_size_x -= 10
                    user_size_y -= 10
                    collision_radius -= 10

        if collision_radius == 0:
            gameover = True

        if Score == win_score:
            gamewin = True

        pygame.display.update()
        clock.tick(fps)




main()
