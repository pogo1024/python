print("HIT ME")
w = str(input())
list1 = list(w.strip())
print("KEY")
h = int(input())
#print(list1)
z = []
for i in range(len(list1)):
    c = ord((list1[i]))
    d = c + h
    e = chr(d)
    z.append(e)

print(''.join(z))
