import numpy as np

#方法一
flag = 1

for i in range(2, 200):
    for j in range(2, i):
        if i % j == 0:
            flag = 0
            break
    if flag:
        print(i)
    flag = 1
#方法二 Eratosthenes筛法


a_l = [1]*200

for i in range(2, 200):
    if i % 2 == 0 and i != 2:
        a_l[i] = 0
    if i % 3 == 0 and i != 3:
        a_l[i] = 0
    if i % 5 == 0 and i != 5:
        a_l[i] = 0
    if i % 7 == 0 and i != 7:
        a_l[i] = 0
    if i % 11 == 0 and i != 11:
        a_l[i] = 0
    if i % 13 == 0 and i != 13:
        a_l[i] = 0
for i in range(2,200):
    if a_l[i] == 1:
        print(i)