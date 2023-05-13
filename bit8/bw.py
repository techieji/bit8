# Black and white (with higher resolution)

import itertools as it
import operator as op

def screen_to_units(scr):
    xsize = 2
    ysize = 4
    # Pray forgive this monstrosity, O God, for the pains of pragmatricity needle me far more so than
    # that lofty ideal of mathematical purity, held for too long in its ivory tower. Shine your light
    # on one who is undeserving, this man to whom hope has fled like the wisdom of his ancestors long
    # passed. ILLUMINATE this code for it is wretched, and REDEEM it so that its worthiness to an eye
    # held by the masters of yore may be filled with many a tear, and not in sorrow.
                                                                                 #   signed, the unawakened coder
    return [[[[scr[ys + y][xs + x] for x in range(xsize)] for y in range(ysize)] for xs in range(0, len(scr[0]), xsize)] for ys in range(0, len(scr), ysize)]

def unit_to_braille(unit):
    l = list(map(op.itemgetter(1), sorted(zip([1,2,3,7,4,5,6,8], it.chain.from_iterable(zip(*unit))))))
    v = sum(map(op.mul, l, map(pow, it.repeat(2), it.count())))
    return chr(v + 10240)

print(unit_to_braille([[1,0],[1,1],[0,0],[0,0]]))

def render(scr, move_cursor=True):
    pass

def as_str(scr):
    pass
