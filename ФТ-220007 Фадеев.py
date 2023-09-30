a, b = float(input("Write number: ")), float(input("Write number: "))
print("Sum:", a+b)
print("Diff:", a-b)
print("Mult:", a*b)
print("Arithm mean:", (a+b)/2)
if a < 0:
    a = -a
if b < 0:
    b = -b
if a > b:
    print("Abs diff:", a-b)
else:
    print("Abs diff:", b-a)
if b != 0:
    print('Div:', round(a/b, 2))
else:
    print('Error: dividing by zero')
