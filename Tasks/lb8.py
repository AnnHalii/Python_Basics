# 1
class Giraffes:
    def __init__(self):
        pass
    def left_foot_forward(self):
        print('left foot forward')
    def right_foot_forward(self):
        print('right foot forward')
    def left_foot_back(self):
        print('left foot back')
    def right_foot_back(self):
        print('right foot back')
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()


reginald = Giraffes()
reginald.dance()

# 2
import turtle

a = turtle.Pen()
b = turtle.Pen()
c = turtle.Pen()
d = turtle.Pen()

a.forward(150)
b.forward(150)
c.forward(150)
d.forward(150)
a.left(90)
b.left(90)
c.right(90)
d.right(90)
a.forward(50)
b.forward(100)
c.forward(50)
d.forward(100)
a.right(90)
b.right(90)
c.left(90)
d.left(90)
a.forward(40)
b.forward(80)
c.forward(40)
d.forward(80)
turtle.mainloop()