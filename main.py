import math 


def main():
    r, h = cr_list()
    print r, h
    ai = ai_calc(r, h)
    print ai
    ci = 1 / (h * h)
    print ci
    bi = bi_calc(r, h)
    print bi
    di = di_calc(r)
    print di


def cr_list():
    a = [5]
    i = 5
    h = 0.2
    while i <= 50:
        i += h
        a.append(i)
    return a, h


def ai_calc(r, h):
    ai = []
    for i in r:
        # rt = int(r[i])
        # print i
        a = (1 / (h * h)) + (1 / ((r[r.index(i)]) * h)) * r.index(i)
        # print a
        ai.append(a)
    return ai


def bi_calc(r, h):
    bi = []
    for i in r:
        # rt = int(r[i])
        # print i
        b = (2 / (h * h)) + (1 / ((r[r.index(i)]) * h)) * r.index(i)
        # print r.index(i)
        bi.append(b)
    return bi


def di_calc(r):
    di = []
    for i in r:
        d = -(math.exp((-math.pow(r[r.index(i)], 2) / 10)))
        di.append(d)
    return di

if __name__ == '__main__':
    main()
