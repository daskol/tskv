#!/usr/bin/env python3
#   encoding: utf8
#   setup.py

"""TSKV

Implementation of Tab-Separated Key-Value file format in Python 3.
"""

from setuptools import setup


DOCLINES = (__doc__ or '').split('\n')

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
Intended Audience :: Information Technology
Intended Audience :: Other Audience
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS
Operating System :: POSIX :: Linux
Operating System :: Microsoft :: Windows
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Topic :: Internet
Topic :: Internet :: Log Analysis
Topic :: Other/Nonlisted Topic
Topic :: Scientific/Engineering
Topic :: Software Development
Topic :: Software Development :: Libraries
Topic :: Text Processing
Topic :: Utilities
"""

PLATFORMS = [
    'Mac OS-X',
    'Linux',
    'Solaris',
    'Unix',
    'Windows',
]

MAJOR = 0
MINOR = 0
PATCH = 0

VERSION = '{0:d}.{1:d}.{2:d}'.format(MAJOR, MINOR, PATCH)


def setup_package():
    setup(
        name='tskv',
        version=VERSION,
        description = DOCLINES[0],
        long_description = '\n'.join(DOCLINES[2:]),
        author='Daniel Bershatsky',
        author_email='daniel.bershatsky@skolkovotech.ru',
        license='MIT',
        platforms=PLATFORMS,
        classifiers=[line for line in CLASSIFIERS.split('\n') if line],
        py_modules=[
            'tskv',
        ],
    )


if __name__ == '__main__':
    setup_package()
