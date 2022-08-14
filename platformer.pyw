from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

w = Tk()
w.state('zoomed')
w.minsize(width=600, height=600)
w.title('Platformer')
w['bg']='#ffffff'
#29 x 14

screen = PhotoImage(file='assets/screen1.png')
g = PhotoImage(file='assets/grass1.png')
d = PhotoImage(file='assets/soil1.png')
p = PhotoImage(file='assets/player1_01.png')
l2 = PhotoImage(file='assets/lava_l131.png')
l1 = PhotoImage(file='assets/lava_r161.png')


class Player():
    def __init__(self,x,y):
        self.er = c.create_image(cr[x],cr[y],anchor = 'sw',image = p)


def read(file):
    with open(file,'r', encoding="utf-8") as f:
        r = f.read()
        s = r.splitlines()
        l = []
        for x in s:
            l.append(x.replace('  ',' ').split(' '))

        for y in range(14):
            for x in range(29):
                if l[y][x] == 'g':
                    tiles.append(c.create_image(cr[x],cr[y],anchor = 'nw',image = g))
                if l[y][x] == 'd':
                    tiles.append(c.create_image(cr[x],cr[y],anchor = 'nw',image = d))
                if l[y][x] == 'l1':
                    h = c.create_image(cr[x],cr[y],anchor = 'nw',image = l1)
                    #tiles.append(h)
                    bads.append(h)
                if l[y][x] == 'l2':
                    h = c.create_image(cr[x],cr[y],anchor = 'nw',image = l2)
                    #tiles.append(h)
                    bads.append(h)



#cr=[4, 46, 88, 130, 172, 214, 256, 298, 340, 382, 424, 466, 508, 550, 592, 634, 676, 718, 760, 802, 844, 886, 928, 970, 1012, 1054, 1096, 1138, 1180]
cr=[3, 43, 83, 123, 163, 203, 243, 283, 323, 363, 403, 443, 483, 523, 563, 603, 643, 683, 723, 763, 803, 843, 883, 923, 963, 1003, 1043, 1083, 1123]

tiles=[]
bads=[]

c = Canvas(w,width = 1160,height = 560,bd = 1,relief = SOLID,bg = 'light sky blue')
bg = c.create_image(3,3,anchor = 'nw',image = screen)

player = c.create_image(cr[0],cr[8],anchor = 'sw',image = p)

c.grid(column = 0,row = 2,padx = 5,pady = 5)

read('data/1.lvl')
#tiles.append(c.create_image(cr[28],cr[13],anchor = 'nw',image = g

play = Player(0,8)

print(play.er)


w.mainloop()




