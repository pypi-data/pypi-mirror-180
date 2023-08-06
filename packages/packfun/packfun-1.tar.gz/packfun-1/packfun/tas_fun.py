import math
from .fn_fun import *

__all__ = ['cir', 'rad', 'fi', 'wi', 'ap', 'bp', 'cp', 'nuc1', 'nuc2']


def cir(d):
    c = round(d * math.pi, 2)
    s = round((math.pi / 4) * math.pow(d, 2), 2)
    return c, s  # for task_1


def rad(ab, bc, ac, bo):
    ld = round(math.sqrt(pow(ab, 2) - pow(bo, 2)), 2)
    r = round(bc / 2 * math.sqrt((2 * ab - bc) / (2 * ac + bc)), 2)
    return ld, r  # for task_2


def fi(x, a, b, i):
    k = math.tan(x + a) - math.log(i, math.fabs(b + 7))
    return k


def wi(c, x, d):
    k = math.pow(c, 5) * math.sqrt(pow(x, 2) + d * math.pow(math.e, 1.3))
    return k  # for task_3a


def ap():
    i = 3
    y = 100 * math.fabs(f5(i) + 50)
    return y


def bp():
    i = 3
    y = 150 * math.fabs(f6(i) + 100)
    return y


def cp():
    i = 3
    y = 200 * math.fabs(f7(i) + 135)
    return y  # for task_3b


def nuc1(k):
    a = f10(k) / k
    return a  # for task_7a


def nuc2(k):
    x = 0.242  # table Moivre-Laplace (0; 1)
    a = pow(-1, k) * ((f10(k) * pow(x, k)) / math.factorial(k))
    return a  # for task_7b
