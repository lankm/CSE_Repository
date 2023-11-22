from math import sqrt
import numpy as np
import sys

class Vec:
    def __init__(self, *args):
        if hasattr(args[0], '__iter__'):
            self.__vec = tuple(val for val in args[0])
        else:
            self.__vec = tuple(val for val in args)

    def i():
        return Vec(1,0,0)
    def j():
        return Vec(0,1,0)
    def k():
        return Vec(0,0,1)

    def x(self, new_val=None):
        if new_val==None:
            return self[0]
        else:
            self[0] = new_val
    def y(self, new_val=None):
        if new_val==None:
            return self[1]
        else:
            self[1] = new_val
    def z(self, new_val=None):
        if new_val==None:
            return self[2]
        else:
            self[2] = new_val
    
    def cross(*vecs):
        pass

    def __matmul__(self, other):
        return sum(a*b for a, b in zip(self[:], other[:]))
    def __add__(self, other):
        vals = (a+b for a, b in zip(self[:], other[:]))
        return Vec(*vals)
    def __sub__(self, other):
        vals = (a-b for a, b in zip(self[:], other[:]))
        return Vec(*vals)
    def __mul__(self, val):
        return Vec(*[a*val for a in self[:]])
    def __truediv__(self, val):
        return Vec(*[a/val for a in self[:]])

    def __len__(self):
        return len(self.__vec)
    def __abs__(self):
        return sqrt(self*self)
    def __bool__(self):
        return any(a>0 for a in self.__vec)

    def __eq__(self, other):
        return all(a==b for a, b in zip(self[:], other[:]))
    def __neg__(self):
        return Vec(-val for val in self.__vec)
    def __pos__(self):
        return self

    def __getitem__(self, dim):
        return self.__vec[dim]
    def __setitem__(self, dim, new_val):
        vals = list([val for val in self.__vec])
        vals[dim] = new_val
        self.__vec = tuple(vals)
    def __iter__(self):
        return iter(self.__vec)
    def __hash__(self):
        return hash(self.__vec)
    
    def __str__(self):
        vals = ' '.join((f'{val:.3f}' for val in self.__vec))
        return f'< {vals} >'
    def __repr__(self):
        vals = ' '.join((f'{val}' for val in self.__vec))
        return f'< {vals} >'

class Mat:
    def __init__(self, *args) -> None:
        arg = list(args[0])
        if hasattr(arg[0], '__iter__'):
            self.__mat = tuple(Vec(a) for a in arg)
        else:
            self.__mat = tuple(Vec(a) for a in args)
    
    def __eq__(self, other):
        return all(a==b for a, b in zip(self[:], other[:]))
    def __neg__(self):
        return Mat(-vec for vec in self.__mat)
    def __pos__(self):
        return self

    def __getitem__(self, vec):
        return self.__mat[vec]
    def __setitem__(self, dim, new_vec):
        vecs = list([vec for vec in self.__mat])
        vecs[dim] = new_vec
        self.__mat = tuple(vecs)
    def __iter__(self):
        return iter(self.__mat)
    def __hash__(self):
        return hash(self.__mat)
    
    def __str__(self):
        vecs = '\n  '.join((f'{vec}' for vec in self.__mat))
        return f'< {vecs} >'
    def __repr__(self):
        vecs = '\n  '.join((f'{val.__repr__}' for val in self.__mat))
        return f'< {vecs} >'

class Simplex:
    pass


def test():
    pass
if __name__ == '__main__':
    test()