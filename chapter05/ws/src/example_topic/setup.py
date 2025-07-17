from setuptools import find_packages, setup

package_name = 'example_topic'

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
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_publish_node = example_topic.topic_publish_node:main',
            'topic_subscribe_node = example_topic.topic_subscribe_node:main',
        ],
    },
)
