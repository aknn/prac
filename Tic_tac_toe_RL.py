import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Screen and game settings
BOARD_SIZE = 300
CELL_SIZE = BOARD_SIZE // 3
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
X_COLOR = (200, 0, 0)
O_COLOR = (0, 0, 200)
LINE_WIDTH = 5
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))

# Reinforcement learning settings
alpha = 0.1
gamma = 0.9
epsilon = 0.2
Q = {}


def draw_board(board):
    screen.fill(BG_COLOR)
    # Draw vertical lines
    for x in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, BOARD_SIZE), LINE_WIDTH)
    # Draw horizontal lines
    for y in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, y * CELL_SIZE), (BOARD_SIZE, y * CELL_SIZE), LINE_WIDTH)
    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                draw_x(row, col)
            elif board[row][col] == 'O':
                draw_o(row, col)


def draw_x(row, col):
    origin_x = col * CELL_SIZE
    origin_y = row * CELL_SIZE
    pygame.draw.line(screen, X_COLOR, (origin_x + 20, origin_y + 20),
                     (origin_x + CELL_SIZE - 20, origin_y + CELL_SIZE - 20), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (origin_x + CELL_SIZE - 20, origin_y + 20),
                     (origin_x + 20, origin_y + CELL_SIZE - 20), LINE_WIDTH)


def draw_o(row, col):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, O_COLOR, (center_x, center_y), CELL_SIZE // 2 - 20, LINE_WIDTH)


def check_winner(board, player):
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def choose_random_empty(board):
    return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == ''])


def rl_move(board, player):
    state = tuple(tuple(row) for row in board)
    if np.random.rand() < epsilon:
        action = choose_random_empty(board)
    else:
        possible_actions = [(r, c) for r in range(3) for c in range(3) if board[r][c] == '']
        action = max(possible_actions, key=lambda act: Q.get((state, act), 0))

    # Play the move
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player
    new_state = tuple(tuple(row) for row in new_board)
    reward = 1 if check_winner(new_board, player) else 0

    # Update Q-table
    old_value = Q.get((state, action), 0)
    future_best = max(
        Q.get((new_state, a), 0) for a in [(r, c) for r in range(3) for c in range(3) if new_board[r][c] == ''])
    Q[(state, action)] = old_value + alpha * (reward + gamma * future_best - old_value)

    return new_board


def main():
    board = [['' for _ in range(3)] for _ in range(3)]
    player = 'X'  # 'X' starts the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and player == 'X':  # Human player X
                # Check if the click is within bounds and place 'X' if the cell is empty
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if board[row][col] == '':
                    board[row][col] = 'X'
                    if check_winner(board, 'X'):
                        print('X wins!')
                        running = False
                    player = 'O'  # Switch to the other player

        if player == 'O' and not any('' == cell for row in board for cell in row) is False:
            # AI makes its move
            board = rl_move(board, 'O')
            if check_winner(board, 'O'):
                print('O wins!')
                running = False
            player = 'X'  # Switch back to the human player

        draw_board(board)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()