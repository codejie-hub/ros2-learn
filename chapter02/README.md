<!-- ros2 创建包 -->
ros2 pkg create demo_pkg --build-type ament_python --license Apache-2.0

<!-- 编译 -->  
colcon build

<!-- 查看环境变量 -->
printenv  | grep PYTHON

<!-- 激活包环境-->
source install/setup.bash

<!-- 运行 -->
<!-- 注意这里node1是可执行文件名称,实际上节点的名称是package_node，为了统一最好将可执行文件名称与节点名称统一 -->
ros2 run demo_pkg node1

<!-- 查看节点 -->
ros2 node list


