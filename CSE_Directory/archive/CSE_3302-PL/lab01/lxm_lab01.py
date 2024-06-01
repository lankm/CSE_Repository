# Landon Moon
# 1001906270
# python 3.10.9
# Windows 10 / Omega

import os

def dirSize(path):
  total=0

  # loop through all files
  for f in os.listdir(path):
    newPath = path + '/' + f

    # if dir
    if os.path.isdir(newPath):
      total+=dirSize(newPath)
    # if file
    else:
      total+=os.path.getsize(newPath)

  return total

# start in current directory
size = dirSize(".")
print(size)
