import chess
import chess.svg
from cairosvg import svg2png
from PIL import Image, ImageDraw
import io

def generate_chess_gif(moves, output_file="chess_animation.gif"):
    # Create a new chess board
    board = chess.Board()
    
    # Split moves into individual moves
    moves_list = moves.split()
    
    # List to hold images for each move
    images = []

    # Generate the initial board position
    board_svg = chess.svg.board(board)
    png_image = io.BytesIO()
    svg2png(bytestring=board_svg, write_to=png_image)
    png_image.seek(0)
    images.append(Image.open(png_image))

    # Apply each move and generate images
    for move in moves_list:
        board.push_san(move)
        board_svg = chess.svg.board(board)
        png_image = io.BytesIO()
        svg2png(bytestring=board_svg, write_to=png_image)
        png_image.seek(0)
        images.append(Image.open(png_image))

    # Save images as a GIF
    images[0].save(output_file, save_all=True, append_images=images[1:], loop=0, duration=1000)

# Example usage
moves = "e4 e5 Nf3 Nc6 Bb5"
generate_chess_gif(moves)