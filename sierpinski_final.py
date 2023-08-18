from drawingpanel import *
import math

from drawingpanel import *

panel_width  = 1024
panel_height = 768

panel  = DrawingPanel(panel_width,panel_height)
canvas = panel.canvas
canvas.pack()



def serpinski_helper(x0,y0,x1,y1,x2,y2):    
    canvas.create_polygon(x0,y0,x1,y1,x2,y2,fill="yellow")
    canvas.create_line(x0,y0,x1,y1)    
    canvas.create_line(x1,y1,x2,y2)
    canvas.create_line(x2,y2,x0,y0)

def serpinski(depth,x=panel_width/2,y=50,side_length=512):

    height      = round(math.sqrt(3)*(side_length/2))
    if depth == 0:
        serpinski_helper(x,y,x - round(side_length/2),y + height,x + round(side_length/2),y + height)
    else:
        serpinski(depth-1, x,               y          ,side_length/2) 
        serpinski(depth-1, x-side_length/4, y+height/2 ,side_length/2) 
        serpinski(depth-1, x+side_length/4, y+height/2 ,side_length/2) 

serpinski(1)


