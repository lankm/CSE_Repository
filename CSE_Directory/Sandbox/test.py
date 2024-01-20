import sympy
from sympy import symbols, sin, cos, sinh, cosh, tanh
from einsteinpy.symbolic import RicciTensor, RicciScalar, ChristoffelSymbols
from einsteinpy.symbolic.metric import MetricTensor

syms = sympy.symbols("t r theta phi R")
t, r, th, ph, R = syms
a = sympy.Function('a')(t)
metric = MetricTensor([
    [R**2,0,0,0],
    [0,R**2 * cosh(t)**2,0,0],
    [0,0,R**2 * cosh(t)**2 * sin(r)**2,0],
    [0,0,0,R**2 * cosh(t)**2 * sin(r)**2 * sin(th)**2]
], syms[:4])

# cs = ChristoffelSymbols.from_metric(metric)

rt = RicciTensor.from_metric(metric)
for row in rt.tensor():
    print(row)

print()
rs = RicciScalar.from_metric(metric)
print(rs.tensor())
