from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ur5e_demo'

def package_files(directory):
    """
    递归收集目录下的所有文件，并保持目录结构
    """
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(path, filename)
            install_path = os.path.join('share', package_name, path)
            paths.append((install_path, [file_path]))
    return paths

mesh_files = package_files('meshes')

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        # (os.path.join('share', package_name, 'meshes'), glob('meshes/**/*',recursive=True)),
    ]+mesh_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wp',
    maintainer_email='code_jie@163.com',
    description='TODO: Package description',
    license='Apach-2.0',
    entry_points={
        'console_scripts': [
        ],
    },
)
