from setuptools import setup

setup(
    name='oscillations',
    version='1.0',
    description='Calculate neutrino oscillation probabilities easily',
    author='Daniel I. Scully',
    # author_email='',
    packages=['oscillations'],
    # install_requires=['', ''], # external packages as dependencies
    extras_require={
        'ROOT':  ["ROOT>=6.1"],
    }
)

