# -*-coding:utf-8-*-

import pprint
import time
from collections import namedtuple
from operator import attrgetter


def test():
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('JavaScript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23)
             )
    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print '\n'
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))


SLOW = 3  # 3s
LIMIT = 5   # 字符数
WARNING = 'too bad, you picked the slow algorithm: ('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    if len(s) > LIMIT:
        print WARNING
        time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    if len(s) < LIMIT:
        print WARNING
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = raw_input('Insert world (type quit to exit)> ')
            if word == 'quit':
                print 'bye'
                return
            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = raw_input('Choose strategy: [1] Use a set, [2] Sort and pair> ')
                try:
                    strategy = strategies[strategy_picked]
                    print 'allUnique({}): {}'.format(word, allUnique(word, strategy))
                except KeyError as err:
                    print 'Incorrect option: {}'.format(strategy_picked)
            print '\n'


if __name__ == '__main__':
    test()
    main()