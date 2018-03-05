import numpy as np
import warnings
from threading import Timer
from copy import deepcopy

warnings.simplefilter(action='ignore', category=FutureWarning)


class Reversi:

    def __init__(self, Matrix=False):

        rows, cols = 8, 8
        if Matrix == False:
            self.Matrix = np.full((rows, cols), '+', dtype=str)
            self.Matrix[3, 4] = self.Matrix[4, 3] = 'O'
            self.Matrix[3][3] = self.Matrix[4][4] = 'X'

        else:
            self.Matrix = Matrix

        # Prints the initial instance of the game
        self.printGame()
        gameType = input("Enter 1 for User vs. Comp, 2 for User vs. User")

        self.timeout = input("How long does each player have to make a move? (in seconds) \n")
        # t = Timer(self.timeout, print, ['Sorry you took too long to make a move, press enter to continue'])
        # t.start()
        # prompt = "You have %d seconds to choose the correct answer...\n" % timeout
        # answer = input(prompt)
        # t.cancel()
        if int(self.timeout) <= 20:
            self.maxtree = 2
        else:
            self.matree = 4

        self.flagMove = 0
        ###which game type
        if int(gameType[-1]) == 1:
            self.vsCompGame()
        else:
            self.vsUserGame()

    ##function to check for validity of a move

    # player is 0 for black 1 for white, swapFlag is 0 to check if move is valid and 1 to swap tiles
    def validMove(self, row, col, player, swapFlag, game_field=False):

        if game_field == False:
            Matrix = self.Matrix
        else:
            Matrix = deepcopy(game_field)
        self.flagMove = 0

        ##returnValue should only be 1 when there is a valid move being made
        returnValue = 0

        # Valid moves for:

        # UP
        # player is black (0) or white (1)
        if self.validMoveU(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # DOWN
        if self.validMoveD(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # LEFT
        if self.validMoveL(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # RIGHT
        if self.validMoveR(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # DIAGONAL RIGHT UP
        if self.validMoveDRU(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # DIAGONAL RIGHT DOWN
        if self.validMoveDRD(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # DIAGONAL LEFT UP
        if self.validMoveDLU(row, col, player, swapFlag, Matrix):
            returnValue = 1

        # DIAGONAL LEFT DOWN
        if self.validMoveDLD(row, col, player, swapFlag, Matrix):
            returnValue = 1

        if Matrix[row][col] == 'X' or Matrix[row][col] == 'O':
            returnValue = 0

        # Make current tile an X or O if the return value is 1
        if returnValue == 1 and player == 0 and swapFlag == 1:
            Matrix[row][col] = 'X'
        elif returnValue == 1 and player == 1 and swapFlag == 1:
            Matrix[row][col] = 'O'
        return returnValue, Matrix

    ######### Valid Moves ###################

    def validMoveU(self, row, col, player, swapFlag, Matrix=False):

        if Matrix == False:
            Matrix = self.Matrix

        # check to make sure inputs are in bounds
        if col - 1 < 0:
            return 0

            # checks which player is making the move
        if player == 0:
            # print("UP Move" + str(row) + str(col))
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row][col - 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row][col - 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveU(row, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row][col - 1] = 'X'

                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row][col - 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row][col - 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveU(row, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row][col - 1] = 'O'

                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveD(self, row, col, player, swapFlag, Matrix=False):

        if Matrix == False:
            Matrix = self.Matrix
        self.flagMove
        # check to make sure inputs are in bounds
        if col + 1 > 7:
            return 0
        # checks which player is making the move
        if player == 0:
            # print("Down Move" + str(row) + str(col))
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row][col + 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row][col + 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveD(row, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row][col + 1] = 'X'

                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row][col + 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row][col + 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveD(row, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row][col + 1] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveR(self, row, col, player, swapFlag, Matrix=False):
        self.flagMove
        if Matrix == False:
            Matrix = self.Matrix
        # check to make sure inputs are in bounds
        if row + 1 > 7:
            return 0

            # checks which player is making the move
        if player == 0:
            # print("Right Move" + str(row) + str(col))

            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col] == 'O':

                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveR(row + 1, col, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveR(row + 1, col, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveL(self, row, col, player, swapFlag, Matrix=False):
        self.flagMove
        if Matrix == False:
            Matrix = self.Matrix
        # check to make sure inputs are in bounds
        if row - 1 < 0:
            return 0

        # checks which player is making the move
        if player == 0:
            # print("Left Move" + str(row) + str(col))
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveL(row - 1, col, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveL(row - 1, col, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveDRU(self, row, col, player, swapFlag, Matrix=False):
        if Matrix == False:
            Matrix = self.Matrix
        self.flagMove

        # check to make sure inputs are in bounds
        if row + 1 > 7 or col - 1 < 0:
            return 0

            # checks which player is making the move
        if player == 0:

            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col - 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col - 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDRU(row + 1, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col - 1] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col - 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col - 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDRU(row + 1, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col - 1] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            # Return 0 if no moves are found
        return 0

    def validMoveDRD(self, row, col, player, swapFlag, Matrix=False):
        if Matrix == False:
            Matrix = self.Matrix

        self.flagMove

        # check to make sure inputs are in bounds
        if col + 1 > 7 or row + 1 > 7:
            return 0

            # checks which player is making the move
        if player == 0:

            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col + 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col + 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDRD(row + 1, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col + 1] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row + 1][col + 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row + 1][col + 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDRD(row + 1, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row + 1][col + 1] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveDLD(self, row, col, player, swapFlag, Matrix=False):
        self.flagMove
        if Matrix == False:
            Matrix = self.Matrix

        # check to make sure inputs are in bounds
        if col + 1 > 7 or row - 1 < 0:
            return 0

            # checks which player is making the move
        if player == 0:

            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col + 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col + 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDLD(row - 1, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col + 1] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col + 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col + 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDLD(row - 1, col + 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col + 1] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    def validMoveDLU(self, row, col, player, swapFlag, Matrix=False):
        if Matrix == False:
            Matrix = self.Matrix
        self.flagMove

        # check to make sure inputs are in bounds
        if col - 1 < 0 or row - 1 < 0:
            return 0

            # checks which player is making the move
        if player == 0:

            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col - 1] == 'X' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col - 1] == 'O':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDLU(row - 1, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col - 1] = 'X'
                return pointer

            self.flagMove = 0
            pointer = 0
            return 0
        elif player == 1:
            # Checks to see if a tile has been flipped and there is a tile of the same
            # value after
            if Matrix[row - 1][col - 1] == 'O' and self.flagMove == 1:
                self.flagMove = 0
                return 1

            # Checks to see if there is a tile of opposing value next to the cursor
            if Matrix[row - 1][col - 1] == 'X':
                # mark that a move is possible
                self.flagMove = 1

                # Recursion in order to continue checking if there are opposing tiles
                pointer = self.validMoveDLU(row - 1, col - 1, player, swapFlag, Matrix)
                if pointer == 1 and swapFlag == 1:
                    Matrix[row - 1][col - 1] = 'O'
                return pointer

            # flag
            self.flagMove = 0
            pointer = 0
            return 0
            # Return 0 if no moves are found
        return 0

    ############## end Movement Validity Functions ##############

    ##############---- GameType Functions ---###################

    # end of game = 1,   Check: 1 Board is full or 2 There is only one color or 3 No more Valid moves
    def endOfGame(self, Matrix=False):
        if Matrix == False:
            Matrix = self.Matrix

        # variables to check number of crosses, X's, O's left on board
        numCrosses = self.gameScore()[2]
        numX = self.gameScore()[0]
        numO = self.gameScore()[1]

        xList = self.listofMoves(0)
        oList = self.listofMoves(1)

        # if no crosses left or there are no x's or o's then game is over
        if numCrosses == 0 or numX == 0 or numO == 0:
            return 1
        # if there are no more valid moves for each player then game is over

        elif len(xList) == 0 and len(oList) == 0:
            print("End of Game xList")
            print(xList)
            print(len(xList))
            return 1
        else:
            return 0

    # returns a list of all possible moves for a certain player, list is in [(x1,y1), (x2,y2), ...] format
    def listofMoves(self, player, game_field=False):
        if game_field == False:
            Matrix = self.Matrix
        else:
            Matrix = game_field

        moves = []
        del moves[:]
        for x in range(0, 8):
            for y in range(0, 8):
                if player == 0:
                    if self.validMove(x, y, player, 0, Matrix)[0] == 1:
                        moves.append((x + 1, y + 1))
                elif player == 1:
                    if self.validMove(x, y, player, 0, Matrix)[0] == 1:
                        moves.append((x + 1, y + 1))
        return moves

        # returns score of game, positive numbers mean Black (X) is winning, negative numbers mean White (O) is winning

    # user move
    # def userMove(self):
    def gameScore(self, Matrix=False):
        if Matrix == False:
            Matrix = self.Matrix
        numX = 0
        numO = 0
        numCrosses = 0

        for x in range(0, 8):
            for y in range(0, 8):
                if self.Matrix[x][y] == 'X':
                    numX += 1
                if self.Matrix[x][y] == 'O':
                    numO += 1
                if self.Matrix[x][y] == '+':
                    numCrosses += 1
        return numX, numO, numCrosses

    # Game for User vs. Computer
    def vsCompGame(self):
        print("\n \nWho is the first player?")

        playerVar = input("1 for User, 2 for Computer")

        if int(playerVar[-1]) == 1:
            self.user = 0
            self.computer = 1
            self.usercolor = 'X'
            self.computercolor = 'O'
            startvalue = False
        elif int(playerVar[-1]) == 2:
            self.user = 1
            self.computer = 0
            self.usercolor = 'O'
            self.computercolor = 'X'
            startvalue = True

        while not self.endOfGame():

            validFlag = 0
            # ComputerPlayer
            if startvalue == True:
                a = self.alpha_beta_search()
                if len(self.listofMoves(self.computer)) == 0:
                    break
                print('the computer decided to set his tile on {},{}'.format(a[0] + 1, a[1] + 1))

                self.validMove(a[0], a[1], self.computer, 1)

                self.printGame()
                validFlag = 0

            startvalue = True

            # UserPlayer
            while validFlag == 0:
                # Player 2 Movement
                print("Possible moves in (row,col) format")
                listMoves = self.listofMoves(self.user)
                print(listMoves)
                if len(listMoves) == 0:
                    break

                moveTimer = Timer(int(self.timeout), print,
                                  ['\nYou took too long, move will be made for you\n Press Enter to Continue'])
                moveTimer.start()
                player2move = input("Player {} in row,col of your current move".format(self.usercolor))
                moveTimer.cancel()

                if player2move != "":
                    x2 = int(player2move[-3]) - 1
                    y2 = int(player2move[-1]) - 1
                    print("Player move is")
                    print(player2move)
                else:
                    tempMove = self.listofMoves(self.user).pop()
                    x2 = int(tempMove[-2]) - 1
                    y2 = int(tempMove[-1]) - 1
                    print("Move is: ")
                    print(tempMove)

                if self.validMove(x2, y2, self.user, 1)[0] == 1:
                    print("Move is valid")
                    validFlag = 1
                else:
                    print("Not a Valid move, try a different one")

                    # reprint gameboard
            self.printGame()

        scoreX = self.gameScore()[0]
        scoreO = self.gameScore()[1]
        if scoreX == scoreO:
            print("Game is a tie")
        elif scoreX > scoreO:
            print("Player Black Wins with" + str(scoreX) + " Points")
        elif scoreX < scoreO:
            print("Player White Wins with" + str(abs(scoreO)) + " Points")

        return 0

    # Game for User vs. User

    # Game for User vs. User
    def vsUserGame(self):

        while not self.endOfGame():

            validFlag = 0

            while validFlag == 0:

                # Player1 Move, inputted and printed to std out, and inputted to gameboard
                print("Possible X moves in (row,col) format")
                print(self.listofMoves(0))
                if len(self.listofMoves(0)) == 0:
                    break
                moveTimer = Timer(int(self.timeout), print,
                                  ['\nYou took too long, move will be made for you\n Press Enter to Continue'])
                moveTimer.start()
                player1move = input("Player Black(X) input your current move in row,col\n")
                moveTimer.cancel()

                if player1move != "":
                    x1 = int(player1move[-3]) - 1
                    y1 = int(player1move[-1]) - 1
                    print("Player move is")
                    print(player1move)
                else:
                    tempMove = self.listofMoves(0).pop()
                    x1 = int(tempMove[-2]) - 1
                    y1 = int(tempMove[-1]) - 1
                    print("Move is: ")
                    print(tempMove)

                # player1's move should be validated first, and the turn should not pass until
                # player1 makes a valid move
                if self.validMove(x1, y1, 0, 1)[0] == 1:
                    print("move is Valid")
                    validFlag = 1
                else:
                    print("Not a Valid move, try a different one")

            # reprint gameboard, reset flag
            self.printGame()
            validFlag = 0

            while validFlag == 0:
                # Player 2 Movement
                print("Possible O moves in (row,col) format")
                print(self.listofMoves(1))
                if len(self.listofMoves(1)) == 0:
                    break
                moveTimer = Timer(int(self.timeout), print,
                                  ['\nYou took too long, move will be made for you\n Press Enter to Continue'])
                moveTimer.start()
                player2move = input("Player White(O) input row,col of your current move")
                moveTimer.cancel()

                if player2move != "":
                    x2 = int(player2move[-3]) - 1
                    y2 = int(player2move[-1]) - 1
                    print("Player move is")
                    print(player2move)
                else:
                    tempMove = self.listofMoves(1).pop()
                    x2 = int(tempMove[-2]) - 1
                    y2 = int(tempMove[-1]) - 1
                    print("Move is: ")
                    print(tempMove)

                if self.validMove(x2, y2, 1, 1)[0] == 1:
                    print("Move is valid")
                    validFlag = 1
                else:
                    print("Not a Valid move, try a different one")

                    # reprint gameboard
            self.printGame()

        scoreX = self.gameScore()[0]
        scoreO = self.gameScore()[1]
        if scoreX == scoreO:
            print("Game is a tie")
        elif scoreX > scoreO:
            print("Player Black Wins with" + str(scoreX) + " Points")
        elif scoreX < scoreO:
            print("Player White Wins with" + str(abs(scoreO)) + " Points")

    # function to print out game matrix
    def printGame(self):
        print('  1 2 3 4 5 6 7 8')
        for x in range(0, 8):
            print(x + 1, end=' ')
            for y in range(0, 8):
                print(self.Matrix[x][y], end=' ')
            print()

        ############## end GameType Functions ###################

    def alpha_beta_search(self):

        '''
        Builds the decision tree (alpha-beta pruning algorithm)
        return: the optimal move
        type: touple
        '''

        CalcMatrix = deepcopy(self.Matrix)
        v, moves_with_values = self.maxValue(CalcMatrix, -np.inf, +np.inf, 0)
        move = max(moves_with_values, key=moves_with_values.get)
        return move

    def maxValue(self, Matrix, alpha, beta, depth):
        '''
        Builds the alpha-beta pruning tree with a depth of 6

        returns: the actual weight and a dictionary with all moves + weight
        '''

        if self.endOfGame(Matrix):
            weight = self.utility(Matrix)
            return weight, weight

        if depth == self.maxtree:
            weight = self.utility(Matrix)
            return weight, weight
        v = -101  # minimum value
        possible_moves = self.listofMoves(self.computer, Matrix)
        possible_moves[:] = [(x[0] - 1, x[1] - 1) for x in possible_moves]
        moves_with_values = {}
        for x in possible_moves:
            v = max(v, self.minValue(self.validMove(x[0], x[1], self.computer, 1, Matrix)[1], alpha, beta, (depth + 1)))
            moves_with_values[x] = v
            if v >= beta:
                return v, moves_with_values
            alpha = max([alpha, v])
        return v, moves_with_values

    def minValue(self, Matrix, alpha, beta, depth):
        if self.endOfGame(Matrix):
            weight = self.utility(Matrix)
            return weight
        v = 101  # maximum value
        possible_moves = self.listofMoves(self.user, Matrix)
        possible_moves[:] = [(x[0] - 1, x[1] - 1) for x in possible_moves]
        for x in possible_moves:
            v = min(v, self.maxValue(self.validMove(x[0], x[1], self.user, 1, Matrix)[1], alpha, beta, (depth + 1))[0])
            if v <= alpha:
                return v
            beta = min([beta, v])
        return v

    def utility(self, Matrix):
        '''
        calculates the heuristic (originally planed with more than one function)

        Counts the amound of tiles of each player

        returns how many percent of all tiles the computer has

        Can be extented by function for the mobility or the stability
        '''
        MaxPlayer = np.count_nonzero(Matrix == self.computercolor)
        MinPlayer = np.count_nonzero(Matrix == self.usercolor)
        return 100 * (MaxPlayer - MinPlayer) / (MaxPlayer + MinPlayer)



game = Reversi()



####Timer for Moves was found online at: https://stackoverflow.com/questions/15528939/python-3-timed-input