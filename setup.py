import setuptools
from distutils.core import setup

with open("README.rst", "r") as rmf:
    long_description = rmf.read()

setup(
    name='easy-regex',
    version= '0.0.1',
    description=(
        'Pre-defined regex'
    ),
    author='YimingQiu',
    author_email='yiming404@gmial.com',
    py_modules = ['easy-regex'],
    license='MIT License',
    url='https://github.com/yimingq/easy-regex',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    
    long_description=long_description,
)
