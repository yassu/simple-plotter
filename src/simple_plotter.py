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
        x = np.linspace(DEFAULT_MIN_X, DEFAULT_MAX_X, DEFAULT_SEP_NUM)
        y = np.sin(x)
        plt.plot(x, y)
