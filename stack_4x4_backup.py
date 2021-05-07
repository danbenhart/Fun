import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 8
COLUMN_COUNT = 8
#
# test_game_state = [[0, 0, 0, 0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 2, 0, 0, 0],
#                    [0, 0, 0, 0, 3, 0, 0, 0],
#                    [8, 7, 6, 5, 4, 3, 2, 1],
#                    [0, 0, 0, 0, 5, 0, 0, 0],
#                    [0, 0, 0, 0, 6, 0, 0, 0],
#                    [0, 0, 0, 0, 7, 0, 0, 0],
#                    [0, 0, 0, 0, 8, 0, 0, 0]]


def is_valid_location(row, column, game_state):
    all_left = game_state[row][:column]
    all_right = game_state[row][column+1:]
    all_up = []
    for line in game_state[:row]:
        all_up.append(line[column])
    all_down = []
    for line in game_state[row+1:]:
        all_down.append(line[column])
    if 0 not in all_left or 0 not in all_right or 0 not in all_up or 0 not in all_down:
        return True
    else:
        return False


# print(is_valid_location(2, 5, test_game_state))


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and \
                    board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and \
                    board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and \
                    board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and \
                    board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                               int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            if is_valid_location(r, c, board):
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS-30)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                 int((r+1) * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2),
                                                    int((r+1) * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = create_board()
# print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

my_font = pygame.font.SysFont("monospace", 75)

while not game_over:

    for event in pygame.event.get():
        # print_board(board)
        draw_board(board)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos_x, pos_y), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos_x, pos_y), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            col = int(math.floor(pos_x / SQUARESIZE))
            row = int(math.floor(pos_y / SQUARESIZE)) - 1

            if is_valid_location(row, col, board):
                if turn == 0:
                    # print(row, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = my_font.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True

                # # Ask for Player 2 Input
                else:
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label = my_font.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)
