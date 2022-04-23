import pygame
import random
import time
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
game_icon = pygame.image.load('icon.png')
pygame.display.set_icon(game_icon)
display_height = 600
display_width =  800
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
FPS = 20
direction = "right"
Text_font = 'comicsansms'
gameDisplay = pygame.display.set_mode((display_width,display_height))
img = pygame.image.load('Snake_head.png')
background_image_start = pygame.image.load('background.jpg')
apple_image = pygame.image.load('apple.png')
block_size = 20
pygame.display.set_caption("Saanp ki Daud")
Score_board = [0]

clock = pygame.time.Clock()

def food_pos():
    food_pos_x = round(random.randrange(block_size,display_width - block_size)/block_size)*block_size
    food_pos_y = round(random.randrange(block_size,display_height - block_size)/block_size)*block_size
    return food_pos_x,food_pos_y

def pause():
    paused = True
    message_to_screen_Center('Game Paused',white,60,y_displace = -100,font_name = Text_font)
    message_to_screen_Center("Press C to Continue or Q to Quit",red,40,y_displace = 25,font_name = Text_font)
    pygame.display.update()
    clock.tick(5)
  
    while paused:
        pygame.mixer.music.pause()
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    

    
    
    
def game_intro():
    global intro
    pygame.mixer.music.pause()
    intro = True
    while intro:
        gameDisplay.blit(background_image_start,[0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


                
        message_to_screen_Center("Welcome to Snake Game",red,60,y_displace = -250,font_name = Text_font)
        message_to_screen_Center("Game Instructions :- ",green,40,y_displace =
        -150,font_name = Text_font)
        message_to_screen_Center("1.) The Objective of the Game is to eat red Apples",black,30,-80,x_displace=-100)
        message_to_screen_Center("2.) The More Apples you eat the more longer you get",black,30,-10,x_displace=-100)   
        message_to_screen_Center("3.) If you run into yourself or the Edges you Die",black,30,60,x_displace=-100)
        message_to_screen_Center("Press C to Play ,P to Pause and Q to Quit",green,30,y_displace = 190,font_name = Text_font,x_displace = -60)
        
        pygame.display.update()
        clock.tick(FPS)



def snake(block_size,snake_list):  
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
    
    gameDisplay.blit(head , tuple(snake_list[-1]))
    for XnY in snake_list[:-1]:
        gameDisplay.fill(green , rect = [XnY[0],XnY[1],block_size,block_size])
     
    

def message_to_screen(msg,color,X,Y,font_size,font_name = None):
    font = pygame.font.SysFont(font_name,font_size) 
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text , [X,Y])

def text_objects(msg,color,font_size,font_name):
    font = pygame.font.SysFont(font_name,font_size)
    textSurface = font.render(msg, True , color)
    return textSurface,textSurface.get_rect()
    
def message_to_screen_Center(msg,color,font_size,y_displace=0,font_name = None,x_displace = 0):
    textSurf,textRect = text_objects(msg,color,font_size,font_name)
    textRect.center = (display_width/2)+x_displace,(display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)
    
def gameLoop():
    global direction
    gameExit = False 
    gameOver = False
    direction = 'right'
    snake_pos_x = display_width / 2
    snake_pos_y = display_height / 2
    snake_list = []
    Change_pos_x = block_size
    Change_pos_y = 0
    snake_length = 1
    Score = 0
    food_pos_x,food_pos_y = food_pos() 
    if len(Score_board) < 2:
        game_intro()
    pygame.mixer.music.play()
    while not gameExit:
        if gameOver == True:
            pygame.mixer.music.pause()
            message_to_screen_Center("GAME OVER!",red,60,y_displace = -50,font_name = Text_font)
            message_to_screen_Center("Press Q to quit and C to Play again",white,30,y_displace = 50 , font_name = Text_font)
            pygame.display.update()
        while gameOver == True:     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False 
                    elif event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Change_pos_x = -block_size
                    Change_pos_y = 0
                    direction = 'left'
                    
                elif event.key == pygame.K_RIGHT:
                    Change_pos_x = block_size
                    Change_pos_y = 0
                    direction = 'right'
                    
                elif event.key == pygame.K_UP:
                    Change_pos_y = -block_size
                    Change_pos_x = 0
                    direction = 'up'
                    
                elif event.key == pygame.K_DOWN:
                    Change_pos_y = block_size
                    Change_pos_x = 0
                    direction = 'down'
                
                elif event.key == pygame.K_p:
                    pause()
                    

                
            
        if snake_pos_x >= display_width or snake_pos_x < 0 or snake_pos_y >= display_height or snake_pos_y < 0 :
            Score_board.append(Score)
            gameOver = True
            
        snake_pos_x += Change_pos_x
        snake_pos_y += Change_pos_y
        
        gameDisplay.fill(black)
        
        snake_head = []
        snake_head.append(snake_pos_x)
        snake_head.append(snake_pos_y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for eachSegment in snake_list[:-1]:
            if eachSegment == snake_head:
                Score_board.append(Score)
                gameOver = True
        
        snake(block_size,snake_list)
        gameDisplay.blit(apple_image,[food_pos_x , food_pos_y])
        message_to_screen(f"Score : {Score}",red,10,10,25,font_name = Text_font)
        message_to_screen(f"High Score : {max(Score_board)}",red,600,10,25,font_name = Text_font)
        pygame.display.update()
        
        
        
        if (snake_pos_x == food_pos_x and snake_pos_y == food_pos_y) or (abs(snake_pos_x-food_pos_x) < block_size and abs(snake_pos_y - food_pos_y) < block_size):
            food_pos_x,food_pos_y = food_pos() 
            snake_length += 1
            Score += 1
        pygame.mixer.music.unpause()
            
        clock.tick(FPS)
        
        

    pygame.quit()
    quit()
     

gameLoop()
