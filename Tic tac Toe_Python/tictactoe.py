#! python3


class Tictactoe:

    def __init__(self,marker):
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

        if move  in self.moves:
            # This position is already played
            return False

        self.moves.append(move)
        self.board[move] = player.upper()

        if len(self.moves) <= 9 and self.checkWin(player):
            print('\n \n \n Player {} Wins'.format(player.upper()))
            self.displayBoard()
            return 9
        elif len(self.moves) == 9 and not self.checkWin(player):
            print('\n \n \n It is a tie')
            self.displayBoard()
            return 9
        self.displayBoard()
        return True



if __name__ == '__main__':


    marker = input('Enter your marker, X or O: ')
    while marker.lower() != 'x' and marker.lower() != 'o':
        print('Invalid marker')
        marker = input('Enter your marker, X or O: ')

    current_player = marker
    moves_left = 9
    game = Tictactoe(marker)


    while moves_left > 0:
        move = int(input('Player {}\'s move. Enter your move (1-9): '.format(current_player.upper())))

        # Check if it is a valid move
        while move not in range(1, 10):
            print('Invalid option')
            move = int(input('Player {}\'s move. Enter your move (1-9): '.format(current_player.upper())))
        retVal = game.playerMove(move,current_player)

        while not retVal :
            print('Position already occupied')
            move = int(input('Player {}\'s move. Enter your move (1-9): '.format(current_player.upper())))
            while move not in range(1, 10):
                print('Invalid option')
                move = int(input('Player {}\'s move. Enter your move (1-9): '.format(current_player.upper())))
            retVal = game.playerMove(move, current_player)

        if retVal == 9:
            break

        if current_player == 'x':
            current_player = 'o'
        else:
            current_player = 'x'
