from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'learning_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch.py')),
        ('share/' + package_name, glob(os.path.join('config', '*.yaml'))),
        ('share/' + package_name, glob(os.path.join('rviz', '*.rviz')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wp',
    maintainer_email='code_jie@163.com',
    description='TODO: Package description',
    license='Apache-2.0',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
