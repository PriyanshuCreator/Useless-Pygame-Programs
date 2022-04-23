import pygame 
pygame.init()
from itertools import combinations as cbs
from time import sleep
from random import randint
display_height = 540
display_width = 540

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
aqua = (0,255,255)

colors = [black,white,red,green,blue,yellow,magenta,aqua]

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tic-Tac-Toe')
clock = pygame.time.Clock()
FPS = 30


X_image = pygame.image.load('X.png')
O_image = pygame.image.load('O.png')
O_image_hover = pygame.image.load('O_hover.png')
X_image_hover = pygame.image.load('X_hover.png')
black_screen = pygame.image.load('black_screen.png')
logo = pygame.image.load('logo.png')


pygame.display.set_icon(logo)

    
all_positions = [[15,15],[195,15],[375,15],[15,195],[195,195],[375,195],[15,375],[195,375],[375,375]] # These are arranged in order
possible_win_sequences = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(2,4,6),(3,4,5),(6,7,8)]
possible_win_sequences = [[all_positions[j] for j in i] for i in possible_win_sequences]




def text_objects(msg,color,font_size,font_name='comicsansms'):
    font = pygame.font.SysFont(font_name,font_size)
    textSurface = font.render(msg, True , color)
    return textSurface,textSurface.get_rect()
    
    
def message_to_screen_Center(msg,color,font_size,y_displace=0,font_name = None,x_displace = 0):
    textSurf,textRect = text_objects(msg,color,font_size,font_name)
    textRect.center = (display_width/2)+x_displace,(display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)

def button():
    global present_turn , Images_on_board
    pos_x , pos_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if 0 < pos_x < 180 and 0 < pos_y < 180:
        hover_pos = all_positions[0]
        
    elif 180 < pos_x < 360 and 0 < pos_y < 180:
        hover_pos = all_positions[1]
        
    elif 360 < pos_x < 540 and 0 < pos_y < 180:
        hover_pos = all_positions[2]
        
    elif 0 < pos_x < 180 and 180 < pos_y < 360:
        hover_pos = all_positions[3] 
        
    elif 180 < pos_x < 360 and 180 < pos_y < 360:
        hover_pos = all_positions[4]
            
    elif 360 < pos_x < 540 and 180 < pos_y < 360:
        hover_pos = all_positions[5]
        
    elif 0 < pos_x < 180 and 360 < pos_y < 540:
        hover_pos = all_positions[6] 
        
    elif 180 < pos_x < 360 and 360 < pos_y < 540:
        hover_pos = all_positions[7]
            
    elif 360 < pos_x < 540 and 360 < pos_y < 540:
        hover_pos = all_positions[8]
     
        
        
    try:
        if hover_pos not in positions_occupied:         
            if present_turn == 'O':
                gameDisplay.blit(O_image_hover,hover_pos)
            else:
                gameDisplay.blit(X_image_hover,hover_pos)
                
    except UnboundLocalError:
        pass
           
    finally:
        if click[0]:
            if hover_pos not in positions_occupied:
                positions_occupied.append(hover_pos)
                if present_turn == 'O':
                    Images_on_board.append(['O',hover_pos])
                    O_positions_occupied.append(hover_pos)
                    present_turn = 'X'
                else:                
                    Images_on_board.append(['X',hover_pos])
                    X_positions_occupied.append(hover_pos)
                    present_turn = 'O'
                    
 
def check_win():
     global Images_on_board,positions_occupied
     Possible_Player_X_Win = [all([i in X_positions_occupied for i in j]) for j in possible_win_sequences]
     Possible_Player_O_Win = [all([i in O_positions_occupied for i in j]) for j in possible_win_sequences]
     
     if any(Possible_Player_O_Win):
         Winning_position = [i for i in cbs(O_positions_occupied,3) if sorted(i) in [sorted(j) for j in possible_win_sequences]][0]
         for i in positions_occupied:
             if i not in Winning_position:                
                 if i in X_positions_occupied:                    
                     gameDisplay.blit(black_screen,i)
                 else:
                     gameDisplay.blit(black_screen,i)
             
         message_to_screen_Center('O Wins!!',red,150,x_displace = 0 , y_displace = 0)
         message_to_screen_Center("Press Q to Quit and C to Play Again",red,40,x_displace = 20, y_displace = 150)
         positions_occupied = [i for i in all_positions]
         return True
           
     elif any(Possible_Player_X_Win):
         Winning_position = [i for i in cbs(X_positions_occupied,3) if sorted(i) in [sorted(j) for j in possible_win_sequences]][0]
         for i in positions_occupied:
             if i not in Winning_position:                
                 if i in X_positions_occupied:                    
                     gameDisplay.blit(black_screen,i)
                 else:
                     gameDisplay.blit(black_screen,i)
         message_to_screen_Center('X Wins!!',red,150,x_displace = 0 , y_displace = 0)
         message_to_screen_Center("Press Q to Quit and C to Play Again",red,40,x_displace = 20, y_displace = 150)
         positions_occupied = [i for i in all_positions]
         return True
         
     elif len(positions_occupied) == len(all_positions):  
         for i in positions_occupied:  
             if i in X_positions_occupied:            
                 gameDisplay.blit(black_screen,i)
             else:     
                 gameDisplay.blit(black_screen,i)
         message_to_screen_Center("It's a Draw!!",red,130,x_displace = 0 , y_displace = 0)
         message_to_screen_Center("Press Q to Quit and C to Play Again",red,40,x_displace = 20, y_displace = 150)
         return True
         
         
                 


    
def draw_board():
    pygame.draw.line(gameDisplay,white,(0,180),(540,180),5)
    pygame.draw.line(gameDisplay,white,(0,360),(540,360),5)
    pygame.draw.line(gameDisplay,white,(180,0),(180,540),5)
    pygame.draw.line(gameDisplay,white,(360,0),(360,540),5)
    
    for i in Images_on_board:
        if i[0] == 'O':
            gameDisplay.blit(O_image,i[1])
        else:
            gameDisplay.blit(X_image,i[1])

# def jittery_effect():
    # pos_x , pos_y = pygame.mouse.get_pos()
    # click = pygame.mouse.get_pressed()
    # for i in range(10):     
        # pygame.draw.circle(gameDisplay,colors[randint(0,7)],(pos_x + randint(-30,30),pos_y + randint(-30,30)),randint(1,5))

def main():
    global present_turn,Images_on_board,positions_occupied,X_positions_occupied,O_positions_occupied
    
    present_turn = 'O'
    Win_check = False
    Images_on_board = []
    positions_occupied = []
    X_positions_occupied = []
    O_positions_occupied = []
    gameOver = False 
    while not gameOver:

        for event in pygame.event.get(): 
     
            if event.type == pygame.QUIT:
                gameOver = True 
            if Win_check:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                    elif event.key == pygame.K_c:
                        main()
                
        gameDisplay.fill(black)
        draw_board() 
        button()
        # jittery_effect()  
        Win_check = check_win()    
        clock.tick(FPS)
        pygame.display.update()

         
    pygame.quit()
    quit()
main()