import re
import matplotlib.pyplot as plt
import numpy as np
FUNC_NAMES = {'sin': 'np.sin', 'cos': 'np.cos', 'tan': 'np.tan'}

DEFAULT_MIN_X = -1
DEFAULT_MAX_X = 1
DEFAULT_MIN_Y = -1
DEFAULT_MAX_Y = 1
DEFAULT_SEP_NUM = 100

VAR_PAT = re.compile('[a-zA-Z]*')
class Plotter(object):
    def __init__(self, func_text, **kw):
        self._varnames = self.get_varnames(func_text)
        self._func = self.replace_to_np(func_text)

    def replace_to_np(self, func_text):
        for funcname, np_funcname in FUNC_NAMES.items():
            func_text = func_text.replace(funcname, np_funcname)
        return func_text

    def get_varnames(self, func_text):
        matchs = re.findall(VAR_PAT, func_text)
        return set(filter(lambda m: m != '' and m not in FUNC_NAMES, matchs))


    def plot(self):
        if len(self._varnames) == 1:
            self.explicit_2d_plot()
        elif len(self._varnames) == 2:
            self.explicit_3d_plot()

    def explicit_2d_plot(self):
        var = list(self._varnames).pop()
        exec(
        '{var} = np.linspace(DEFAULT_MIN_X, DEFAULT_MAX_X, DEFAULT_SEP_NUM)'.
            format(var=var))
        x = np.linspace(DEFAULT_MIN_X, DEFAULT_MAX_X, DEFAULT_SEP_NUM)
        y = eval(self._func)
        exec('plt.plot({var}, y)'.format(var=var))
        plt.show()

    def explicit_3d_plot(self):
        from mpl_toolkits.mplot3d import Axes3D
        var1, var2 = list(self._varnames)
        exec('{var1} = np.linspace('
                'DEFAULT_MIN_X, DEFAULT_MAX_X,'
                'DEFAULT_SEP_NUM)'.format(var1=var1))
        exec('{var2} = np.linspace('
                'DEFAULT_MIN_Y, DEFAULT_MAX_Y,'
                'DEFAULT_SEP_NUM)'.format(var2=var2))
        exec('{var1}, {var2} = np.meshgrid({var1}, {var2})'.format(
            var1=var1, var2=var2))
        z = eval(self._func)
        fig = plt.figure()
        ax = Axes3D(fig)
        exec('ax.plot_wireframe({}, {}, {})'.format(var1, var2, 'z'))
        plt.show()

plotter = Plotter('x**2+y**2')
plotter.explicit_3d_plot()
