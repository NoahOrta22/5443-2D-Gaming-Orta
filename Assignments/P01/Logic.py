import numpy as np
import random

SIZE = 4

# self.board = np.zeros((SIZE, SIZE))

# self.board[0] = np.array([2, 2, 2, 2])
# self.board[1] = np.array([8, 16, 16, 4])

# self.board = np.array([[4, 4, 2, 4], 
#                 [4, 32, 0, 2],
#                 [2, 0, 2, 0],
#                 [4, 4, 0, 4]])


# print(self.board)

class game_board():
    def __init__(self):
        # game variables initialize
        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0
    
    #
    #   Returns 'True' if the board is full
    #
    def board_full(self):
        if np.any(self.board == 0):
            return False
        else:
            return True

    #
    #   Returns False if the board is full and there are no valid moves
    #
    def has_valid_move(self):
        if self.board_full():
            # check rows to see if similar numbers are next to each other
            for row in range(SIZE):
                for col in range(SIZE-1):
                    if self.board[row][col] == self.board[row][col+1]:
                        return True
            # check columns to see if similar numbers are next to each other
            for col in range(SIZE):
                for row in range(SIZE-1):
                    if self.board[row][col] == self.board[row+1][col]:
                        return True
            # if no similiar numbers are next to eachother return false
            return False
        else:
            return True

    #
    #   Function for adding pieces in random spots after a moves
    #
    def add_piece(self):
        # find the rows & columns of where there's a zero
        row, col = np.where(self.board==0)

        # if there are zeros in the matrix
        if len(row) > 0: 
            index = random.randint(0, len(row)-1)
            
            # 10% chance of placing a 4
            if random.randint(1, 10) == 10:
                self.board[row[index], col[index]] = 2
            else:
                self.board[row[index], col[index]] = 2
        

    # 
    #   Function to slide the blockes 
    #   
    #   Returns: false if the board was unchanged
    #
    def move(self, direction):

        # holds the state of the old board
        old_board = np.copy(self.board)

        changed = False

        #   tiles are going up
        if direction == 'up': 
            for col in range (SIZE):
                # going through elements in a row from right to left
                for row in range (SIZE):

                    # if there are numbers that are not zero below the current
                    if self.board[row, col] == 0 and np.any(self.board[row+1:, col] != 0):
                        # the game state has been changed
                        changed == True         

                        # we're going to shift the elements up until there's a non zero
                        while self.board[row, col] == 0:
                            self.board[row:, col] = np.roll(self.board[row:, col], -1)

                    # if we're not on the first row
                    if row > 0:
                        # elements next to eachother are the same
                        if self.board[row, col] == self.board[row-1, col]:
                            # combine the elements and add to the score
                            self.board[row-1, col] *= 2
                            self.score += self.board[row-1, col]
                            self.board[row, col] = 0

                            # if there are numbers that are not zero to the bottom of current
                            if self.board[row, col] == 0 and np.any(self.board[row+1:, col] != 0):
                                # we're going to shift the elements to the right so there's a non zero
                                while self.board[row, col] == 0:
                                    self.board[row:, col] = np.roll(self.board[row:, col], -1)
                        

        #   tiles are going right
        elif direction == 'right': 
            for row in self.board:
                # going through elements in a row from right to left
                for i in range (SIZE-1, -1, -1):
                    # if there are numbers that are not zero to the left of current
                    if row[i] == 0 and np.any(row[:i] != 0):
                        # the game state has been changed
                        changed == True 

                        # we're going to shift the elements to the right so there's a non zero
                        while row[i] == 0:
                            row[:i+1] = np.roll(row[:i+1], 1)

                    # if we're not on the last column
                    if i < SIZE-1:
                        # elements next to eachother are the same
                        if row[i] == row[i+1]:
                            # combine the elements and add to the score
                            row[i+1] *= 2
                            self.score += row[i+1]
                            row[i] = 0

                            # if there are numbers that are not zero to the left of current
                            if row[i] == 0 and np.any(row[:i] != 0):
                                # we're going to shift the elements to the right so there's a non zero
                                while row[i] == 0:
                                    row[:i+1] = np.roll(row[:i+1], 1)

        #   tiles are doing down
        elif direction == 'down': 
            for col in range (SIZE):
                # going through elements in a column from bottom to top
                for row in range (SIZE-1, -1, -1):

                    # if there are numbers that are not zero above the current
                    if self.board[row, col] == 0 and np.any(self.board[:row, col] != 0):
                        # the game state has been changed
                        changed == True 

                        # we're going to shift the elements up until there's a non zero
                        while self.board[row, col] == 0:
                            self.board[:row+1, col] = np.roll(self.board[:row+1, col], 1)

                    # if we're not on the last row
                    if row < SIZE-1:
                        # elements next to eachother are the same
                        if self.board[row, col] == self.board[row+1, col]:
                            # combine the elements and add to the score
                            self.board[row+1, col] *= 2
                            self.score += self.board[row+1, col]
                            self.board[row, col] = 0

                            # if there are numbers that are not zero above the current
                            if self.board[row, col] == 0 and np.any(self.board[:row, col] != 0):
                                # we're going to shift the elements down until there's a non zero
                                while self.board[row, col] == 0:
                                    self.board[row:, col] = np.roll(self.board[row:, col], 1)

        #   tiles are going left
        elif direction == 'left': 
            for row in self.board:
                # going through elements in a row from right to left
                for i in range (0, SIZE):

                    # if there are numbers that are not zero to the right of current
                    if row[i] == 0 and np.any(row[i+1:] != 0):
                        # the game state has been changed
                        changed == True 

                        # we're going to shift the elements to the right so there's a non zero
                        while row[i] == 0:
                            row[i:] = np.roll(row[i:], -1)

                    # if we're not on the first column
                    if i > 0:
                        # elements next to eachother are the same
                        if row[i] == row[i-1]:
                            # combine the elements and add to the score
                            row[i-1] *= 2
                            self.score += row[i-1]
                            row[i] = 0

                            # if there are numbers that are not zero to the right of current
                            if row[i] == 0 and np.any(row[i+1:] != 0):
                                # we're going to shift the elements to the right so there's a non zero
                                while row[i] == 0:
                                    row[i:] = np.roll(row[i:], -1)

        # if the old and new board are the same then they haven't changed
        if (old_board==self.board).all():
            return False
        else:
            return True
