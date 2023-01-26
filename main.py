a=input()
b=input()
if str(a).isdigit() and str(b).isdigit():
    f=int(a)*(int(b)/100)+int(a)
    print(str(round(f)))
else:
    print("Invalid Input")
