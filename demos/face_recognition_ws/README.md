## 使用自定义的服务接口创建人脸识别服务

### 创建服务接口功能包

```
ros2 pkg create face_interface --dependencies sensor_msgs rosidl_default_generators --license Apache-2.0
```
 
### 项目结构

```
.
└── face_interface
    ├── CMakeLists.txt
    ├── LICENSE
    ├── package.xml
    └── srv
```

### 配置步骤

#### 1.在CMakeLists.txt文件中添加生成服务接口的CMake指令

```
rosidl_generate_interfaces(${PROJECT_NAME} 
  "srv/FaceDetector.srv"
  DEPENDENCIES sensor_msgs
)
```

#### 2.在package.xml中添加接口包标识

```xml
  <member_of_group>rosidl_interface_packages</member_of_group>
```
`<member_of_group>rosidl_interface_packages</member_of_group>`：这个标签将当前包face_interface声明为`rosidl_interface_packages`组的成员


### 构建和使用

```
colcon build
```

```
source install/setup.bash
```

#### 查看服务接口

```
ros2 interface show face_interface/srv/FaceDetector
```


# 创建服务功能包

```
ros2 pkg create demo_python_service --build-type ament_python --dependencies rclpy face_interface --license Apache-2.0
```





