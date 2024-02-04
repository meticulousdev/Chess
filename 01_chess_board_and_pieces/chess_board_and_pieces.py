import tkinter as tk
from PIL import ImageTk, Image

UNIT = 100
HEIGHT = 8
WIDTH = 8

PhotoImage = ImageTk.PhotoImage


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(f"{WIDTH * UNIT}x{HEIGHT * UNIT}")
    window.title("Chess Board and Pieces")

    file_path: str = "./01_chess_board_and_pieces/img/"
    king_bk = PhotoImage(Image.open(file_path + "king_bk.png").resize((50, 50)))
    king_wh = PhotoImage(Image.open(file_path + "king_wh.png").resize((50, 50)))
    queen_bk = PhotoImage(Image.open(file_path + "queen_bk.png").resize((50, 50)))
    queen_wh = PhotoImage(Image.open(file_path + "queen_wh.png").resize((50, 50)))
    bishop_bk = PhotoImage(Image.open(file_path + "bishop_bk.png").resize((50, 50)))
    bishop_wh = PhotoImage(Image.open(file_path + "bishop_wh.png").resize((50, 50)))
    knight_bk = PhotoImage(Image.open(file_path + "knight_bk.png").resize((50, 50)))
    knight_wh = PhotoImage(Image.open(file_path + "knight_wh.png").resize((50, 50)))
    rook_bk = PhotoImage(Image.open(file_path + "rook_bk.png").resize((50, 50)))
    rook_wh = PhotoImage(Image.open(file_path + "rook_wh.png").resize((50, 50)))

    canvas = tk.Canvas(window, bg='white',
                       height=HEIGHT * UNIT,
                       width=WIDTH * UNIT)
    
    # Grid
    for col in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = col, 0, col, HEIGHT * UNIT
        canvas.create_line(x0, y0, x1, y1, fill='black')
    for row in range(0, HEIGHT * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = 0, row, HEIGHT * UNIT, row
        canvas.create_line(x0, y0, x1, y1, fill='black')

    # Rectangle
    # TODO MERGE
    for col in range(0, 5):
        for row in range(0, 5):
            x1 = 100 + 200 * (col - 1)
            y1 = 0 + 200 * (row - 1)
            x2 = 200 + 200 * (col - 1)
            y2 = 100 + 200 * (row - 1)
            canvas.create_rectangle(x1, y1, x2, y2, fill='light gray')

    for col in range(0, 5):
        for row in range(0, 5):
            x1 = 200 * (col - 1)
            y1 = 100 + 200 * (row - 1)
            x2 = 100 + 200 * (col - 1)
            y2 = 200 + 200 * (row - 1)
            canvas.create_rectangle(x1, y1, x2, y2, fill='light gray')

    canvas.create_image(350, 50, image=king_bk)    
    canvas.create_image(450, 750, image=king_wh)

    canvas.create_image(450, 50, image=queen_bk)    
    canvas.create_image(350, 750, image=queen_wh)

    canvas.create_image(550, 50, image=bishop_bk)
    canvas.create_image(250, 50, image=bishop_bk)
    canvas.create_image(550, 750, image=bishop_wh)    
    canvas.create_image(250, 750, image=bishop_wh)

    canvas.create_image(650, 50, image=knight_bk)
    canvas.create_image(150, 50, image=knight_bk)
    canvas.create_image(650, 750, image=knight_wh)    
    canvas.create_image(150, 750, image=knight_wh)

    canvas.create_image(750, 50, image=rook_bk)
    canvas.create_image(50, 50, image=rook_bk)
    canvas.create_image(750, 750, image=rook_wh)    
    canvas.create_image(50, 750, image=rook_wh)

    canvas.pack()

    window.mainloop()