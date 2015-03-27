from sys import path
path.append('src')
from simple_plotter import get_varnames


def get_varnames_test1():
    assert(get_varnames('x**2 + y**3') == {'x', 'y'})

def get_varnames_test2():
    assert(get_varnames('t**2') == {'t'})

def get_varnames_test3():
    assert(get_varnames('sin(x**2)') == {'x'})
