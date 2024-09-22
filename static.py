import chess
import chess.svg
from cairosvg import svg2png
from PIL import Image

def generate_chess_image(moves, output_file="chess_board.png"):
    # Create a new chess board
    board = chess.Board()

    # Apply the moves to the board
    for move in moves.split():
        board.push_san(move)

    # Generate the SVG of the board
    board_svg = chess.svg.board(board)

    # Convert SVG to PNG
    svg2png(bytestring=board_svg, write_to=output_file)

    # Open the image and display it (optional)
    image = Image.open(output_file)
    image.show()

# Example usage
moves = "Nf3"
generate_chess_image(moves)

