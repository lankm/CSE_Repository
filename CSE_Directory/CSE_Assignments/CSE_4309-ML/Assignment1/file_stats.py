import sys
import numpy as np

f = open(sys.argv[1])

buffArr = []
for (i, line) in enumerate(f.readlines()):
    numbers = line.split()
    buffArr.append(list(map(float,numbers)))

columns = np.array(buffArr).transpose()

for (i, nums) in enumerate(columns):
    print("Column %d: mean = %.4f, std = %.4f" % (i+1, np.mean(nums), np.std(nums, ddof=1)))