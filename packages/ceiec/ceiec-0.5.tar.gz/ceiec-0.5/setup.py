from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.5'
DESCRIPTION = 'Paquete para uso exclusivo de miembros del CEIEC'

# Setting up
setup(
    name="ceiec",
    version=VERSION,
    author="CEIEC members",
    author_email="<ceiec@ceiec.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'CEIEC'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)