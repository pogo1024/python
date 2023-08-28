#!/usr/bin/python3
print("HIT ME")
w = list(input())
#list1 = list(w.strip())
#print(list1)
# z = []
# for i in range(len(list1)):
# c = ord((list1[i]))
# z.append(hex(c))
# 
# print(z)

z = list(map(ord,w))
kk =list(map(hex,z))
print(kk)
