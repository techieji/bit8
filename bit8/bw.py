# Black and white (with higher resolution)

import itertools as it

def chunk(_i, n):
    i = iter(_i)
    while (l := list(it.islice(i, n))):
        yield l

def transpose(l):
    return list(zip(*l))

def ipad(scr):
    for x in scr:
        if len(x) % 2 != 0:
            x.append(0)
    if len(scr) % 4 != 0:
        for _ in range(len(scr) % 4):
            scr.append([0] * len(scr[0]))

def screen_to_units(scr):
    xsize = 2
    ysize = 4
    return [[ [[scr[ys + y][xs + x] for x in range(xsize)] for y in range(ysize)] for xs in range(0, len(scr[0]), xsize)] for ys in range(0, len(scr), ysize) ]

def render(scr, move_cursor=True):
    pass

def as_str(scr):
    pass
