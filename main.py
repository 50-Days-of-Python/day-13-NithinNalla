a=input()
if('.'in a):
    k=round(float(a))
else:
    k=int(a)
b=input()
if('.'in a):
    p=round(float(b))
else:
    p=int(b)
f=k*(p/100)+k
print(f)
