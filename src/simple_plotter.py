import re
from optparse import OptionParser
import matplotlib.pyplot as plt
import numpy as np

__version__ = '0.1.0'

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
        self._xmin = kw.get('xmin', DEFAULT_MIN_X)
        self._xmax = kw.get('xmax', DEFAULT_MAX_X)
        self._ymin = kw.get('ymin', DEFAULT_MIN_Y)
        self._ymax = kw.get('ymax', DEFAULT_MAX_Y)
        self._title = kw.get('title', None)

    def replace_to_np(self, func_text):
        for funcname, np_funcname in FUNC_NAMES.items():
            func_text = func_text.replace(funcname, np_funcname)
        return func_text

    def get_varnames(self, func_text):
        matchs = re.findall(VAR_PAT, func_text)
        return set(filter(lambda m: m != '' and m not in FUNC_NAMES, matchs))


    def plot(self, show=True, fig_filename=None):
        if len(self._varnames) == 1:
            self.explicit_2d_plot(show=show)
        elif len(self._varnames) == 2:
            self.explicit_3d_plot(show=show)
        if fig_filename:
            plt.savefig(fig_filename)

    def explicit_2d_plot(self, show=True):
        var = list(self._varnames).pop()
        if self._title:
            plt.title(self._title)
        exec(
        '{var} = np.linspace({xmin}, {xmax}, DEFAULT_SEP_NUM)'.
            format(var=var, xmin=self._xmin, xmax=self._xmax))
        x = np.linspace(self._xmin, self._xmax, DEFAULT_SEP_NUM)
        y = eval(self._func)
        plt.xlim(self._xmin, self._xmax)
        plt.ylim(self._ymin, self._ymax)
        exec('plt.plot({var}, y)'.format(var=var))
        plt.xlabel('{}-axis'.format(var))
        plt.ylabel('{}-axis'.format('y'))
        if show:
            plt.show()

    def explicit_3d_plot(self, show=True):
        from mpl_toolkits.mplot3d import Axes3D
        var1, var2 = list(self._varnames)
        exec('{var1} = np.linspace('
                'self._xmin, self._xmax,'
                'DEFAULT_SEP_NUM)'.format(var1=var1))
        exec('{var2} = np.linspace('
                'self._ymin, self._ymax,'
                'DEFAULT_SEP_NUM)'.format(var2=var2))
        exec('{var1}, {var2} = np.meshgrid({var1}, {var2})'.format(
            var1=var1, var2=var2))
        z = eval(self._func)
        fig = plt.figure()
        ax = Axes3D(fig)
        if self._title:
            ax.set_title(self._title)
        ax.set_xlabel("{}-axis".format(var1))
        ax.set_ylabel("{}-axis".format(var2))
        ax.set_zlabel("{}-axis".format('z'))
        exec('ax.plot_wireframe({}, {}, {})'.format(var1, var2, 'z'))
        if show:
            plt.show()

def get_parser():
    parser = OptionParser(version=__version__)
    parser.add_option(
        '--xmin',
        action='store',
        type='float',
        dest='xmin',
        help='set min of x-value'
    )

    parser.add_option(
        '--xmax',
        action='store',
        type=float,
        dest='xmax',
        help='set max of x-value'
    )

    parser.add_option(
        '--ymin',
        action='store',
        type=float,
        dest='ymin',
        help='set min of y-value'
    )

    parser.add_option(
        '--ymax',
        action='store',
        type=float,
        dest='ymax',
        help='set max of y-value'
    )

    parser.add_option(
        '--title',
        action='store',
        dest='title',
        help='set title of graph'
    )

    return parser

def main():
    parser = get_parser()
    (options, funcnames) = parser.parse_args()

    if len(funcnames) == 0:
        print('Please input function')
        exit()

    funcname = funcnames[0]
    plot_kw = {}
    plot_kw_names = ('xmin', 'xmax', 'ymin', 'ymax', 'title')
    for kw_name in plot_kw_names:
        if getattr(options, kw_name, None) is not None:
            plot_kw[kw_name] = getattr(options, kw_name)

    plotter = Plotter(funcname, **plot_kw)
    plotter.plot()

if __name__ == '__main__':
    main()
