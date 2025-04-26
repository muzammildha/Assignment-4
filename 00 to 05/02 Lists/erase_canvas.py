import tkinter as tk


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 900
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    eraser_coords = canvas.coords(eraser)
    overlapping_objects = canvas.find_overlapping(*eraser_coords)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def on_mouse_move(event, canvas, eraser):
    canvas.moveto(eraser, event.x, event.y)
    erase_objects(canvas, eraser)

def canvas_eraser():
    root = tk.Tk()
    root.title("Eraser Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
   
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill='blue', outline='black')

    def start_eraser(event):
        eraser = canvas.create_rectangle(
            event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE,
            fill='pink'
        )
        canvas.bind('<Motion>', lambda e: on_mouse_move(e, canvas, eraser))

    canvas.bind('<Button-1>', start_eraser)

    root.mainloop()

canvas_eraser() 
