from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='',
    author='Oghenetega Biokoro',
    author_email='teggyg123@gmail.com'
)