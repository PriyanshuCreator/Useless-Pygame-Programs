import pygame
from os import listdir
pygame.init()

display_width = 560
display_height =  560
grey = (125,135,150)
white = (232,235,239)
blue =  (200,0,0)
blue_under_capture = (255,0,0)
block_size = 70
default_positions_filled = False
Present_piece_to_move = None
Last_piece_position = None
Positions_Pieces_under_attack = {}


# Loading Pieces Images
black_bishop = pygame.image.load('Pieces/black_bishop.png')
white_bishop = pygame.image.load('Pieces/white_bishop.png')

white_pawn = pygame.image.load('Pieces/white_pawn.png')
black_pawn = pygame.image.load('Pieces/black_pawn.png')

black_queen = pygame.image.load('Pieces/black_queen.png')
white_queen = pygame.image.load('Pieces/white_queen.png')

black_king = pygame.image.load('Pieces/black_king.png')
white_king = pygame.image.load('Pieces/white_king.png')

white_rook = pygame.image.load('Pieces/white_rook.png')
black_rook = pygame.image.load('Pieces/black_rook.png')

black_knight = pygame.image.load('Pieces/black_knight.png')
white_knight = pygame.image.load('Pieces/white_knight.png')



gameDisplay = pygame.display.set_mode((display_width,display_height))
gameClose = False


Pieces_position_dict = {}


def draw_chessboard():
    global Positions_dict_filled,Pieces_position_dict
    Pos_change = [0,70,140,210,280,350,420,490,560]
    present_board_color = grey
    for i in range(9):
        for j in range(9):
            if present_board_color == white:
                present_board_color = grey 
            else:
                present_board_color = white
            pygame.draw.rect(gameDisplay,present_board_color,pygame.Rect(Pos_change[i],Pos_change[j],70,70))
            
def Default_Place_pieces():
    global white_pawn_position_list
    white_pawn_position_list = [(70*i,420) for i in range(8)]
    black_pawn_position_list = [(70*i,70) for i in range(8)]
    
    Main_pieces_positions_black_list = [(70*i,0)  for i in range(8)]
    Main_pieces_positions_white_list = [(70*i,490)  for i in range(8)]

    Main_pieces_positioning_black = ['black_rook','black_knight','black_bishop','black_queen','black_king','black_bishop','black_knight','black_rook']
    Main_pieces_positioning_white = ['white_rook','white_knight','white_bishop','white_queen','white_king','white_bishop','white_knight','white_rook']  
    
    for i in white_pawn_position_list:
        Pieces_position_dict[(i,(i[0]+70,i[1] + 70))] = 'white_pawn'

    for i in black_pawn_position_list:
        Pieces_position_dict[(i,(i[0]+70,i[1] + 70))] = 'black_pawn'

    for i in range(len(Main_pieces_positions_black_list)):
        Pieces_position_dict[(Main_pieces_positions_black_list[i],(Main_pieces_positions_black_list[i][0]+70,Main_pieces_positions_black_list[i][1] + 70))] = Main_pieces_positioning_black[i]

    for i in range(len(Main_pieces_positions_white_list)):
        Pieces_position_dict[(Main_pieces_positions_white_list[i],(Main_pieces_positions_white_list[i][0]+70,Main_pieces_positions_white_list[i][1] + 70))] = Main_pieces_positioning_white[i]
    
    # Adding Remaining Positions to the Piece_position_dict
    ## Total 32 square boxes
    for i in range(2,6):
        for j in range(8):
            Pieces_position_dict[((70*j,70*i),(70*j + 70 , 70*i + 70))] = ''
    
        
def Present_board_state():
    for Position,Piece in Pieces_position_dict.items():
        
        if Piece and Piece != blue and Piece != blue_under_capture:
            gameDisplay.blit(eval(Piece),Position[0])
            
        elif Piece == blue :
            length = Position[1][0] - Position[0][0]
            breadth = Position[1][1]-Position[0][1]
            pygame.draw.rect(gameDisplay,blue,pygame.Rect(Position[0][0],Position[0][1],length,breadth))
        
        elif Piece == blue_under_capture:
            length = Position[1][0] - Position[0][0]
            breadth = Position[1][1]-Position[0][1]
            pygame.draw.rect(gameDisplay,blue,pygame.Rect(Position[0][0],Position[0][1],length,breadth))
            gameDisplay.blit(eval(Positions_Pieces_under_attack[Position]),Position[0])
                
 

def move_white_pawn():
    global Pieces_position_dict,Present_piece_to_move,Last_piece_position,Positions_Pieces_under_attack
    ## Checking if Capturing is Available or not
    
    pos_capture_a_1,pos_capture_b_1 = (Piece_Position[1][0],Piece_Position[0][1]-block_size),(Piece_Position[1][0]+block_size,Piece_Position[0][1])
    
    pos_capture_a_2,pos_capture_b_2 = (Piece_Position[0][0]-block_size,Piece_Position[0][1]-block_size),(Piece_Position[0][0],Piece_Position[0][1])
    
    Possible_capture = [(pos_capture_a_1,pos_capture_b_1),(pos_capture_a_2,pos_capture_b_2)]


    
    if Piece_Position[0] in white_pawn_position_list: 
        pos_a,pos_b = (Piece_Position[0][0],Piece_Position[0][1]-block_size*2),(Piece_Position[1][0],Piece_Position[0][1])
        Possible_moves_positions = [((pos_a[0],pos_a[1]),(pos_b[0],pos_b[1]-70)),((pos_a[0],pos_a[1]+70),(pos_b[0],pos_b[1]))]
        
    
    elif Piece_Position not in white_pawn_position_list:
        pos_a,pos_b = (Piece_Position[0][0],Piece_Position[0][1]-block_size),(Piece_Position[1][0],Piece_Position[0][1])
        Possible_moves_positions = [(pos_a,pos_b)]
    
    for Capture_pos in Possible_capture:
        try:
            Piece_present = Pieces_position_dict[Capture_pos]
        except KeyError:
            pass
         
        else:
            if Piece_present and Piece_present != blue and Piece_present != blue_under_capture:
                if Piece_present.split('_')[0] == 'black':
                    Pieces_position_dict[Capture_pos] = blue_under_capture
                    Possible_moves_positions.append(Capture_pos)
                    Positions_Pieces_under_attack[Capture_pos] = Piece_present
                    
            elif Piece_present == blue_under_capture:
                    Pieces_position_dict[Capture_pos] = blue_under_capture
                    Possible_moves_positions.append(Capture_pos)
                    Positions_Pieces_under_attack[Capture_pos] = Piece_present
                    

    for Possible_move in Possible_moves_positions:
        if Pieces_position_dict[Possible_move] == '':
            Pieces_position_dict[Possible_move] = blue
            

##    for Position,Piece in Pieces_position_dict.items():
##        if Position not in Possible_moves_positions and Pieces_position_dict[Position] == blue:
##        
##            Pieces_position_dict[Position] = ''
    

        
        
    Present_piece_to_move = 'white_pawn'
    Last_piece_position = Piece_Position
    
  
 
def Move_Pieces():
    global Pieces_position_dict,Piece_Position
    pos_x,pos_y = pygame.mouse.get_pos() 
    left_click = pygame.mouse.get_pressed()[0] 
    if left_click:
        for Piece_Position,piece in Pieces_position_dict.items():
            if Piece_Position[0][0] < pos_x and pos_x < Piece_Position[1][0] and Piece_Position[0][1] < pos_y and pos_y < Piece_Position[1][1]:
                if piece:
                    if piece == 'white_pawn':
                        return 'white_pawn'
                        
                    elif piece == blue:
                        
                        Pieces_position_dict[Piece_Position] = Present_piece_to_move
                        Pieces_position_dict[Last_piece_position] = ''
                        


                        
                        
        

            
                        
                    
                
            
        
       
     

while not gameClose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameClose = True
    piece_to_move = Move_Pieces()
    
    if piece_to_move == 'white_pawn':
        move_white_pawn()
        
    draw_chessboard()
    Present_board_state()
     
    if not default_positions_filled:
        Default_Place_pieces()
        default_positions_filled = True
    pygame.display.update()
   
print(Pieces_position_dict)
pygame.quit()
quit()
