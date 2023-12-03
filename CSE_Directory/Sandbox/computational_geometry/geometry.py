# README:
# this should be done in a language with operator and function overloading along with strong typing

from math import sqrt, factorial
from itertools import combinations
import random
import sys
import numpy as np
import sympy as sp

class Vec:
    def __init__(self, vals):
        self.__vec = np.array(vals, dtype=float)
        if self.__vec.ndim != 1:
            raise ValueError('more than one vector given')

    def i():
        return Vec([1,0,0])
    def j():
        return Vec([0,1,0])
    def k():
        return Vec([0,0,1])

    def x(self, newval=None):
        if newval==None:
            return self[0]
        else:
            self[0] = newval
    def y(self, newval=None):
        if newval==None:
            return self[1]
        else:
            self[1] = newval
    def z(self, newval=None):
        if newval==None:
            return self[2]
        else:
            self[2] = newval
    
    def cross(*vecs):
        num_vec, num_dim = np.shape(vecs)
        req_vec = num_dim-1

        # get a possibly random tangent vector
        cross = Vec.qcross(*vecs)
        
        # hypervolume consistancy (||cross|| stays correct for any dimentional space)
        if req_vec == num_vec:
            return cross
        else:
            return Vec.cross(*vecs, cross.U()) # append a new tangent unit vector so hypervolume is unchanged.
    def qcross(*vecs): # quick cross. use if norm doesn't matter
        num_vec, num_dim = np.shape(vecs)
        req_vec = num_dim-1
        if num_vec > req_vec:
            raise ValueError('too many vectors given for this space')
        
        # pad matrix with random vectors for extra degrees of freedom
        filler = [np.random.rand(num_dim) for _ in range(req_vec-num_vec)]
        if len(filler) != 0:
            mat = np.concatenate((vecs,filler))
        else:
            mat = vecs
        
        # actual cross product calculation
        return Vec([-((i%2<<1)-1) * np.linalg.det(np.delete(mat, i, axis=1)) for i in range(len(mat)+1)])
    def dot(self, other):
        return self@other

    def norm(self):
        return abs(self)
    def U(self):
        return Vec(self.__vec/abs(self))

    def __matmul__(self, other):
        result = self.__vec@other
        if result.ndim == 1:
            return Vec(result)
        else:
            return Mat(result)
    def __add__(self, other):
        if len(np.shape(other)) != 1:
            raise ValueError('addition requires a vector-like arument')
        if np.shape(self) != np.shape(other):
            raise ValueError('vectors must be the same size')
        
        return Vec(self.__vec+other)
    def __sub__(self, other):
        if len(np.shape(other)) != 1:
            raise ValueError('subtraction requires a vector-like arument')
        if np.shape(self) != np.shape(other):
            raise ValueError('vectors must be the same size')
        
        return Vec(self.__vec-other)
    def __mul__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('multiplication requires a scalar arument')
        return Vec(self.__vec*val)
    def __truediv__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('division requires a scalar arument')
        return Vec(self.__vec/val)
    def __neg__(self):
        return Vec(-self.__vec)
    def __pos__(self):
        return self

    def __len__(self):
        return len(self.__vec)
    def __abs__(self): # norm
        return np.linalg.norm(self.__vec)
    def __bool__(self):
        return any(val>0 for val in self.__vec)

    def __eq__(self, other):
        return np.array_equal(self.__vec, other)

    def __getitem__(self, i):
        return self.__vec[i]
    def __setitem__(self, i, newval):
        if len(np.shape(newval)) != 0:
            raise ValueError('expected a scalar value')
        self.__vec[i] = newval
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
    def __init__(self, vecs) -> None:
        self.__mat = np.array(vecs, dtype=float)

        if self.__mat.ndim != 2:
            raise ValueError('incorrect number of dimentions')
        
        shape = np.shape(self.__mat)
        if any(shape[i]!=shape[i+1] for i in range(len(shape)-1)):
            raise ValueError('non-square matrix')
    
    def T(self):
        return Mat(self.__mat.T)
    def det(self):
        return abs(self)    
    def sub_matrix(self, i, j):
        return Mat([[self[b][a] for b in range(len(self)) if b!=j] for a in range(len(self)) if a!=i])

    def __matmul__(self, other):
        result = self.__mat@other
        if result.ndim == 1:
            return Vec(result)
        else:
            return Mat(result)
    def __add__(self, other):
        if np.shape(self.__mat) != np.shape(other):
            raise ValueError('addition requires a matrix-like arument of the same shape')
        return Mat(self.__mat+other)
    def __sub__(self, other):
        if np.shape(self.__mat) != np.shape(other):
            raise ValueError('subtraction requires a matrix-like arument of the same shape')
        return Mat(self.__mat-other)
    def __mul__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('multiplication requires a scalar arument')
        return Mat(self.__mat*val)
    def __truediv__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('division requires a scalar arument')
        return Mat(self.__mat/val)
    def __neg__(self):
        return Mat(-self.__mat)
    def __pos__(self):
        return Mat(self.__mat)

    def __len__(self):
        return len(self.__mat)
    def __abs__(self): # determinant
        return np.linalg.det(self.__mat)      
    def __bool__(self): # inversable
        return bool(np.linalg.det(self.__mat) != 0)

    def __eq__(self, other):
        return np.array_equal(self.__mat, other)

    def __getitem__(self, i):
        return self.__mat[i]
    def __setitem__(self, i, newvec):
        if len(np.shape(newvec)) != 1:
            raise ValueError('expected a vector-like value')
        if np.shape(self[0]) != np.shape(newvec):
            raise ValueError('vector must be the same size as the matrix')
        
        self.__mat[i] = newvec
    def __iter__(self):
        return iter(self.__mat)
    def __hash__(self):
        return hash(self.__mat)
    
    def __str__(self):
        vecs = '\n  '.join((f'{Vec(vec)}' for vec in self.__mat))
        return f'< {vecs} >'
    def __repr__(self):
        vecs = '\n  '.join((f'{Vec(val).__repr__()}' for val in self.__mat))
        return f'< {vecs} >'

class Simplex:
    def __init__(self, vecs):
        self.__vecs = np.array(vecs)
        shape = np.shape(self.__vecs)

        if self.__vecs.ndim != 2:
            raise ValueError('incorrect number of dimentions')
        
        if shape[0] > shape[1]+1:
            raise ValueError('too many vectors for for this space')
    
    def sub_simplexes(self, dimdown):
        return [Simplex(a) for a in combinations(self.__vecs, len(self.__vecs)-dimdown)]
    def spheroid(self):
        # IDEA: get perpendicular bisectors and find the intersection point
        base_vec = 0
        mat = list(self.relative_vecs(base_vec))
        num_vec, num_dim = np.shape(mat)

        for _ in range(num_dim-num_vec): # pad with tangent vectors
            mat.append([*Vec.qcross(*mat)])

        for i in range(num_vec):    # tangent bisectors
            mat[i] = [*mat[i],np.dot(mat[i],mat[i])/2]

        for i in range(num_dim-num_vec):    # on same plane of the simplex (0 dist along tangent vectors)
            mat[num_vec+i].append(0)

        rref, shape = sp.Matrix(mat).rref()
        # TODO increment through shape and handle properly. happens if a higher dimention shape is flat. Ex: tetroid has planar like a triangle. or has 0 volume

        center = self.__vecs[base_vec] + [a for a in rref[:, -1]]
        radius = abs(Vec(center) - self.__vecs[base_vec]) # radius from all points is the same
        tangents = [mat[num_vec+i][:-1] for i in range(num_dim-num_vec)] # getting generated tangent vectors

        return Spheroid(center, radius, tangents)

    def dims(self): # dimentional shape. not space
        return len(self)-1
    def relative_vecs(self, i): # get relative vectors from vector i
        return np.array([v-self.__vecs[i] for v in self.__vecs if Vec(v) != self.__vecs[i]])

    def count(self):
        return len(self)
    def length(self):
        dims = self.dims()
        if dims != 1:
            raise ValueError(f'Simplex is {dims} dimentional instead of 1')
        return abs(self)
    def area(self):
        dims = self.dims()
        if dims != 2:
            raise ValueError(f'Simplex is {dims} dimentional instead of 2')
        return abs(self)
    def volume(self):
        dims = self.dims()
        if dims != 3:
            raise ValueError(f'Simplex is {dims} dimentional instead of 3')
        return abs(self)
    def hypervolume(self):
        dims = self.dims()
        if dims < 4:
            raise ValueError(f'Simplex is {dims} dimentional instead of 4 or more.')
        return abs(self)

    def __add__(self, vec):
        if len(np.shape(vec)) != 1:
            raise ValueError('addition requires a vector-like arument')
        if np.shape(self.__vecs[0]) != np.shape(vec):
            raise ValueError('vectors must be the same size')
        
        return Simplex([a+vec for a in self.__vecs])
    def __sub__(self, vec):
        if len(np.shape(vec)) != 1:
            raise ValueError('subtraction requires a vector-like arument')
        if np.shape(self.__vecs[0]) != np.shape(vec):
            raise ValueError('vectors must be the same size')
        return Simplex([a-vec for a in self.__vecs])
    def __mul__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('multiplication requires a scalar arument')
        return Simplex([a*val for a in self.__vecs])
    def __truediv__(self, val):
        if len(np.shape(val)) != 0:
            raise ValueError('division requires a scalar arument')
        
        return Simplex([a/val for a in self.__vecs])
    def __neg__(self):
        return Simplex(-self.__vecs)
    def __pos__(self):
        return Simplex(self.__vecs)

    def __len__(self): # # of points
        return len(self.__vecs)
    def __abs__(self): # n-dim hypervolume 
        # spcial case to follow the pattern of hypervolumes. akin to returning a count instead of length or volume
        if self.dims() == 0:
            return 1
        
        # getting relative vectors so position doesn't effect the outcome
        mat = self.relative_vecs(0)
        num_vec, num_dim = np.shape(mat)

        # if simplex that is the same dim of its space, pad with zeros. Ex: triangle is 2d, tetrahedron is 3d
        if num_vec == num_dim:
            zeros = np.zeros((num_vec,1))
            mat = np.concatenate((mat, zeros), axis=1)
        
        return abs(Vec.cross(*mat)) / factorial(len(mat))

    def __eq__(self, other):
        return np.array_equal(self.__vecs, other)

    def __getitem__(self, i):
        return self.__vecs[i]
    def __setitem__(self, i, newvec):
        if len(np.shape(newvec)) != 1:
            raise ValueError('expected a vector-like value')
        if np.shape(self[i]) != np.shape(newvec):
            raise ValueError('vectors must be the same size')
        
        self.__vecs[i] = newvec
    def __iter__(self):
        return iter(self.__vecs)
    def __hash__(self):
        return hash(self.__vecs)

    def __str__(self):
        shapes = ['point','line','triangle','tetrahedron']
        volumes = ['count','length','area','volume','hypervolume']

        dims = self.dims()
        if dims in range(len(shapes)):
            shape = shapes[dims]
            volume = volumes[dims]
        else:
            shape = f'{dims}-simplex'
            volume = volumes[4]

        return f'{shape} with {volume} {abs(self)}'
    def __repr__(self):
        vecs = '\n  '.join((f'{Vec(val).__repr__()}' for val in self.__vecs))
        return f'[ {vecs} ]'

class Spheroid: # TODO
    def __init__(self, centroid, r, tangents=[]):
        self.__centroid = np.array(centroid)
        self.__r = r
        self.__tangents = np.array(tangents) # for a spheroid with lower dims than its space. Ex: circle in 3d space

    def dims(self):
        return len(self.__centroid) - len(self.__tangents)

    def __str__(self):
        shapes = ['point','line','circle','sphere']

        dims = self.dims()
        if dims in range(len(shapes)):
            shape = shapes[dims]
        else:
            shape = f'{dims}-spheroid'

        return f'{shape} with radius {self.__r}'
    def __repr__(self):
        return f'{Vec(self.__centroid).__repr__()} with radius {self.__r}'

class Pointcloud: # TODO
    def __init__(self, vecs):
        self.__vecs = np.array(vecs)
        if self.__vecs.ndim != 2:
            raise ValueError('incorrect number of dimentions')
        
    def convex_hull(self): # TODO
        # return a polytope
        pass

    def __add__(self, other):
        if len(np.shape(other)) != 2:
            raise ValueError('addition requires a matrix-like value')
        return Pointcloud(list(self.__vecs) + list(other))
    def __sub__(self, other):
        if len(np.shape(other)) != 2:
            raise ValueError('subtraction requires a matrix-like value')
        return Pointcloud([a for a in self.__vecs if Vec(a) not in [Vec(b) for b in other]])

    def __eq__(self, other):
        return all([all(a==b) for a, b in zip(self.__vecs, other)])

    def __getitem__(self, i):
        return self.__vecs[i]
    def __setitem__(self, i, newvec):
        self.__vecs[i] = newvec
    def __iter__(self):
        return iter(self.__vecs)
    def __hash__(self):
        return hash(self.__vecs)

    def __str__(self):
        vecs = '\n  '.join((f'{Vec(val)}' for val in self.__vecs))
        return f'[ {vecs} ]'
    def __repr__(self):
        vecs = '\n  '.join((f'{Vec(val).__repr__()}' for val in self.__vecs))
        return f'[ {vecs} ]'

class Polytope: # TODO
    def __init__(self, simplexes):
        # dictionary from a simplex to its neighbors
        # confirm the polytope doesn't have a hole
        pass
        

def test():
    v1 = Vec([5,-30,0])
    v2 = Vec([4,5,0])
    v3 = Vec([-4,7,0])
    v4 = Vec([2,-5,0])
    s = Simplex([v1,v2,v3,v4])
    print(s.spheroid().__repr__())
    print(s.spheroid())



if __name__ == '__main__':
    test()