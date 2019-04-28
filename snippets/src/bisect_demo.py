import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]


def demo(bisect_fn):
    for n in reversed(NEEDLES):
        pos = bisect_fn(HAYSTACK, n)
        offset = pos * '  |'
        print(f'{n:2} @ {pos:2}     {offset}{n:2}')


def run_test():
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ''.join(f'{n:3}' for n in HAYSTACK))
    demo(bisect_fn)


def run_test_insert():
    print(HAYSTACK)
    # insert 22 into HAYSTACK at the right place
    bisect.insort(HAYSTACK, 22)
    print(HAYSTACK)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """For a give score return the grade"""
    # find the right index of score in breakpoints
    # e.g. 33 is below 60 and so the index is 0
    # index 0 is 'F' in grades
    i = bisect.bisect(breakpoints, score)
    g = grades[i]
    print(f"{score} -- {g}")
    return g


def run_test_grades():
    [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]


if __name__ == "__main__":
    run_test_grades()
