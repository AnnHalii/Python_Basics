from tkinter import *
import time
        
class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        
        self.canvas = Canvas(self.tk, width=500, height=500, bd=0, highlightthickness=0)
        self.canvas.pack()
        
        self.tk.update()
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.bg = PhotoImage(file="white.gif")
        self.bg2 = PhotoImage(file="black.gif")
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 8):
            for y in range(0, 8):
                if x % 2 == 0:
                    if y % 2 == 0:
                        self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')
                    else:
                        self.canvas.create_image(x * w, y * h, image=self.bg2, anchor='nw')
                else:
                    if y % 2 == 0:
                        self.canvas.create_image(x * w, y * h, image=self.bg2, anchor='nw')
                    else:
                        self.canvas.create_image(x * w, y * h, image=self.bg, anchor='nw')



        
        self.sprites = []
        self.running = True
                
    def add(self, sprite):
        self.sprites.append(sprite)
        
    def mainloop(self):
        while 1:
            for sprite in self.sprites:
                sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
g.mainloop()

