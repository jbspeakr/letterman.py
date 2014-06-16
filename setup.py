import os
from setuptools import setup
from letterman import __version__ as package_version


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='letterman.py',
    version=package_version,
    packages=['letterman', 'letterman.test'],
    url='https://github.com/jbspeakr/letterman.py',
    license='MIT',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    description='  Python lib for creating DIN 5008 and DIN 676 compliant PDF letters.',
    long_description=read('README.md'),
    install_requires=read('requirements.txt').split('\n'),
)
