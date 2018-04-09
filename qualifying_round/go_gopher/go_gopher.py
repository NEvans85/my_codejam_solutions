import sys

t = int(input())
for test in range(t):
    a = int(input())
    prepared = set()
    outX, outY = 2, 2
    print(str(outX) + ' ' + str(outY))
    sys.stdout.flush()
    go_count = 1
    inX, inY = [int(el) for el in input().split(' ')]
    firstX = inX
    outX, outY = inX + 1, inY + 1
    while inX > 0:
        prepared.add((inX, inY))
        while (outX - 1, outY - 1) in prepared and (outX - 1, outY) in prepared and (outX - 1, outY + 1) in prepared and (outX - firstX + 2) * 3 < a:
            outX += 1
        print(str(outX) + ' ' + str(outY))
        sys.stdout.flush()
        go_count += 1
        inX, inY = [int(el) for el in input().split(' ')]
    if inX == -1:
        if go_count >= 1000:
            sys.stderr.write("max count reached \n")
        else:
            sys.stderr.write("invalid pos error \n")
