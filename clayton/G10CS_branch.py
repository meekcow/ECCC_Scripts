from Tkinter import *
import random
import time

colours = ['#23AAFC','#E5223F']
colour = colours[0]

def getColour():
    try:
        return colour
    except Exception as e:
        colour = colours[0]
        return colour
    
def key(event):
    if str(event.char) == 'h':
        root.overrideredirect(True)
    elif str(event.char) == 'c':
        C.delete('all')
    elif str(event.char) == 'r':
        C.itemconfig('all', outline = colours[1])
        colour = colours[1]
        C.pack(fill='both')
    elif str(event.char) == 'b':
        C.itemconfig('all', outline = colours[0])
        colour = colours[0]
        C.pack(fill='both')
    elif str(event.char) == 's':
        t = C.find_withtag('Square')
        for obj in t:
            C.itemconfig(obj, outline = '#3EFF1F')
    else:
        root.overrideredirect(False)

root = Tk()
root.title = "Game"
root.state('zoomed')
root.wm_attributes("-topmost", 1)

C = Canvas(root,bg='black', width=1920, height=1080)
C.bind("<Key>",key)
C.pack(fill='both')
C.focus_set()


class Rekt:
    def __init__(self, C):
        self.C = C
        C.focus_set()


    def draw(self):
        x = []
        x.append(random.randint(0,1920))
        x.append(random.randint(0,1080))
        x.append(x[0]+random.randint(0,100))
        x.append(x[1]+random.randint(0,100))
        colour = getColour()
        if (x[2] - x[0]) == (x[3]-x[1]):
            print 'Square!'
            C.create_rectangle(x[0],x[1],x[2],x[3],tag='Square', outline=colour)
        else:
            C.create_rectangle(x[0],x[1],x[2],x[3], outline=colour)
        self.C.after(100, self.draw)




theOne = Rekt(C)
theOne.draw()  #Changed per Bryan Oakley's comment.
root.mainloop()
