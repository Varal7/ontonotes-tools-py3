#!/usr/bin/env python

from distutils.core import setup

setup(name='ontonotes-tools-py3',
      version='0.1.0',
      description='OntoNotes DB Tool for Python 3',
      author='Victor Quach (credit Sameer Pradhan and Jeff Kaufman)',
      python_requires='>=3.5',
      packages=['on', 'on.corpora', 'on.common', 'on.tools'],
      package_dir={'on': 'src/on',
                   'on.corpora': 'src/on/corpora',
                   'on.common': 'src/on/common',
                   'on.tools': 'src/on/tools'}
     )
