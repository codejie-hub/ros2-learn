from setuptools import find_packages
from setuptools import setup

setup(
    name='face_interface',
    version='0.0.0',
    packages=find_packages(
        include=('face_interface', 'face_interface.*')),
)
