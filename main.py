#Write your code here.
a=input()
if('.'in a):
    k=round(float(a))
else:
    k=int(a)
p=int(input())
f=int(k*(p/100)+k)
print(f)
