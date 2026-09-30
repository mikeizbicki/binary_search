from src.leetcode import find_smallest_positive, find_largest_negative, count_repeats, find_smallest
import math
import sys
import time
import timeit



def test__find_smallest_positive_1():
    assert find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])==4

def test__find_smallest_positive_2():
    assert find_smallest_positive([0, 1, 2, 3])==1

def test__find_smallest_positive_3():
    assert find_smallest_positive([-3, -2, -1, 0, 1])==4

def test__find_smallest_positive_4():
    assert find_smallest_positive([-3, -2, -1, 0, 0.1, 1])==4

def test__find_smallest_positive_5():
    assert find_smallest_positive([]) is None

def test__find_smallest_positive_6():
    assert find_smallest_positive([-1]) is None

def test__find_smallest_positive_7():
    assert find_smallest_positive([1]) == 0

def test__find_smallest_positive_8():
    assert find_smallest_positive([1, 2]) == 0

def test__find_smallest_positive_9():
    assert find_smallest_positive([-1, 2]) == 1

def test__find_smallest_positive_10():
    assert find_smallest_positive([-2, -1]) is None

def test__find_smallest_positive_11():
    assert find_smallest_positive(list(range(-100000, 100000, 47))) == 2128

def test__find_smallest_positive_12():
    assert find_smallest_positive(list(range(100000, 200000, 47))) == 0

def test__find_smallest_positive_13():
    assert find_smallest_positive(list(range(-200000, -100000, 47))) is None


def test__count_repeats_1():
    assert count_repeats([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1)==10

def test__count_repeats_2():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1)==10

def test__count_repeats_3():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],1)==10

def test__count_repeats_4():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],2)==5

def test__count_repeats_5():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],5)==1

def test__count_repeats_6():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],-1)==1

def test__count_repeats_7():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],-1)==0

def test__count_repeats_8():
    assert count_repeats([5],1)==0

def test__count_repeats_9():
    assert count_repeats([5],5)==1

def test__count_repeats_10():
    assert count_repeats([],5)==0

def test__count_repeats_11():
    assert count_repeats([5]*10000+[4,3,2,2,2,1],2)==3

def test__count_repeats_12():
    assert count_repeats([5]*10000,2)==0


def test__find_largest_negative_1():
    assert find_largest_negative([-3, -2, -1, 0, 1, 2, 3])==2

def test__find_largest_negative_2():
    assert find_largest_negative([1, 2, 3]) is None

def test__find_largest_negative_3():
    assert find_largest_negative([-3, -2, -1])==2

def test__find_largest_negative_4():
    assert find_largest_negative([-3, -2, -1, 0])==2

def test__find_largest_negative_5():
    assert find_largest_negative([-0.5])==0

def test__find_largest_negative_6():
    assert find_largest_negative([]) is None

def test__find_largest_negative_7():
    assert find_largest_negative([-1])==0

def test__find_largest_negative_8():
    assert find_largest_negative([0]) is None

def test__find_largest_negative_9():
    assert find_largest_negative([0, 1, 2]) is None

def test__find_largest_negative_10():
    assert find_largest_negative([0]*10) is None

def test__find_largest_negative_11():
    assert find_largest_negative(list(range(-100000, 100000, 47)))==2127

def test__find_largest_negative_12():
    assert find_largest_negative(list(range(100000, 200000, 47))) is None

def test__find_largest_negative_13():
    assert find_largest_negative(list(range(-200000, -100000, 47)))==2127

def test__find_smallest_1():
    assert find_smallest([4, 3, 2, 1, 2, 3])==3

def test__find_smallest_2():
    assert find_smallest([1, 2, 3])==0

def test__find_smallest_3():
    assert find_smallest([3, 2, 1])==2

def test__find_smallest_4():
    assert find_smallest([5])==0

def test__find_smallest_5():
    assert find_smallest([]) is None

def test__find_smallest_6():
    assert find_smallest([-4, -3, -2, -1])==0

def test__find_smallest_7():
    assert find_smallest([-4, -3, -2, -1, 0, 1])==0

def test__find_smallest_8():
    assert find_smallest(list(range(100000, -100000, -1)))==199999

def test__find_smallest_9():
    xs = list(range(100000, -100000, -1)) + list(range(-99998, 100000))
    assert find_smallest(xs)==199999

def test__find_smallest_10():
    assert find_smallest(list(range(-100000, 100000)))==0



# the following test ensure that the runtimes are logrithmic;
# the timeit library runs the functions 1e6 times in a loop;
# if your function is efficient (logarithmic runtime),
# this will take 5-20 seconds per test case;
# if your function is in-efficient, this will take hours per test case;
# the long running tests will timeout on github actions and the test will fail

def test__find_smallest_positive_runtime():
    seconds = timeit.timeit(
        'find_smallest_positive(xs)',
        'from src.leetcode import find_smallest_positive; xs=list(range(-100000,100000,1))'
        )
    print('seconds=',seconds)

def test__count_repeats_runtime():
    seconds = timeit.timeit(
        'count_repeats(xs,0)',
        'from src.leetcode import count_repeats; xs=list(range(100000,-100000,-1))'
        )
    print('seconds=',seconds)

def test__count_repeats_runtime2():
    seconds = timeit.timeit(
        'count_repeats(xs,0)',
        'from src.leetcode import count_repeats; xs=[0]*100000'
        )
    print('seconds=',seconds)


# the code below is a fancier way of testing for runtime of programs;
# it is more complicated, but much faster to run;
# these tests below are how real projects would test the runtime of their code,
# but I want to force you to use the slow tests above to help you develop
# good habits with using the various pytest features to run only some tests


def _count_calls(fn, *args):
    '''
    Invoke fn(*args) while counting how many times fn is entered.
    Works for recursive functions: each recursive call fires a 'call' event.
    '''
    calls = 0

    def tracer(frame, event, arg):
        nonlocal calls
        if event == 'call' and frame.f_code.co_name == fn.__name__:
            calls += 1
        return tracer

    sys.setprofile(tracer)
    try:
        result = fn(*args)
    finally:
        sys.setprofile(None)
    return result, calls


def test__find_smallest_positive_call_count():
    xs = list(range(-100000, 100000))
    _, calls = _count_calls(find_smallest_positive, xs)
    # A correct binary search makes O(log n) recursive calls.
    assert calls <= 2 * math.ceil(math.log2(len(xs)))


def test__count_repeats_call_count():
    xs = list(range(100000, -100000, -1))
    _, calls = _count_calls(count_repeats, xs, 0)
    # count_repeats performs two binary searches, so allow 2x the bound.
    assert calls <= 4 * math.ceil(math.log2(len(xs)))


def test__find_largest_negative_call_count():
    xs = list(range(-100000, 100000))
    _, calls = _count_calls(find_largest_negative, xs)
    assert calls <= 2 * math.ceil(math.log2(len(xs)))


def test__find_smallest_call_count():
    xs = list(range(100000, -100000, -1)) + list(range(-99998, 100000))
    _, calls = _count_calls(find_smallest, xs)
    assert calls <= 2 * math.ceil(math.log2(len(xs)))


def test__find_smallest_positive_elapsed():
    xs = list(range(-100000, 100000))
    find_smallest_positive(xs)  # warm up
    t0 = time.perf_counter()
    for _ in range(1000):
        find_smallest_positive(xs)
    dt = time.perf_counter() - t0
    # 1000 log-time calls should complete in well under a second;
    # a linear implementation would take many seconds here.
    assert dt < 1.0


def test__count_repeats_elapsed():
    xs = list(range(100000, -100000, -1))
    count_repeats(xs, 0)  # warm up
    t0 = time.perf_counter()
    for _ in range(1000):
        count_repeats(xs, 0)
    dt = time.perf_counter() - t0
    assert dt < 1.0
