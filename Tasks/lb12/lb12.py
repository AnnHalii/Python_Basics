from tkinter import *
import time


# 1
def create_triangle(color_1, color_2, color_3, color_4):
    c = Canvas()
    c.pack()
    c.create_polygon((0, 100, 50, 0, 100, 100), fill=color_1)
    c.create_polygon((0, 200, 100, 0, 200, 200), fill=color_2)
    c.create_polygon((100, 200, 200, 100, 300, 200), fill=color_3)
    c.create_polygon((200, 10, 100, 100, 300, 100), fill=color_4)
    mainloop()


create_triangle('green', 'yellow', 'red', 'blue')


# 2
tk = Tk()
c = Canvas(tk, width=500, height=500)
c.pack()
triangle = c.create_polygon(100, 200, 200, 100, 300, 200)
print(c.coords(triangle))
c.move(triangle, 50, 0)
tk.update()
time.sleep(1)
print(c.coords(triangle))
c.move(triangle, 0, 50)
tk.update()
time.sleep(1)
print(c.coords(triangle))
c.move(triangle, -50, 0)
tk.update()
time.sleep(1)
print(c.coords(triangle))
c.move(triangle, 0, -50)
tk.update()
time.sleep(1)
print(c.coords(triangle))

mainloop()

# 3
tk = Tk()
c = Canvas(tk, width=500, height=500)
c.pack()

image_obj = PhotoImage(file="photo.gif")
obj = c.create_image(50,50, anchor=NW, image=image_obj)
c.move(obj, 50, 0)
tk.update()
time.sleep(1)
c.move(obj, 0, 50)
tk.update()
time.sleep(1)
c.move(obj, -50, 0)
tk.update()
time.sleep(1)
c.move(obj, 0, -50)
tk.update()
time.sleep(1)

mainloop()
