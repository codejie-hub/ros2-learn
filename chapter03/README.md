<!-- 学习：创建多个功能包 -->

<!-- 在当前目录创建工作空间 -->
mkdir -p ws/src

<!-- 切换到工作空间目录 -->
cd ws

<!-- 在src目录下创建多个功能包 -->
ros2 pkg create demo_pkg1 --build-type ament_python --license Apache-2.0
ros2 pkg create demo_pkg2 --build-type ament_python --license Apache-2.0

<!-- 在工作空间下编译 -->
colcon build

<!-- 查看工作空间下的所有包 -->
ls -l ws/src

<!-- 删除编译的结果 -->
rm -rf ws/build ws/install ws/log

<!-- 编译指定的功能包  -->
colcon build --packages-select demo_pkg

<!-- 查看功能包 -->
ros2 pkg list | grep demo_pkg

<!-- 查看包的信息 -->
colcon info demo_pkg


<!-- 一个功能包作为另一个功能包的依赖 -->
例如：demo_pkg 作为 demo2_pkg 的依赖
在demo2_pkg的package.xml中添加demo_pkg的依赖
<depend>demo_pkg</depend>

<!-- 编译demo2_pkg -->
colcon build --packages-select demo2_pkg
或者直接 colcon build

===输出===
Starting >>> demo_pkg
Finished <<< demo_pkg [0.58s]          
Starting >>> demo2_pkg
Finished <<< demo2_pkg [0.57s]          

Summary: 2 packages finished [1.33s]

可以发现先编译依赖包demo_pkg再编译demo2_pkg
