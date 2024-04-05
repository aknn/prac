import chess
import chess.svg
import pygame
import numpy as np
import cairosvg
import io

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    board = chess.Board()

    while not board.is_game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Simple AI move (random for now, replace with model prediction)
        move = np.random.choice([m.uci() for m in board.legal_moves])
        board.push_uci(move)

        # Render the board
        screen.fill(pygame.Color("white"))
        svg = chess.svg.board(board=board).encode('utf-8')  # Generate SVG from the chess board
        png = cairosvg.svg2png(bytestring=svg)  # Convert SVG to PNG using cairosvg
        image = pygame.image.load(io.BytesIO(png))  # Load this PNG into Pygame
        screen.blit(image, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()