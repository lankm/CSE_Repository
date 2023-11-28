# README:
# The purpose of this file is to provide a linear algebra interface that is implemented with only the python standard library.
# With this interface, users should have a simple and easy framework that can be used in other projects.
# This library is intended to be optimized relative to other python code. As always, lower-level languages would run faster but that is not the purpose of this library.
# This code is intended to be a useful but proof-of-concept library for my other projects. A C++ implementation would probably be the next step.
# Clean code practices take precidence over raw performance

import sys
from itertools import *

def array(iterable):
    return list(tuple(iterable))
def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
def prod(iterable):
    prod = 1
    for val in iterable:
        prod *= val
    return prod
def depth(data):
    if not iterable(data):  # if value
        return 0
    if not data:            # if empty list
        return 1
    return 1 + max(depth(item) for item in data)
def shape(data):
    if not iterable(data):
        return ()
    return (len(data),) + shape(data[0]) if data else (0,)
def flatten(data):
    result = []
    for item in data:
        if iterable(item):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
    
class Mat:
    def __init__(self, mat):
        # TODO validate data. 2d, rectangular, floats
        self.__mat = mat
    
    def shape(self):
        if type(self) != Mat:
            raise TypeError('Expected a Mat type')
        
        return len(self.__mat), len(self.__mat[0])
    
    # TODO clean this up... a lot
    def __getitem__(self, args):
        if not type(args) == tuple:
            args = (args, slice(None))
        if len(args) > 2:
            raise TypeError(f'Mat.__getitem__() takes up to 2 positional arguments but {len(args)} were given')

        num_cols, num_rows = self.shape()
        cols, rows = args
        cols = list(range(0,num_cols))[cols]
        if type(cols) == int:
            cols = [cols]
        rows = list(range(0,num_rows))[rows]
        if type(rows) == int:
            rows = [rows]

        return [[self.__mat[i][j] for j in rows] for i in cols]
    def __setitem__(self, args, new):
        if not type(args) == tuple:
            args = (args, slice(None))
        if len(args) > 2:
            raise TypeError(f'Mat.__getitem__() takes up to 2 positional arguments but {len(args)} were given')

        slices = 2
        num_cols, num_rows = self.shape()
        cols, rows = args
        cols = list(range(0,num_cols))[cols]
        if type(cols) == int:
            cols = [cols]
            slices -= 1
        rows = list(range(0,num_rows))[rows]
        if type(rows) == int:
            rows = [rows]
            slices -= 1

        match slices:
            case 0:
                for j in rows:
                    for i in cols:
                        self.__mat[i][j] = new
            case 1:
                for j in rows:
                    for val, i in zip(new, cols):
                        self.__mat[i][j] = val
            case 2:
                for row, j in zip(new, rows):
                    for val, i in zip(row, cols):
                        self.__mat[i][j] = val
class Vec:
    pass


def test():
    l = [[0,1,2],
         [3,4,5],
         [6,7,8]]
    m = Mat(l)
    m[0,:] = [3,3,3]
    print(m[:,:])
if __name__ == '__main__':
    test()
