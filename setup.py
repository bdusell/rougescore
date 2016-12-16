from setuptools import setup, find_packages
import os
import codecs

base_dir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as fin:
    long_description = fin.read()

setup(
    name='rougescore',
    version='0.1.0',
    description='Python implementation of ROUGE',
    long_description=long_description,
    url='https://github.com/bdusell/rougescore',
    author='Brian DuSell',
    author_email='bdusell@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering'
    ],
    keywords='nlp rouge summarization evaluation',
    packages=['rougescore'],
    install_requires=['six']
)
