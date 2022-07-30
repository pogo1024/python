#!/usr/bin/python3
print("HIT ME")
w = str(input())
list1 = list(w.strip())
print(list1)
z = []
for i in range(len(list1)):
    c = ord((list1[i]))
    z.append(hex(c))

print(z)
