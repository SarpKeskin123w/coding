import sys
import time
from drawingpanel import *

def render_text(panel, text, font, x, y):
    panel.canvas_create_text(x, y, text=text, font=font)

def animate_text(panel, filename, width, height, font_size, wpm):
    with open(filename, 'r') as file:
        text = file.read()
    
    words = text.split()
    word_delay = 60 / wpm
    panel = DrawingPanel(width=width, height=height)
    canvas = panel.canvas

    center_x = width // 2
    center_y = height // 2

    font = ("Courier", font_size)

    for word in words:
        canvas.delete("all")
        render_text(panel, word, font, center_x, center_y)
        panel.update()
        time.sleep(word_delay)

    with open('output.txt', 'w') as f:
        f.writelines('\n'.join(words))

def main():
    
    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    font_size = int(sys.argv[4])
    wpm = int(sys.argv[5])

    animate_text(DrawingPanel(), filename, width, height, font_size, wpm)

if __name__ == "__main__":
    main()
