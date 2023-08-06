import os
from setuptools import setup, find_packages
from glob import glob

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

exec(open('cvnets/__version__.py').read())
setup(
    name="cvnets",
    version=__version__,
    author="Jihoon Lucas Kim",
    description="Library for Computer Vision Deep Learning Networks",
    packages=find_packages(),
    package_data={'cvnets': ['**/*.yaml']},
    include_package_data=True,
)

