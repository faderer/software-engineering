import numpy as np


flag = 1

for i in range(42):
    for j in range(2, i*i + i + 41):
        if (i*i + i + 41) % j == 0:
            flag = 0
            break
    if flag:
        print(i,end=" ")
    flag = 1