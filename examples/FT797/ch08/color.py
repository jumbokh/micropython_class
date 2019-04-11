# -*- coding: utf-8 -*-

"""
   程式說明請參閱8-19頁
"""

def hsv2rgb(h, s, v):
    if s == 0.0:
        return v, v, v

    r, g, b = v, v, v

    i = int(h/60.0)
    f = h/60.0 - i

    if i == 0:
        g *= 1.0 - s * (1.0 - f)
        b *= 1.0 - s
    elif i == 1:
        r *= 1.0 - s * f
        b *= 1.0 - s
    elif i == 2:
        r *= 1.0 - s
        b *= 1.0 - s * (1.0 - f)
    elif i == 3:
        r *= 1.0 - s
        g *= 1.0 - s * f
    elif i == 4:
        r *= 1.0 - s * (1.0 - f)
        g *= 1.0 - s
    elif i == 5:
        g *= 1.0 - s
        b *= 1.0 - s * f

    return (int(r * 1023.0), int(g * 1023.0), int(b * 1023.0))