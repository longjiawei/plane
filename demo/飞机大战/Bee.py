import random
import tkinter


class Bee():
    def __init__(self,canvas):
        self.canvas = canvas
        global x, y
        x = random.randint(50,550)
        y = -50
        bee_img = tkinter.PhotoImage(file="D:\python\demo\飞机大战\图片\\10.gif")
        self.canvas.create_image(x, y, anchor=tkinter.CENTER, image=bee_img, tags='xg')

    def bee_move(self):
        self.canvas.move('xg',0,5)
        self.canvas.after(50,self.bee_move())
class Screen():
    def __init__(self,canvas):
        self.canvas = canvas
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, width=600, height=800)
        self.canvas.pack()
        bg_img = tkinter.PhotoImage(file="D:\python\demo\飞机大战\图片\\2.gif")
        self.canvas.create_image(300, 400, anchor=tkinter.CENTER, image=bg_img, tags='bg')


        self.root.mainloop()
if __name__ == '__main__':
    screen = Screen(canvas= 1)
