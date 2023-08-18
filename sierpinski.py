from drawingpanel import *
import math

from drawingpanel import *

panel_width  = 1024
panel_height = 768

panel  = DrawingPanel(panel_width,panel_height)
canvas = panel.canvas
canvas.pack()

dx = panel_width/2
dy = panel_height/2
a  = 512



def serpinski_create(x0,y0,x1,y1,x2,y2):
    canvas.create_polygon(x0,y0,x1,y1,x2,y2,fill="blue")

def serpinski(n,cx=dx,cy=dy,a=a):

    h  = round(math.sqrt(3)*(a / 2))

    if n == 0:

        x0 = cx
        y0 = cy - int(h/3)*2

        x1 = cx - int(a/2)
        y1 = cy + int(h/3)

        x2 = cx + int(a/2)
        y2 = cy + int(h/3)
        
        serpinski_create(x0,y0,x1,y1,x2,y2)

    else:
        serpinski(n-1,cx ,cy-(h/3),a/2)
        serpinski(n-1,cx-a/4,cy+h/6,a/2)
        serpinski(n-1,cx+a/4,cy+h/6,a/2)

serpinski((int(input("enter the n:  "))))



