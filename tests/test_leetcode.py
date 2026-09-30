from src.leetcode import find_smallest_positive, count_repeats
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
    return True

def test__count_repeats_runtime():
    seconds = timeit.timeit(
        'count_repeats(xs,0)',
        'from src.leetcode import count_repeats; xs=list(range(100000,-100000,-1))'
        )
    print('seconds=',seconds)
    return True

def test__count_repeats_runtime2():
    seconds = timeit.timeit(
        'count_repeats(xs,0)',
        'from src.leetcode import count_repeats; xs=[0]*100000'
        )
    print('seconds=',seconds)
    return True
