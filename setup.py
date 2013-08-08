from distutils.core import setup

setup(
    name='MathLib',
    version='0.1.0',
    author='Charles J. Lai',
    author_email='cjl223@cornell.edu',
    packages=['mathlib', 'mathlib.test', 'mathlib.core', 'mathlib.lib', 
    'mathlib.linalg', 'mathlib.numbers', 'mathlib.stats'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Useful, learning focused algorithms and data structures',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)