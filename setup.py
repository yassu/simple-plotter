from setuptools import setup
from src.simple_plotter import __version__


setup(
    name='simple-plotter',
    version=__version__,
    author='Yassu',
    description=(
        'simple plotter by using matplotlib in your console'),
    long_description=(
        "This program provides plotter command, for very simple plot.\n"
        "Note that this program depends on matplotlib"
        ),
    url='https://github.com/yassu/simple-plotter',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: Freeware',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers'
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author_email='yassumath@gmail.com',
    license=(
        'Released Under the Apache license\n'
        'https://github.com/yassu/simple-plotter\n'
    ),
    entry_points = {
        'console_scripts': [
            'plotter = src.simple_plotter:main'],
    }
)
