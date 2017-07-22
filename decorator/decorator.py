# -*-coding:utf-8-*-
'''
Created on 2017年7月19日

@author: houguangdong
'''
import functools

known = {0:0, 1:1}

def fibonacci1(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci1(n-1) + fibonacci1(n-2)
    known[n] = res
    return res


known_sum = {0: 0}

def nsum(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n-1)
    known_sum[n] = res
    return res


def memoize(fn):
    known = dict()
    # 创建修饰器
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def nsum1(n):
    '''返回前n个数字的和'''
    assert (n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum1(n-1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    from timeit import Timer
#     t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
#     print t.timeit()
    t = Timer('fibonacci1(100)', 'from __main__ import fibonacci1')
    print t.timeit()
    print nsum(5)
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci', 'func': fibonacci}, {'exec': 'nsum1(200)', 'import': 'nsum1', 'func': nsum1}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print 'name: {}, doc: {}, executing: {}, time: {}'.format(m['func'].__name__, m['func'].__doc__, m['exec'], t.timeit())