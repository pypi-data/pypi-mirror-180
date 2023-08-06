import os
from setuptools import find_packages, setup
import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Holb",
    version="0.0.2",
    author='Viacheslav Hodlevskyi',
    author_email='slavagodlevsky86@gmail.com',
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Slava-git/holb.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)