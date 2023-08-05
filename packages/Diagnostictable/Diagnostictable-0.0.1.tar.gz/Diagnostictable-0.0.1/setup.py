from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Diagnostictable',
    version='0.0.1',
    description='This package is for making medication table',
    author= 'Ariana',
    #url = 'https://github.com/Spidy20/PyMusic_Player',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['diagnostic'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['Diagnostictable'],
    package_dir={'':'src'},
    install_requires = [
        'pandas',
        'numpy',
        'datetime'
    ]
)