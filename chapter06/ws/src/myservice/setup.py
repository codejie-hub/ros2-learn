from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'myservice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 安装服务定义文件
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
        # ('share/'+ package_name+'srv/*.srv'),
    ],
    install_requires=['setuptools','rosidl_runtime_py',],
    zip_safe=True,
    maintainer='wp',
    maintainer_email='code_jie@163.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serviceNode=myservice.simple_service:main',
            'clientNode=myservice.simple_client:main'
        ],
    },
)
