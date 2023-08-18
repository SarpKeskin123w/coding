import sys
import time
from tkinter import Tk, Canvas

def render_text(canvas, text, font, x, y):
    canvas.create_text(x, y, text=text, font=font)

def animate_text(panel, filename, width, height, font_size, wpm):
    with open(filename, 'r') as file:
        text = file.read()
    
    words = text.split()
    word_delay = 60 / wpm * 1000  

    root = Tk()
    root.title("speed reader")
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()

    center_x = width // 2
    center_y = height // 2

    font = ("Courier", font_size)

    for word in words:
        canvas.delete("all") 
        render_text(canvas, word, font, center_x, center_y)
        panel.update()
        time.sleep(word_delay / 1000)  

    with open('gutenberg.txt', 'w') as f:
        f.writelines('\n'.join(words))

    root.mainloop()

def main():

    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    font_size = int(sys.argv[4])
    wpm = int(sys.argv[5])

    panel = Tk()
    animate_text(panel, filename, width, height, font_size, wpm)
    panel.mainloop()

if __name__ == "__main__":
    main()
