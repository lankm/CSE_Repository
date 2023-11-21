import numpy as np

class Point:
  def __init__(self, *args: float):
    self.vector = np.array(args, dtype=float)

  def dim(self, i: int) -> float:
    return self.vector[i]
  def x(self) -> float:
    return self.dim(0)
  def y(self) -> float:
    return self.dim(1)
  def z(self) -> float:
    return self.dim(2)
  
  def dims(self) -> int:
    return len(self.vector)

  def dist(self, other):
    return np.linalg.norm(self- other)
  
  def __sub__(self, other) -> Point:
    return self.vector - other
  def __eq__(self, other) -> bool:
    return np.all(self - other)

class Line:
  def __init__(self, p1: Point, p2: Point):
    if p1.dims() != p2.dims():
      raise TypeError('Points have non-equal number of dimentions.')
    self.p1 = p1
    self.p2 = p2

  def dist(self):
    return self.p1.dist(self.p2)
  
  def dims(self):
    return self.p1.dims()

class Graph:
  # list of points and lines. holds point data but line index
  # list of lines and points. holds line data but point index
  def __init__(self):
    self.p_type = None
    self.p_to_l = []
    self.l_to_p = []
  
  def add_point(self, point: Point):
    pass
  def add_line(self, line: Line):
    pass

  def delete_point(self):
    pass
  def delete_line(self):
    pass

  def get_points(self, line: Line):
    pass
  def get_lines(self, point: Point):
    pass