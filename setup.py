import os
import inspect
from setuptools import find_packages, setup

root = os.path.dirname(os.path.realpath(__file__))
long_description = open(os.path.join(root, 'README.md')).read()

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))

def get_install_requirements(path):
    content = open(os.path.join(__location__, path)).read()
    return [req for req in content.splitlines() if req != '']

setup(
    name='pyforecastapp',
    version='1.0.0',
    description='Python API for ForecastApp.com',
    long_description=long_description,
    url='http://github.com/project-ada/pyforecastapp',
    author='Miiro Juuso',
    author_email='miiro.juuso@artirix.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    keywords='forecast api',
    install_requires=get_install_requirements('requirements.txt')
)
