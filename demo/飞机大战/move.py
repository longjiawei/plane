import random
import tkinter


class Hero():
    def __init__(self):
        global x, y
        x = random.randint(50, 550)
        y = -50
        self.root = tkinter.Tk()
        self.root.title('飞机大战')
        self.canvas = tkinter.Canvas(self.root,width='600',height='800')
        self.canvas.pack()
        hero_img = tkinter.PhotoImage(file = "D:\python\demo\飞机大战\图片\\1.gif")
        bg_img = tkinter.PhotoImage(file ="D:\python\demo\飞机大战\图片\\2.gif" )
        bee_img = tkinter.PhotoImage(file="D:\python\demo\飞机大战\图片\\10.gif")

        self.canvas.create_image(300,400,anchor = tkinter.CENTER,image = bg_img,tags = 'bg')
        self.canvas.create_image(300,750,anchor= tkinter.CENTER,image= hero_img,tags= 'hero')
        for i in range(1,10):
            self.canvas.create_image(x, y, anchor=tkinter.CENTER, image=bee_img, tags='gw')
        self.bee_move()


        self.root.mainloop()
    def bee_move(self):
        self.canvas.move('gw',0,+2)
        self.canvas.after(50,self.bee_move)

    def move(self):
        self.canvas.move('hero',0,-2)
        self.canvas.move('bg',0,5)
        self.canvas.after(50,self.move)


    def move_left(self):
        self.canvas.move('hero',-2,0)
    def move_right(self):
        self.canvas.move('hero',+2,0)
    def move_up(self):
        self.canvas.move('hero',0,-2)
    def move_dowm(self):
        self.canvas.move('hero',0,+2)

if __name__ == '__main__':
    Hero()