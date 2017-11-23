# Color Settings
BLACK       = ( 53,  53,  53) # Not absolute black to make it easier on the eyes.
WHITE       = (202, 202, 202) # Not absolute white to make it easier on the eyes.
RED         = (255,  78,  78)
YELLOW      = (255, 255,   0)
BG_COLOR_1  = (126,  87,  78) # Background colour 1
BG_COLOR_2  = (237, 221, 204) # Background colour 2
GOLD        = (238, 232, 170) # The King colour trim.
PIECECOLOR  = [RED, BLACK, WHITE, WHITE]

# Game Settings
FPS = 30
TITLE     = "COMP 4752 - Checkers"
TILESIZE  = 80 # used to draw the board.
PIECEPAD    = 5
# Font settings
FONTNAME  = "monospace"
FONTSIZE  = 30
FONTBOLD  = True


# Lists containing the default positions of red/black checker locations
STARTING_RED_POSITIONS = [(0,1), (0,3), (0,5), (0,7), (1,0), (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (2,7) ]
STARTING_BLACK_POSITIONS = [ (7,0), (7,2), (7,4), (7,6), (6,1), (6,3), (6,5), (6,7), (5,0), (5,2), (5,4), (5,6) ]

# Lists containing positions where red/black pieces can become king
RED_CAN_BECOME_KING = [(7,0), (7,2), (7,4), (7,6)]
BLACK_CAN_BECOME_KING = [(0,1), (0,3), (0,5), (0,7)]

# All the legal actions a red piece can do.
LEGAL_RED_ACTIONS = [ (1, -1), (1, 1) ]

# All the legal actions a black piece can do.                        
LEGAL_BLACK_ACTIONS = [ (-1, 1), (-1, -1) ]

# All the legal actions a red/black king piece can do
LEGAL_KING_ACTIONS = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

# Checkers Settings. Only PIECEPAD, BOARD_ROWS and BOARD_COLS are used right now for 
# graphics stuff. Other settings will be to actual make it a game later.
PLAYER_ONE  = 0
PLAYER_TWO  = 1
PLAYER_NONE = 2
DRAW        = 3
BOARD_ROWS  = 8
BOARD_COLS  = 8

# Result strings for when player wins.
PLAYER_NAMES = ["Player One", "Player Two", "Player None", "Draw"]
GAME_RESULT_STRING = ["Player One Wins!", "Player Two Wins!", "Game In Progress", "Game is a Draw!"]

# A list of Arrays that have starting positions for debugging. Insert them into the init function red_piece_list and black_piece_list to test them out.

# This defines a state in which a red piece can jump over a black piece.
RED_CAN_JUMP_POSITION_R = [(0,1), (2,3)]
RED_CAN_JUMP_POSITION_B = [(7,0), (3,4)]

# This defines a state in which a black piece can jump over a red piece after the (2,3) 
# red piece moves to the left or right.
BLACK_CAN_JUMP_POSITION_R = [(0,1), (2,3)]
BLACK_CAN_JUMP_POSITION_B = [(7,0), (4,3)]

# Positions where red can jump 2 times.
RED_CAN_JUMPX2_POSITION_R = [(0,1), (0,3)]
RED_CAN_JUMPX2_POSITION_B = [(7,0), (1,4), (3,4), (3,6)]

# Positions where red can jump 3 times.
RED_CAN_JUMPX3_POSITION_R = [(0,1), (0,3)]
RED_CAN_JUMPX3_POSITION_B = [(7,0), (1,4), (3,4), (5,4)]

# Positions where red can become king
RED_CAN_BECOME_KING_R = [(6,1), (6,3), (6,5), (6,7)]
RED_CAN_BECOME_KING_B = [(5,2)]
RED_CAN_BECOME_KING_KING_LIST_R = [(6,1), (6,3)]

# Positions where black can become king
BLACK_CAN_BECOME_KING_R = [(2,3)]
BLACK_CAN_BECOME_KING_B = [(1,0), (1,2), (1,4), (1,6)]
BLACK_CAN_BECOME_KING_KING_LIST_B = [(1,0), (1,2)]

# Positions where black AI will always jump
BLACK_AI_WILL_JUMP_R = [(2,5), (1,0)]
BLACK_AI_WILL_JUMP_B = [(4,3), (6,5)]
BLACK_AI_WILL_JUMP_B_KING_LIST = [(1,0), (1,2)]




