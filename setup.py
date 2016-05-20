import os
import inspect
from setuptools import find_packages, setup

root = os.path.dirname(os.path.realpath(__file__))

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

setup(
    name='pyforecastapp',
    version='1.0.2',
    description='Python API for ForecastApp.com',
    long_description='Python API for ForecastApp.com. See http://github.com/project-ada/pyforecastapp',
    url='http://github.com/project-ada/pyforecastapp',
    author='Miiro Juuso',
    author_email='miiro.juuso@artirix.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    keywords='forecast api',
    install_requires=['requests']
)
