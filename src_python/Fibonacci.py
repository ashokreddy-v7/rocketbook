limit = 10
a = 0
b = 1
c = 0

while True:
    if(c > 10):
        exit(0)

    print(b)
    b = a + b
    a = b
    c = c + 1