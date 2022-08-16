from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import pygame as pg
from pynput import keyboard
from pynput.keyboard import Key
import sys
import time
pg.init()


HEIGHT = 560
WIDTH = 1120
ACC = 0.5
FRIC = -0.12

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


pressed_keys = set()

vec = pg.math.Vector2

jumps = 0
vx = 0
vy = 0


def close():
    global carryon
    
    
    
    carryon = False

def on_press(key):
    global pressed_keys
    #print(pressed_keys)
    pressed_keys.add(key)

def on_release(key):
    global pressed_keys
    #print(pressed_keys)
    #try:
    pressed_keys.remove(key)
    #except Error as err:
        #print(err)

class Player():
    def __init__(self,x,y):
        
        
        self.pos = vec((cr[x], cr[y]-1))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

        self.er = c.create_image(self.pos.x,self.pos.y,anchor = 'sw',image = p)
    def move(self):
        self.acc = vec(0100.5)

        #print('hello')        
        if Key.left in pressed_keys:
            self.acc.x = -ACC
        if Key.right in pressed_keys:
            self.acc.x = ACC
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = WIDTH-1
        if self.pos.x < 0:
            self.pos.x = 1

        c.coords(self.er,self.pos.x,self.pos.y)
    def iscolliding(self):
##        for x in tiles:
##            p = c.coords(play.er)
##            t = c.coords(x)
##            if t[1] <= p[1]:
##                #c.coords(play.er,p[0],t[1])
##                return c.coords(x)
##        return False
        p = c.coords(self.er)
        cd = c.find_overlapping(p[0], p[1], p[0]+40, p[1]+40)
        print(cd)
        for x in cd:
            t = c.coords(x)
            print('t[1]',t[1],'\np[1]',p[1])
            c.delete(x)
            if x == self.er:
                pass
            else:
                if t[1] <= p[1]:
                    #c.coords(play.er,p[0],t[1])
                    return c.coords(x)
    def update(self):
        hits = self.iscolliding()
        if hits:
            self.pos.y = hits[1]+39
            self.vel.y = 0
    def jump(self):
        self.vel.y = -15



##def update():
##    keys = pg.key.get_pressed()
##    for x in tiles:
##
##
##    if keys[K_LEFT]:
##        player.acc.x = -ACC
##    if keys[K_RIGHT]:
##        player.acc.x = ACC      


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
#bg = c.create_image(3,3,anchor = 'nw',image = screen)

#player = c.create_image(cr[0],cr[8],anchor = 'sw',image = p)

c.grid(column = 0,row = 2,padx = 5,pady = 5)

read('data/1.lvl')
#tiles.append(c.create_image(cr[28],cr[13],anchor = 'nw',image = g

play = Player(0,8)

print(play.er)


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

#w.protocol("WM_DELETE_WINDOW", close)
carryon = True
while carryon:
    w.update()
    play.move()
    play.update()
    time.sleep(1/60)
listener.stop()
w.quit()
print('hello')
sys.exit()
w.mainloop()




