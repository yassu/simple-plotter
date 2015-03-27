from sys import path
path.append('src')
from simple_plotter import Plotter

def get_varname_test1():
    plotter = Plotter('x**2 + y**2')
    assert(plotter._varnames == {'x', 'y'})

def get_varname_test2():
    plotter = Plotter('sin(x**2)')
    assert(plotter._varnames == {'x'})

def replace_to_np_test():
    plotter = Plotter('sin(x**2) + cos(y**2)')
    assert(plotter._func == 'np.sin(x**2) + np.cos(y**2)')
