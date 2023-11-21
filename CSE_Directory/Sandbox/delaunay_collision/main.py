import matplotlib.pyplot as plt
from graph import Point, Line, Graph

def main():
  p1 = Point(2,2,3)
  p2 = Point(1,1,3)
  l = Line(p1,p2)
  print(l.dist())

if __name__ == '__main__':
  main()