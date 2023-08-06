import os
from setuptools import setup, find_packages


description = open('srsinst/readme.md').read()

setup(
    name='srsinst',
    version='0.0.1',
    description='Namespace package for instrument library from Stanford Research Systems',
    packages=['srsinst'],
    package_data={
        'srsinst': ['../srsinst/readme.md']
    },
    long_description=description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',

    license="MIT license",
    keywords=["SRS", "Stanford Research Systems"],
    author="Chulhoon Kim",
    # author_email="chulhoonk@yahoo.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ]
)
