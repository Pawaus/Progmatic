expressions = []


def calc_str(exp):
    pl_exp = exp.split('+')
    pl_exp2 = []
    tmp = 0
    for i in pl_exp:
        min_exp = i.split('-')
        tmp2 = int(min_exp[0])
        if len(min_exp) > 1:
            for j in range(1, len(min_exp), 1):
                tmp2 -= int(min_exp[j])
        tmp += tmp2
    return tmp


def req_exp(exp, num):
    if num != 0:
        req_exp(exp + str(num) + '+', num - 1)
        req_exp(exp + str(num) + '-', num - 1)
        req_exp(exp + str(num), num - 1)
    else:
        expressions.append(exp + str(num))


if __name__ == '__main__':
    req_exp('', 9)
    for i in expressions:
        if calc_str(i) == 200:
            print(i + ' = 200')
