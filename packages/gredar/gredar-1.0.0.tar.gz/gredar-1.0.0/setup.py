from setuptools import setup

setup(
    name='gredar',
    version='1.0.0',
    packages=['gredar'],
    install_requires=['asyncio'],
    author='Bernward Sanchez',
    author_email='contact@bern.codes',
    description='A package for allocating missing memory when using asyncio'
)
