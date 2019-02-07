## Tkinter base using 2.7

import Tkinter as tk

#Random font constant
LARGE_FONT = ("Arial", 24)

#Main application window
class Application(tk.Tk):

    #initialization (keyword args)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #container to hold all the screens of the application
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #create dictionary of screens
        self.frames = {}

        #population dictionary will all possible screens in the application
        for screen in (MainMenu, ScreenOne, ScreenTwo):
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

        label = tk.Label(self, text="Main Menu", font = LARGE_FONT)
        label.pack(pady=10, padx =10)

        button = tk.Button(self, text="Print text",
                            command=lambda: printline("Lorem Ipsum"))
        button.pack()

        #navigation button to other Frames
        navButton1 = tk.Button(self, text="Page One",
                               #lamba allows command function to have parameters
                                command=lambda: controller.show_frame(ScreenOne))
        navButton1.pack()

        navButton2 = tk.Button(self, text="Page Two",
                                command=lambda: controller.show_frame(ScreenTwo))
        navButton2.pack()

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
        label.pack(pady=10,padx=10)

        navButton1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MainMenu))
        navButton1.pack()

        navButton2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(ScreenOne))
        navButton2.pack()

app = Application()
app.mainloop()
