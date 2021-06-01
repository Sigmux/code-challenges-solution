a = True
b = False
c = (a or b)and(a and not b)
d =((a and b)and(b and not b))

print(d, c)
