===================
Simple Plotter
===================

This project is graph plotter by command line.
Note that this project is provide `matplotlib`.

For example, when you run this script as following:

::

    python src/simple_plotter.py 'x**3'

then, you can see following image.

.. image:: http://gyazo.com/baa973f4902a67544fe2eb9b28d6ee64.png
   :alt: x**3
   :width: 218
   :height: 186

Usage
=======

Most simple usage is like as above:

::

    python src/simple_plotter.py {function}

and you can plot parametrix plot(in 2-dimensional) by entering

::

    python src/simple_plotter.py ({x(t)}, {y(t)})

For example,

::

    python src/simple_plotter.py "(t**2, t**3)"

.. image:: http://gyazo.com/bb86b4b5684f20bb01a0a2b7d6a14935.png
   :alt: simple cusp
   :width: 218
   :height: 186

For plot in 3-dimensional space, you can only draw explicit plot by following syntax:

::

    python src/simple_plotter.py "x**2 + y**3"

.. image:: http://gyazo.com/b8145c6317f9414d1fea896a63c89d7d.png
   :alt: x**2 + y**3
   :width: 218
   :height: 186

Options
============

* `--xmin`: set minimum value of `x`
* `--xmax`: set maximum value of `x`
* `--ymin`: set minimum value of `y`
* `--ymax`: set maximum value of `y`
* `--title`: set title of graph
* `--o`, `--save`: save graph as image file, without showing
