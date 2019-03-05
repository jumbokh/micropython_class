### Start of file: random.py ###
import os

def getrandbits(k):
    numbytes = (k + 7) // 8
    x = int.from_bytes(os.urandom(numbytes), 'big')
    return x >> (numbytes * 8 - k)

def bit_length(n):
    res = n
    count = 1
    while res>1:
        res = res>>1
        count = count+1
    return count

def randbelow(n):
    k = bit_length(n)
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r

def randrange(start, stop=None, step=1):
    istart = int(start)
    if istart != start:
        raise ValueError("non-integer arg 1 for randrange()")
    if stop is None:
        if istart > 0:
            return randbelow(istart)
        raise ValueError("empty range for randrange()")

    # stop argument supplied.
    istop = int(stop)
    if istop != stop:
        raise ValueError("non-integer stop for randrange()")
    width = istop - istart
    if step == 1 and width > 0:
        return istart + randbelow(width)
    if step == 1:
        raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))

    # Non-unit step argument supplied.
    istep = int(step)
    if istep != step:
        raise ValueError("non-integer step for randrange()")
    if istep > 0:
        n = (width + istep - 1) // istep
    elif istep < 0:
        n = (width + istep + 1) // istep
    else:
        raise ValueError("zero step for randrange()")

    if n <= 0:
        raise ValueError("empty range for randrange()")

    return istart + istep*randbelow(n)

def randint(a, b):
    return randrange(a, b+1)
### End of file random.py ###
