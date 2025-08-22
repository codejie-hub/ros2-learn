from setuptools import find_packages, setup

package_name = 'tf_pkg_test'

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
    license='TODO: License declaration',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tf_publisher = tf_pkg_test.tf_publisher:main',
            'tf_subscriber = tf_pkg_test.tf_subscriber:main',
        ],
    },
)
