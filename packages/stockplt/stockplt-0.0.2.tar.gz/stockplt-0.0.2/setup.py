from setuptools import setup, find_packages
# from distutils.core import setup
import codecs
import os


VERSION = '0.0.2'
DESCRIPTION = 'stockplt'

# Setting up
setup(
    name="stockplt",
    version=VERSION,
    author="Hong Tang",
    author_email="<stanghong@gmail.com>",
    description=DESCRIPTION,
    # url = 'https://github.com/stanghong/pypi_publication', 
    # packages=find_packages('addup'),
    packages=[], #'quicklookts'
    install_requires=['numpy','pandas','matplotlib'],
    # download_url = 'https://github.com/stanghong/pypi_publication/archive/refs/tags/v0.0.9.tar.gz',
    
    keywords=['python', 'visualization','plot'],

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
