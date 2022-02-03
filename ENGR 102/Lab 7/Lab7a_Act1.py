# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab7a_Act1a
# Date: 12 October 2021


board = [['.' for _ in range(8)] for _ in range(8)] # Make board
for i in range(3):
    for j in range(8):
        if (i+j)%2:
            board[i][j] = '○' # Put light pieces on correct squares
            
for i in range(5, 8):
	for j in range(8):
		if (i+j)%2:
			board[i][j] = '●' # Put light pieces on correct squares
board.append([' '] + list(map(lambda x: f'{x}', range(8)))) # Label numbers at the bottom (cols)
for i in range(8):
    board[i] = [f'{i}']+board[i] # Label numbers on the side (rows)

#################Functions#################
def display_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def is_valid(start, dest):

    # Make sure we're on a black square
    if (dest[0] + dest[1]) % 2:

        # Make sure we're in boundsd
        if not (0 <= start[0] <= 7 and
            0 <= start[1] <= 7 and
            0 <= dest[0] <= 7 and
            0 <= dest[1] <= 7):
            return 0
        
        # Make sure we're moving in the proper direction
        if board[start[0]][start[1]+1] == '●':
            if dest[0] - start[0] != -1:
                return 0
        elif board[start[0]][start[1]+1] == '○':
            if dest[0] - start[0] != 1:
                return 0
        # Make sure we're actually moving a piece
        if board[start[0]][start[1]+1] == '.':
            print('Piece not found')
            return 0
        elif board[start[0]][start[1]+1] == board[dest[0]][dest[1]+1]:
            return 0

        # Make sure we're only moving to adjacent squares
        if abs(start[1] - dest[1]) != 1:
            return 0
        return 1
        
    # if it is a white square it returns false
    else:
        return 0      

def update_board(start, dest):
    curr_piece = board[start[0]][start[1]+1]
    # Sets the end value
    board[dest[0]][dest[1]+1] = curr_piece
    # Sets the start value to empty
    board[start[0]][start[1]+1] = '.'

#########################################
    
while True:
    display_board()
    
    piece_to_move = input('Enter the row and column of the piece you want to move separated by a space (Ex: 2 5): ')
    if piece_to_move == 'stop':
        exit()

    move = input('Enter the destination row and column separated by a space (Ex: 2 5): ')
    if move == 'stop':
        exit()
    
    piece_to_move = list(map(int, piece_to_move.split()))
    move = list(map(int, move.split()))
    
    # Validate input
    if is_valid(piece_to_move, move):
        update_board(piece_to_move, move)
    else:
        print("Invalid move, try again")