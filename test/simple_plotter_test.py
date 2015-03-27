from sys import path
path.append('src')
from simple_plotter import get_varnames


def get_names_test1():
    assert(get_varnames('x**2 + y**3') == {'x', 'y'})

def get_names_test2():
    assert(get_varnames('t**2') == {'t'})
