#!/usr/bin/env python
from setuptools import setup, find_packages

version = '2.0.1'

with open("./README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="PyMyORM",
    version=version,
    url='https://github.com/oldjun/PyMyORM',
    author='JP Chen',
    author_email='oldjun@sina.com',
    description='Pure Python MySQL ORM',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
    install_requires=[
        'PyMySQL>=1.0.2'
    ],
    license="MIT",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
    ],
)
