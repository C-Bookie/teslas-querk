
import numpy as np
import pygame, sys
from pygame.locals import *

import time
import math
import random


def foo(n, b):
    r=[]
    while (n>0):
        r.append(n%b)
        n/=b
        n-=n%1
    return [0] if len(r)==0 else r
#    return [int(d) for d in str(n)]

def bar(n):
    r=0
    for a in n:
        r+=a
    return r

def loop(base, lj, l):
    red=[]
    n=0
    while n<lj:
        r = []
        i = 0
        while i<l:
            a=foo(n*i, base)
            while len(a)>1:
                a=foo(bar(a), base)
            r.append(a[0])
            i+=1
        print(str(n)+": "+str(r))
        red.append(r)
        n+=1

    return red

if __name__ == '__main__':
    lj=250
    l = 250
    size = 1

    base = 10


    pygame.init()
    global surface
    surface = pygame.display.set_mode((l*size, lj*size), 0, 32)

    cycle = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        base = cycle+1
#        base = 10
        red = loop(base, lj, l)

        y = 0
        while y < lj:
            x = 0
            while x < l:
                moo = red[y][x]
                p = math.floor((255. / base) * moo)
                pygame.draw.rect(surface, (p, p, p), (size * x, size * y, size, size))
                x += 1
            y += 1

        pygame.display.update()
#        time.sleep(4)
#        break
        cycle+=1


