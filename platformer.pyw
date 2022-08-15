from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pygame as pg

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

vec = pg.math.Vector2

jumps = 0
vx = 0
vy = 0

class Player():
    def __init__(self,x,y):
        self.er = c.create_image(cr[x],cr[y],anchor = 'sw',image = p)
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        def move(self):
            self.acc = vec(0,0.5)
 
            pressed_keys = pygame.key.get_pressed()
                    
            if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
            if pressed_keys[K_RIGHT]:
                self.acc.x = ACC
            
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc

            if self.pos.x > WIDTH:
                self.pos.x = WIDTH
            if self.pos.x < 0:
                self.pos.x = 0
        def jump(self):
            global jumps, vy
            if jumps == 0, or jumps == 1:
                vy += 33
                jumps += 1

def iscolliding():
    for x in tiles:
        p = c.coords(play.er)
        t = c.coords(x)
        if t[1] <= p[1]):
            c.coords(play.er,p[0],t[1])
            return True##############
    return False

def update():
    keys = pg.key.get_pressed()
    for x in tiles


    if keys[K_LEFT]:
        player.acc.x = -ACC
    if keys[K_RIGHT]:
        player.acc.x = ACC      


def touch():
    global vx,vy,jumps

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




