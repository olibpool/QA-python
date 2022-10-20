a = int(input('input a: '))
b = int(input('input b: '))
c = int(input('input c: '))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
        
else:
    if b > c:
        print(b)
    else:
        print(c)