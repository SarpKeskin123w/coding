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



def serpinski_helper(cx,cy,a,h):
    x0 = cx
    y0 = cy - int(2*h/3)

    x1 = cx - int(a)
    y1 = cy + int(h/3)

    x2 = cx + int(a)
    y2 = cy + int(h/3)
        
    canvas.create_polygon(x0,y0,x1,y1,x2,y2,fill="blue")

def serpinski(depth,cx=dx,cy=dy,a=a):

    h  = round(math.sqrt(3)*(a / 2))

    if depth == 0:
        serpinski_helper(cx,cy,a/2,h)

    else:
        serpinski(depth-1, cx      , cy -h/3 ,a/2) # shift Up
        serpinski(depth-1, cx - a/4, cy +h/6 ,a/2) # shift right down
        serpinski(depth-1, cx + a/4, cy +h/6 ,a/2) # shift left  down

serpinski(3)


