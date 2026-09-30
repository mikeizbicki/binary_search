from src.argmin import argmin, find_boundaries, argmin_simple


def test__argmin_1():
    epsilon = 1.0
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_2():
    epsilon = 1e-3
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_3():
    epsilon = 1e-6
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_4():
    epsilon = 1e-9
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_5():
    epsilon = 1e-12
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_6():
    epsilon = 1e-6
    lo = -1e20
    hi = 1e20
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_7():
    epsilon = 1e-6
    lo = -1e20
    hi = 0
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon

def test__argmin_8():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_9():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = -5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon

def test__argmin_10():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = -5000
    f = lambda x: x
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon


def test__find_boundaries_1():
    x_min = 0
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_2():
    x_min = 10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_3():
    x_min = -10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_4():
    x_min = 1e10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__find_boundaries_5():
    x_min = -1e10
    f = lambda x: (x-x_min)**2
    lo,hi = find_boundaries(f)
    assert lo <= x_min <= hi

def test__argmin_simple_1():
    epsilon = 1e-3
    x_min = 0
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_simple_2():
    epsilon = 1e-3
    x_min = 10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_simple_3():
    epsilon = 1e-3
    x_min = -10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_simple_4():
    epsilon = 1e-3
    x_min = -1e10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon

def test__argmin_simple_5():
    epsilon = 1e-3
    x_min = 1e10
    f = lambda x: (x-x_min)**2
    assert abs(argmin_simple(f,epsilon)-x_min) <= epsilon
