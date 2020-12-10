from setuptools import setup
from distutils.core import setup, Extension
from Cython.Build import cythonize


setup(
    name="anagrams",
    ext_modules=cythonize('src/anagrams_finder.pyx'),
    install_requires=[
        'Cython~=0.29.21',
        'pytest~=6.1.2',
        'click=7.1.2',
    ],
    entry_points={
        'console_scripts': [
            'anagrams = cli:main',
        ],
    }
)
