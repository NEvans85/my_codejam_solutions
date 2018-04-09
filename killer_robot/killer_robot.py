f = open("test_input.txt", 'r')

def damage(string):
    total = 0
    strength = 1
    for ch in string:
        if ch == 'C':
            strength *= 2
        if ch == 'S':
            total += strength
    return total

t = f.readline()
for trial in range(t):
    d, p = input().split(' ')
    d = int(d)
    hacks = 0
    sCount = p.count('S')
    if sCount > d:
        result = "IMPOSSIBLE"
    else:
        while damage(p) > d:
            swapIdx = p.rfind('CS')
            p = p[:swapIdx] + 'SC' + p[swapIdx + 2:]
            hacks += 1
        result = str(hacks)
    print("Case #{}: {}".format(str(trial+1), result))
