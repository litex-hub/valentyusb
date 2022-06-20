#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="valentyusb",
    test_suite="test",
    license="BSD",
    python_requires="~=3.6",
    install_requires=[],
    packages=find_packages(exclude=("test*", "sim*", "doc*")),
    include_package_data=True,
    platforms=["Any"],
    keywords="HDL ASIC FPGA hardware design",
    classifiers=[
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
