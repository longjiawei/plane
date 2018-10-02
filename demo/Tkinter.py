import random
import tkinter


class Ball(object):
    def __init__(self,canvas,scrnwidth, scrnheight ):
        self.canvas = canvas
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.radius = random.randint(20,100)
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)
        self.xpos = random.randint(10,int(scrnwidth-20))
        self.ypos = random.randint(10,int(scrnheight-20))
        c = lambda : random.randint(0,255)
        self.color='#%02x%02x%02x'%(c(),c(),c())
    def draw_ball(self):

        x1 = self.xpos - self.radius
        y1 = self.ypos + self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos - self.radius
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def ball_move(self):

        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity *= -1
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity *= -1
        if self.xpos - self.radius <= 0:
            self.xvelocity *= -1
        if self.ypos -self.radius <= 0:
            self.yvelocity *= -1
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)

class ScreenSever:

    def __init__(self, num_balls):
        self.balls = list()
        self.num_balls = random.randint(5, 20)
        self.root = tkinter.Tk()
        self.root.overrideredirect(1)
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        self.root.bind('<Motion>',self.myquit)
        self.root.bind('<KeyPress>',self.myquit)
        self.canvas = tkinter.Canvas(self.root,width= w ,height = h)
        self.canvas.pack()
        for i in range(num_balls):
            ball = Ball(self.canvas,scrnwidth = w , scrnheight = h)
            ball.draw_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.ball_move()
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self,event):
        self.root.destroy()

if __name__ == '__main__':
    ScreenSever(30)


