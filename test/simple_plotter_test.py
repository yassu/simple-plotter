from sys import path
path.append('src')
from simple_plotter import Plotter, DEFAULT_MIN_X

def get_funcs_test():
    assert(Plotter.get_funcs('t**2') == ('t**2', ))

def get_funcs_test2():
    assert(Plotter.get_funcs('t**2, t**3') == ('t**2', 't**3'))

def get_funcs_test3():
    assert(Plotter.get_funcs('(t**2, t**3)') == ('t**2', 't**3'))

def get_varname_test1():
    plotter = Plotter('x**2 + y**2')
    assert(plotter._varnames == {'x', 'y'})

def get_varname_test2():
    plotter = Plotter('sin(x**2)')
    assert(plotter._varnames == {'x'})

def replace_to_np_test():
    plotter = Plotter('sin(x**2) + cos(y**2)')
    assert(Plotter.replace_to_np('sin(x**2) + cos(y**2)') == 'np.sin(x**2) + np.cos(y**2)')

def xmin_test():
    plotter = Plotter('sin(x)')
    assert(plotter._xmin == DEFAULT_MIN_X)

def xmin_test2():
    plotter = Plotter('sin(x)', xmin=10)
    assert(plotter._xmin == 10)
