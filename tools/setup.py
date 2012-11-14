#!/bin/env/python

from distutils.core import setup,Extension
from setuptools import find_packages

print find_packages()

setup(
    name = 'vm2cb',
    version = '0.1',
    description= " '2-CB (C-Control-II kompatible virtuelle Maschine).",
    author = 'Christoph Schueler',
    author_email = 'cpu12.gems@googlemail.com',
    url = 'http://www.github.com/Christoph/2vm-2cb',
    packages = ['vm2cb'],
    entry_points = {
	'console_scripts': [
		'vmcldisasm = vmcldisasm:main',
		'vmcinfo = vmcinfo:main',
        ],
    },
    install_requires = ['pyserial', ]
)
