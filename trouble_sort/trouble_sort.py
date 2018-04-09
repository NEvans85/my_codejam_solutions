def trouble_sort(vals):
    svals = vals[:]
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(svals) - 2):
            if svals[idx] > svals[idx + 2]:
                svals[idx], svals[idx + 2] = svals[idx + 2], svals[idx]
                sorted = False
    return svals

cases = int(input())
for case in range(cases):
    n = int(input())
    v = [int(el) for el in input().split(' ')]
    sv = trouble_sort(v)
    result = 'OK'
    for idx, el in enumerate(sv[:-1]):
        if el > sv[idx + 1]:
            result = str(idx)
            break
    print("Case #{}: {}".format(str(case + 1), result))
