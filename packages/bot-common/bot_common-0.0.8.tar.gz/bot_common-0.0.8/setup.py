from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.8'
DESCRIPTION = 'Common libraries AISAC Bot'
LONG_DESCRIPTION = 'A package that contains the common libraries for the AISAC Bot'

# Setting up
setup(
    name="bot_common",
    version=VERSION,
    author="cla.fragomeli_92",
    author_email="<cla.fragomeli@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['SQLAlchemy==1.4.29', 'mysql-connector-python-rf==2.2.2', 'PyYAML==5.4.1', 'pydantic==1.9.0'],
    zip_safe=False
)
