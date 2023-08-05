from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path


# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='papysql',
    package_dir = {'': 'papysql'},
    packages=find_packages('papysql'),
    version='0.1.2',
    long_description='This is a library to interface SQL with python. The basic library read the tables with list_tables method and read them with display_table. When a table is red is then converted into a pandas DataFrame. Moreover it gives the possibility to read a SQL script that builds a db with ExecuteScriptFromFile',
    author='Francesco Gualdi',
    license='MIT'
)
