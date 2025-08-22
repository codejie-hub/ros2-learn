from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'tf_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wp',
    maintainer_email='code_jie@163.com',
    description='TODO: Package description',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'static_tf_publish = tf_test.tf_static_publish:main',
            'dynamic_tf_publish = tf_test.tf_dynamic_publish:main',
            'tf_subscribe = tf_test.tf_subscribe:main'
        ],
    },
)
