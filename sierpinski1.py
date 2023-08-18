from drawingpanel import *

width = 1024
height = 768
panel = DrawingPanel(width, height)
canvas = panel.canvas
panel.set_background("white")

def triangle(x, y, size):
    x1 = x - size / 2
    y1 = y + size / 2
    x2 = x + size / 2
    y2 = y + size / 2
    x3 = x
    y3 = y - size / 2

    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")

def draw(n, x, y, size):
    
    if n == 0:
        triangle(x, y, size)
    else:

        draw(n - 1, x, y, size / 2) #ORTA KISIM
        draw(n - 1, x - size / 2, y + size / 2, size / 2)  #SOL ÜST
        draw(n - 1, x + size / 2, y + size / 2, size / 2)  #SAĞ ÜST

def main():
    draw(10, width / 2, height / 4, width / 4)

main(5)
