from setuptools import find_packages, setup

package_name = 'camera_vis'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wp',
    maintainer_email='code_jie@163.com',
    description='TODO: Package description',
    license='Apach-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_subscriber = camera_vis.camera_Img_sub:main',
        ],
    },
)
