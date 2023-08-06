# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:19:14 2022

@author: MI19288
"""

from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'Witsi Witsi - Diagramador de mallas'
LONG_DESCRIPTION = 'Descripción larga en proceso...'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="Witsi", 
        version=VERSION,
        author="Rodrigo H",
        author_email="<andreafernanda.muniz@bbva.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests",
                          "pandas",
                          "matplotlib",
                          "networkx",
                          "graphviz"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'Witsi Wisti'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
