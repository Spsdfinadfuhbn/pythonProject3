from dggs import summ


def average(m):
    m.sort()
    n = len(m)
    sumi = 0
    count = 0
    for i in range(n):
        if m[i] % 3 == 0:
            count += m[i]
            sumi += 1
    return count / sumi


m = list((map(int, input().split(","))))
print(average(m))
print(summ(2, 3))
