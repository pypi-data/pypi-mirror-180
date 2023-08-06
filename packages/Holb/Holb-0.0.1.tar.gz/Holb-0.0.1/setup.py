import os
from setuptools import find_packages, setup
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Holb",
    version="0.0.1",
    author='Viacheslav Hodlevskyi',
    author_email='slavagodlevsky86@gmail.com',
    url="https://github.com/Slava-git/holb.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)