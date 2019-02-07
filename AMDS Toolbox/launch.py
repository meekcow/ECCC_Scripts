## Combining a Tkinter GUI with tools.py
## Creating a toolbox applications :)
## Michael Zhang - michaelhzhang@hotmail.com
## last updated: 10/09/2018

import Tkinter as tk
import tools

#Random font constant
LARGE_FONT = ("Arial", 24)

#Main application window
class Application(tk.Tk):

    #initialization (keyword args)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #applications icon and title
        self.iconbitmap(self, default='img/bijou.ico')
        self.title("AMDS Toolbox")

        #application size and configurations
        self.geometry('800x600')
        
        #container to hold all the screens of the application
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create dictionary of screens
        self.frames = {}

        #list of class objects that are screens
        self.screens = []
        for name in classNames:
            self.screens.append(globals()[name])

        #population dictionary will all possible screens in the application
        for screen in self.screens:
            frame = screen(container, self)
            self.frames[screen] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #set the MainMenu screen as the landing page
        self.show_frame(MainMenu)

    #function to draw the given screen as the top layer
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()

#random function for printing given parameter
def printline(quickPrint=""):
    print(quickPrint)

#MainMenu starting screen
class MainMenu(tk.Frame):
    
    #initialization of this Frame class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Welcome to the toolbox! Select any tool",
                         font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Print text",
                            command=lambda: printline("Lorem Ipsum"))
        button.pack()

        #navigation button to other Frames
        navButton1 = tk.Button(self, text="Page One",
                               #lamba allows command function to have parameters
                                command=lambda: controller.show_frame(ScreenOne))
        navButton1.pack()

        navButton2 = tk.Button(self, text="Page Two",
                                command=lambda: controller.show_frame(Tools))
        navButton2.pack()

        navTools = 0

        for tool in tools.listOfTools:
            tk.Button(self, text=tool,
                      command=lambda: controller.show_frame(ScreenOne)).pack()
            

#Toolbox screen
class Tools(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

#ScreenOne screen
class ScreenOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        navButton1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        navButton1.pack()

        navButton2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(ScreenTwo))
        navButton2.pack()


class ScreenTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        navButton1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        navButton1.pack()

        navButton2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(ScreenOne))
        navButton2.pack()

#current namespace of the script above (classes, variables, functions)
namespace = dir()
#list comprehension finds first instance of string containing '__'
classNames = namespace[namespace.index("MainMenu"):
                       [i for i, n in enumerate(namespace) if '__' in n][0]]


app = Application()
app.mainloop()
