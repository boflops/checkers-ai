import sys
import pygame as pg
import logging
import Project_GameState
from settings import *

# What each module does
# sys - This will set the recursion limit so that algorithms won't run on forever.
# settings - This will import the settings file in the current directory.

# Importing the GameState which will be used purely as the GUI for the application. As it
# As it stands right now, we draw the GUI information from a mix of this file and
# the GameState. In the next update the DisplayState will have more of that responsibility.
from Project_GameState import GameState as DisplayState

# set which version of the GameState you will use for each Player in the game
from Project_GameState import GameState as P1GameState
from Project_GameState import GameState as P2GameState

# set which Player object you will use for each Player in the game
P1Player = Project_GameState.Player_AlphaBeta(1, 0)
P2Player = Project_GameState.Player_AlphaBeta(2, 0) # Project_GameState.Player_AlphaBeta(2, 0)

# The basic Checkers class.
class Checkers:
    # The init function where we initalize important information about pygame and checkers.
    def __init__(self):
        # print("+INITIALIZED77777+")
        pg.init() # This initializes pygame, must be done.
        pg.display.set_caption(TITLE) # Sets title of the window as defined in settings.
        self.clock = pg.time.Clock() # Used to set the FPS.
        self.display_state = DisplayState(BOARD_ROWS, BOARD_COLS) # Used to display the GUI
        self.width  = self.display_state.cols() * TILESIZE # Width of screen.
        self.height = self.display_state.rows() * TILESIZE + 40 # Height of screen.
        self.screen = pg.display.set_mode( (self.width, self.height) ) # Window Size.
        self.font = pg.font.SysFont(FONTNAME, FONTSIZE, bold=FONTBOLD) # Used later.
        self.winner = PLAYER_NONE # Won't need to worry about this for now.
        self.text_position = (10, self.height-35) # Used later.
        self.player_states = [P1GameState(BOARD_ROWS, BOARD_COLS), P2GameState(BOARD_ROWS, BOARD_COLS)]
        self.players = [P1Player, P2Player]

        # Variables used to create the checkerboard pattern background.
        self.flip_color = True # Used to switch background colors when drawing the board.

    # The main game update loop of the application
    def update(self):
        # This sets a limit on how fast our computers process the drawing code.\
        self.dt = self.clock.tick(FPS) / 1000
        self.do_turn()
        self.events() # This will check for any input.
        self.draw() # Draw everything on the screen.

    # This will draw everything on the screen.
    def draw(self):
        # Add another parameter for king color.
        self.draw_board() # Draw the basic checkerboard for the background.

        # Determine if there's a winner.
        player = self.display_state.player_to_move()
        if (self.winner == PLAYER_NONE):
            self.draw_text(PLAYER_NAMES[player] + (": Human" if self.players[player] == None else ": AI Thinking"), self.text_position, PIECECOLOR[player])
        else:    
            self.draw_text(GAME_RESULT_STRING[self.winner], self.text_position, PIECECOLOR[self.winner])
        
        self.draw_piece_list(self.screen, self.display_state.red_piece_list, RED, 2) # Draw all the red pieces.
        self.draw_piece_list(self.screen, self.display_state.black_piece_list, BLACK, 2) # Draw all the black pieces.

        # If a player has pressed down on a piece then highlight potential moves.
        self.draw_piece_list(self.screen, self.display_state.red_piece_potential_move_list, WHITE, 2) # Draw all potential red moves on board.
        self.draw_piece_list(self.screen, self.display_state.black_piece_potential_move_list, WHITE, 2) # Draw all potential red moves on board.
        pg.display.flip() # Paint the graphics to the screen.

    # This will draw the checkered background of the checkers screen.
    def draw_board(self):
        # This must always be reinitialized or else colors will constantly be flashing.
        self.flip_color = True
        self.screen.fill(BG_COLOR_1) # Fill the Background to BG Colour 2.
        
        # Draw all the tiles on the screen.
        # NOTE: We don't use drawrect to create a rectangle but we instead fill the part
        # of the screen(like paintbucket in MS Paint/Photoshop) to fill in the checkerboard
        # design.
        for c in range(self.display_state.cols()):
            for r in range(self.display_state.rows()):
                # Draw a colored tile on the screen depending on flip_color value.
                if (self.flip_color == True):
                    self.screen.fill(BG_COLOR_1, (c*TILESIZE, r*TILESIZE, TILESIZE*1, TILESIZE*1))
                    self.flip_color = False # Draw the next tile a different color.
                else:
                    self.screen.fill(BG_COLOR_2, (c*TILESIZE, r*TILESIZE, TILESIZE*1, TILESIZE*1))
                    self.flip_color = True # Draw the next tile a different color.

            # Flip the color again so the next column starts with a different color.
            self.flip_color = not self.flip_color 

    # This will draw a list of pieces on a board using a list of tuples.
    def draw_piece_list(self, surface, piece_list, color, border):
        # For every piece in given list, draw a piece at that row and column.
        for piece in piece_list:
            row, col = self.display_state.rows() - 1 - piece[0], piece[1]
            
            if (piece in self.display_state.red_king_piece_list) or (piece in self.display_state.black_king_piece_list):
                pg.draw.circle(surface, color, (col*TILESIZE+TILESIZE//2, row*TILESIZE+TILESIZE//2), TILESIZE//2-PIECEPAD)
                pg.draw.circle(surface, GOLD, (col*TILESIZE+TILESIZE//2, row*TILESIZE+TILESIZE//2), TILESIZE//2-PIECEPAD, border)
            else:
                pg.draw.circle(surface, color, (col*TILESIZE+TILESIZE//2, row*TILESIZE+TILESIZE//2), TILESIZE//2-PIECEPAD)

    # draw some text with the given arguments
    def draw_text(self, text, pos, color):
        label = self.font.render(text, 1, color)
        self.screen.blit(label, pos)
        
    # reset the game to a the default state board
    def reset(self):
        # print("Reset")
        self.winner = PLAYER_NONE
        self.display_state = DisplayState(BOARD_ROWS, BOARD_COLS)
        self.player_states[0] = P1GameState(BOARD_ROWS, BOARD_COLS)
        self.player_states[1] = P2GameState(BOARD_ROWS, BOARD_COLS)

    # This will execute a move when passed a new row/column location.
    def do_move(self, move):
        # print("about to do move")
        player = self.display_state.player_to_move()
        # print("do move player is ", player)
        # print("self.players[player] is ", self.players[player])
        # print("move is ", move)

        # This if statement is used to change the selected index to the one alpha beta
        # generated when it found the best move.
        if self.players[player] != None:
            # # print("AI temp_best_just_done_move is ", self.players[player].temp_best_just_done_move_B)
            # # print("AI self.players[player].temp_best_selected_piece is ", self.players[player].temp_best_selected_piece_B)
            # # print("AI self.players[player].temp_red_pieces_to_remove_list is ", self.players[player].temp_red_pieces_to_remove_list_B)
            # print("move is ", move)
            self.display_state.selected_piece =  self.players[player].temp_best_selected_piece_B
            self.player_states[0].selected_piece =  self.players[player].temp_best_selected_piece_B
            self.player_states[1].selected_piece =  self.players[player].temp_best_selected_piece_B

            # Updating the red pieces to remove list.
            self.display_state.red_pieces_to_remove_list = self.players[player].temp_red_pieces_to_remove_list_B
            self.player_states[0].red_pieces_to_remove_list = self.players[player].temp_red_pieces_to_remove_list_B
            self.player_states[1].red_pieces_to_remove_list = self.players[player].temp_red_pieces_to_remove_list_B

            # Updating the black pieces to remove list.
            self.display_state.black_pieces_to_remove_list = self.players[player].temp_black_pieces_to_remove_list
            self.player_states[0].black_pieces_to_remove_list = self.players[player].temp_black_pieces_to_remove_list
            self.player_states[1].black_pieces_to_remove_list = self.players[player].temp_black_pieces_to_remove_list
            

        # print("do move")
        # Check for winner and do move.
        self.winner = self.display_state.winner()
        self.display_state.do_move(move)
        self.player_states[0].do_move(move)
        self.player_states[1].do_move(move)

    # This function will do a basic move
    def do_turn(self):
        # # print("do turn")
        self.winner = self.display_state.winner()
        if self.winner == PLAYER_NONE:              # there is no winner yet, so get the next move from the AI
            player = self.display_state.player_to_move()    # get the next player to move from the state
            # # print("------ ", player)
            if self.players[player] != None:        # if the current player is an AI, get its move
                # print("About to do turn")
                
                if (player == 0):
                    # NOTE: If both uncommented, program will break.
                    # Uncomment out this line if you want a AB move.
                    # self.do_move(self.players[player].get_move(self.player_states[player])) # Get an alpha beta move.

                    # Uncomment out this line if you want a random move
                    self.do_move(self.players[player].get_random_move(self.player_states[player])) # Get a random move.
                elif (player == 1):
                    # NOTE: If both uncommented, program will break.
                    # Uncomment out this line if you want a AB move.
                    self.do_move(self.players[player].get_move(self.player_states[player])) # Get an alpha beta move.

                    # Uncomment out this line if you want a random move
                    # self.do_move(self.players[player].get_random_move(self.player_states[player])) # Get a random mov
                    
            
    # Returns the tile (r,c) on the grid underneath a given mouse position in pixels
    def get_tile(self, mpos):
        return (mpos[1] // TILESIZE, mpos[0] // TILESIZE)

    # This function will handle all user input handling.
    def events(self):
        # Loop through every event occuring.
        for event in pg.event.get():
            # If user hit the X button on window, then quit.
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
            # Check if a key is pressed down.
            if event.type == pg.KEYDOWN:
                # Reset board to starting state.
                if event.key == pg.K_r:      self.reset()
                
                # ALL DEBUGGING STUFF.
                # If left key pressed, move a black piece.
                if event.key == pg.K_LEFT:
                    print("LEFT")
                    # self.do_move_by_index(self.black_piece_list, 9, LEGAL_BLACK_ACTIONS[1])

                # If left key pressed, move a red piece.
                if event.key == pg.K_RIGHT:
                    print("RIGHT")
                    # self.do_move_by_index(self.red_piece_list, 9, LEGAL_RED_ACTIONS[1])

                # If D is pressed down, print debuging information
                if event.key == pg.K_d:
                    # print("Debugging is cool")
                    player = self.display_state.player_to_move()
                    # # print("-- random is ", self.players[0].get_random_move(self.player_states[player]))
                    # print("Display state red pieces are ", self.display_state.red_piece_list)

            # Check if a mousebutton is pressed down.
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    move = self.get_tile(event.pos)
                    repositioned_row = move[0] - (BOARD_ROWS - 1)
                    move = (abs(repositioned_row), move[1])
                    # print("Move pressed is ", move)

                    red_p_moves = self.display_state.red_piece_potential_move_list
                    black_p_moves = self.display_state.black_piece_potential_move_list
                    
                    # If player clicked on a potential move then go to that postion.
                    if ((move in red_p_moves or move in black_p_moves) and self.winner == PLAYER_NONE):
                        self.do_move(move)
                        continue

                    # If player didn't click on potential move then show them instead.
                    self.display_state.highlight_potential_moves(move)
                    self.player_states[0].highlight_potential_moves(move)
                    self.player_states[1].highlight_potential_moves(move)

# This is the main executable part of the program.
sys.setrecursionlimit(10000) # Can't go past 10000 recursive depth.

# This is the basic game object
game_object = Checkers()

# This is the "game loop" of the program, it is an infinite loop that runs the game.
while True:
    game_object.update()
                
