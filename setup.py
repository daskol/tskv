#!/usr/bin/env python3
#   encoding: utf8
#   setup.py

"""TSKV

Implementation of Tab-Separated Key-Value file format in Python 3.
"""

from setuptools import setup, find_packages
from subprocess import Popen, PIPE


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

# Reference version that could be clarify with git tags
MAJOR = 0
MINOR = 0
PATCH = 0

VERSION = '{0:d}.{1:d}.{2:d}'.format(MAJOR, MINOR, PATCH)
VERSION_PATH = 'tskv/version.py'
VERSION_FILE = """\
#   encoding: utf8
#   version.py
#   This file is generated from setup.py

MAJOR = {major:d}
MINOR = {minor:d}
PATCH = {patch:d}
COMMIT = {commit:d}

SHORT_VERSION = '{version:s}'
VERSION = '{version:s}'
FULL_VERSION = '{full_version:s}'

REVISION = '{revision}'
"""


def get_git_version():
    env = dict()
    command = ('git', 'describe', '--long')

    with Popen(command, stdout=PIPE, env=env) as proc:
        stdout, _ = proc.communicate()
        gitver = stdout.decode().rstrip()

    version, commit, hash = gitver.split('-')

    globals()['VERSION'] = version  # fix package version

    commit = int(commit)
    rev = hash[1:]

    major, minor, patch = map(int, version[1:].split('.'))

    return gitver, version, (major, minor, patch), commit, rev

def write_version(**kwargs):
    content = VERSION_FILE.format(**kwargs)

    with open(VERSION_PATH, 'w') as fout:
        fout.write(content)

def setup_version():
    version_info = get_git_version()
    gitver, version, (major, minor, patch), commit, rev = version_info

    write_version(**dict(
        major=major,
        minor=minor,
        patch=patch,
        commit=commit,
        revision=rev,
        version=version,
        full_version=gitver))

def setup_package():
    setup_version()
    setup(
        name='tskv',
        version=VERSION,
        description = DOCLINES[0],
        long_description = '\n'.join(DOCLINES[2:]),
        author='Daniel Bershatsky',
        author_email='daniel.bershatsky@skolkovotech.ru',
        url='https://github.com/daskol/tskv',
        license='MIT',
        platforms=PLATFORMS,
        classifiers=[line for line in CLASSIFIERS.split('\n') if line],
        packages=find_packages())


if __name__ == '__main__':
    setup_package()
