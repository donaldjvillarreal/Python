'''
This file contains  functions that create
the game file used by the Game model
'''
import battle_board as bb
import game_pieces as gp

def prompt_place_piece(piece, piece_index, gameboard, team):
    '''
    prompts user to place a piece and ensures it can be placed
    at the ive x y location
    '''
    while True:
        print('Place your ' + piece.name)

        x = int(input('Row: '))
        y = int(input('Column: '))
        y2 = -1

        if piece.name == 'heavy tackle':
            y2 = y + 1

        # Ensure input is correct
        if (team == 'home' and (x < 1 or x > 6)):
            print('Row out of range')
            continue
        elif (team =='away' and (x < 26 or x > 31)):
            print('Row out of range')
            continue
        if (y < 0 or y > 15 or y2 > 15):
            print('Column our of range')
            continue
        if(x % 2 == 0 and y > 14 and y2 > 14):
            print('Column out of range')
            continue
        if not bb.empty_space(gameboard, x,y):
            print('Space is occupied')
            continue

        if (piece.name == 'heavy tackle' and not bb.empty_space(gameboard, x, y2)):
            print('Space is occunpied')
            continue
        else:
            bb.place_piece(piece_index, (x,y), gameboard)
            piece.place_on_board(x,y)
            if piece.name == 'heavy tackle':
                bb.place_piece(piece_index, (x,y2), gameboard)
            break

def choose_piece_to_move(piece_dictionary, team):
    '''
    This function lets a player chose a uninjured piece to move.
    It returns the chosen piece.
    '''
    while True:
        available_pieces = []
        for piece in piece_dictionary[team]:
            if (not piece.injured):
                available_pieces.append(piece)

        print("You can move one of the following pieces.")
        for piece in available_pieces:
            print(piece.name)
        chosen_one = input("Please select one: ")

        for piece in available_pieces:
            if (piece.name == chosen_one):
                piece_index = piece_dictionary[team].index(piece)
                return piece_index
        else:
            print("Invalid input")

'''
def prompt_move_piece(piece, piece_index, rolled_value, score, gameboard, team):

    while True:
        print 'Choose a location for ' + piece.name

        x = int(input('Row: '))
        y = int(input('Column: '))
        y2 = -1

        if piece.name == 'heavy tackle':
            y2 = y + 1

        # Ensure input is correct
        within_roll = gp.check_movement(piece, rolled_value, (x,y))
        if (not within_roll):
            print "You can't move that far"
            continue
        if (y < 0 or y > 15 or y2 > 15):
            print 'Column out of range'
            continue
        if(x % 2 == 0 and y > 14 and y2 > 14):
            print 'Column out of range'
            continue
        if not bb.empty_space(gameboard, x,y):
            print 'Space is occupied'
            continue

        if (piece.name == 'heavy tackle' and not bb.empty_space(gameboard, x, y2)):
            print 'Space is occupied'
            continue
        else:
            # empty old position
            old_position = piece.position
            gameboard[old_position['xpos']][old_position['ypos']] = 'E'
            if piece.name == 'heavy tackle':
                gameboard[old_position['xpos']][old_position['ypos2']] = 'E'

            # check for ball
            if (gameboard[x][y] == 'B'):
                piece.has_ball = True

            # place piece
            bb.place_piece(piece_index, (x,y), gameboard)
            piece.place_on_board(x,y)

            # heavy tackle
            if piece.name == 'heavy tackle':
                if (gameboard[x][y2] == 'B'):
                    piece.has_ball = True
                bb.place_piece(piece_index, (x,y2), gameboard)

            # check if touchdown
            if (gp.touchdown(piece, (x,y), team)):
                score[team] += 1
                return True
            else:
                return False
'''

def prompt_move_piece(piece, piece_index, rolled_value, score, gameboard, team):
    '''
    Prompts the player to choose a location based on
    the rolled value
    '''
    move_list = ['ul', 'ur', 'l', 'r', 'dl', 'dr']
    while rolled_value != 0 and True:
        print('Move ' + piece.name)
        print('up-left (ul)')
        print('up-right (ur)')
        print('left (l)')
        print('right (r)')
        print('down-left (dl)')
        print('down-right (dr)')

        move = input('move: ')

        # Ensure input is correct
        if move not in move_list:
            print('invalid move')
            continue

        
        within_roll = gp.check_movement(piece, rolled_value, (x,y))
        if (not within_roll):
            print("You can't move that far")
            continue
        if (y < 0 or y > 15 or y2 > 15):
            print('Column out of range')
            continue
        if(x % 2 == 0 and y > 14 and y2 > 14):
            print('Column out of range')
            continue
        if not bb.empty_space(gameboard, x,y):
            print('Space is occupied')
            continue

        if (piece.name == 'heavy tackle' and not bb.empty_space(gameboard, x, y2)):
            print('Space is occunpied')
            continue
        else:
            # empty old position
            old_position = piece.position
            gameboard[old_position['xpos']][old_position['ypos']] = 'E'
            if piece.name == 'heavy tackle':
                gameboard[old_position['xpos']][old_position['ypos2']] = 'E'

            # check for ball
            if (gameboard[x][y] == 'B'):
                piece.has_ball = True

            # place piece
            bb.place_piece(piece_index, (x,y), gameboard)
            piece.place_on_board(x,y)

            # heavy tackle
            if piece.name == 'heavy tackle':
                if (gameboard[x][y2] == 'B'):
                    piece.has_ball = True
                bb.place_piece(piece_index, (x,y2), gameboard)

            # check if touchdown
            if (gp.touchdown(piece, (x,y), team)):
                score[team] += 1
                return True
            else:
                return False
