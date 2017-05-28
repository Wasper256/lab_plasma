import math 


def main():
    r, h = cr_list()
    ai = ai_calc(r, h)
    ci = ci_calc(r, h)
    bi = bi_calc(r, h)
    di = di_calc(r)
    f = TDMA(ai, bi, ci, di)
    print f
    with open("res.txt", 'w') as file:
        for i in f:
            file.write(str(i) + "\n")


def cr_list():
    a = [5]
    i = 5
    h = 0.2
    while i <= 50:
        i += h
        a.append(round(i, 3))
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


def ci_calc(r, h):
    ci = []
    for i in r:
        c = 1 / (h * h)
        ci.append(c)
    return ci


def di_calc(r):
    di = []
    for i in r:
        d = -(math.exp((-math.pow(r[r.index(i)], 2) / 10)))
        di.append(d)
    return di


def TDMA(ai, bi, ci, di):
    a, b, c, di = ai, bi, ci, di
    alpha = []
    alpha.append(0)
    beta = []
    beta.append(-5)
    n = len(di)
    x = [0] * n

    for i in range(n - 1):
        alpha.append(-b[i] / (a[i] * alpha[i] + c[i]))
        beta.append((di[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i]))
    x[n - 1] = (di[n - 1] - a[n - 2] * beta[n - 1]) / (c[n - 1] + a[n - 2] * alpha[n - 1])
    for i in reversed(range(n - 1)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x

if __name__ == '__main__':
    main()
