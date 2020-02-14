#! python3
'''
THE CLASSIC GAME TIC TAC TOE

This code implements the classic Tic Tac Toe game.

Author: Givith Abraham
Ver: 1.1
'''

class Tictactoe:

    def __init__(self):
        self.moves = []
        self.board = [' ']*10
        self.displayBoard()


    def displayBoard(self):
        '''
        Method to display the updated board
        '''
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])


    def checkValidMove(self,move):
        '''
        This function checks if the move entered by the user is a valid one or not
        :param move: string/character entered by the user
        :return: INVALID/OCCUPIED/FAIR_MOVE
        '''

        if move not in range(1, 10):
            return 'INVALID'
        elif move in self.moves:
            return 'OCCUPIED'
        else:
            return 'FAIR_MOVE'


    def getTotalMoves(self):
        '''
        This function returns the number total moves played in the game
        :return: total moves | int
        '''
        return len(self.moves)


    def checkWin(self, player):
        '''
        Check if a player has won the game
        :param player: player marker x/o
        :return: true/false
        '''
        player = player.upper()
        if self.board[7] == player and self.board[8] == player  and self.board[9] == player  or \
        self.board[4] == player  and self.board[5] == player  and self.board[6] == player  or \
        self.board[1] == player  and self.board[2] == player  and self.board[3] == player  or \
        self.board[7] == player  and self.board[4] == player  and self.board[1] == player  or \
        self.board[8] == player  and self.board[5] == player  and self.board[2] == player  or \
        self.board[9] == player  and self.board[6] == player  and self.board[3] == player  or \
        self.board[7] == player  and self.board[5] == player  and self.board[3] == player  or \
        self.board[1] == player  and self.board[5] == player  and self.board[9] == player :
            return True
        else:
            return False


    def playerMove(self,move,player):
        '''
        This function makes the user move on board and make calls to checkWin function to see if the game is won/tied
        :param move: user move | character
        :param player: marker for current player| character
        :return: 'WIN'/'TIE'/True
        '''
        # Make the move
        self.moves.append(move)
        self.board[move] = player.upper()

        if len(self.moves) <= 9 and self.checkWin(player):
            # The player have won the game
            self.displayBoard()
            return 'WIN'
        elif len(self.moves) == 9 and not self.checkWin(player):
            # Game is tied
            self.displayBoard()
            return 'TIE'
        self.displayBoard()
        return True



if __name__ == '__main__':

    quit = False

    while not quit:
        # Get the marker for the user
        marker = ''
        while marker == '':
            try:
                marker = input('Enter your marker, X or O: ')
                if marker.lower() != 'x' and marker.lower() != 'o':
                    print('Invalid marker')
                    marker =''
            except:
                pass

        current_player = marker
        total_moves = 0
        game = Tictactoe()


        while total_moves < 9:

            # Check if it is a valid move
            check_move_validity = ''
            while check_move_validity != 'FAIR_MOVE':
                try:
                    # Get the user move
                    move = int(input('Player {}\'s move. Enter your move (1-9): '.format(current_player.upper())))
                    check_move_validity = game.checkValidMove(move)
                    if check_move_validity == 'INVALID':
                        print('Invalid option')
                    elif check_move_validity == 'OCCUPIED':
                        print('Position already occupied')
                except:
                    pass

            # Make the validated move on the board
            game_status = game.playerMove(move, current_player)

            if game_status == 'WIN':
                print('\n \n \n Player {} Wins'.format(current_player.upper()))
                break
            elif game_status == 'TIE':
                print('\n \n \n It is a tie')
                break
            else:
                pass

            #Check the number of moves made so far
            total_moves = game.getTotalMoves()

            # Switch the move to next player
            if current_player == 'x':
                current_player = 'o'
            else:
                current_player = 'x'

        # Check if the user wants to play again
        if input('Do you want to play again  y/n ? ').lower() == 'y':
            quit = False
        else:
            quit = True