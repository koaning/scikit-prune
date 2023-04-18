import os
from setuptools import setup, find_packages

base_packages = [
    "scikit-learn>=1.0.0",
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="scikit-prune",
    version="0.1.0",
    description="Prune your sklearn models.",
    author="Vincent D. Warmerdam",
    url="https://github.com/koaning/scikit-prune",
    packages=find_packages(exclude=["notebooks", "tests"]),
    package_data={},
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=base_packages,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)