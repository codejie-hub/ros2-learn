# ROS2 Launch文件学习与实战

本篇博客将带你系统学习 ROS2 中 launch 文件的编写与使用，涵盖多节点启动、参数传递、资源重映射、参数文件配置、launch文件嵌套等核心内容，并结合实际代码案例进行讲解。

---

## 一、多个节点如何启动

在 ROS2 中，launch 文件可以同时启动多个节点。例如，`simple.launch.py` 文件如下：

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='talk_listen',
            executable='talker',
            output='screen'
        ),
        Node(
            package='talk_listen',
            executable='listener',
            output='screen'
        ),
    ])
```

只需一条命令即可启动所有节点：

```bash
ros2 launch learning_launch simple.launch.py
```

---

## 二、参数值传递

ROS2 节点参数可以通过 launch 文件直接传递，也可以通过命令行传递。

### 1. launch文件内参数传递

`parameters.launch.py` 演示了如何在 launch 文件中声明参数，并传递给节点：

```python
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

def generate_launch_description():
   background_r_launch_arg = DeclareLaunchArgument(
      'r', default_value=TextSubstitution(text='0')
   )
   background_g_launch_arg = DeclareLaunchArgument(
      'g', default_value=TextSubstitution(text='84')
   )
   background_b_launch_arg = DeclareLaunchArgument(
      'b', default_value=TextSubstitution(text='122')
   )

   return LaunchDescription([
      background_r_launch_arg,
      background_g_launch_arg,
      background_b_launch_arg,
      Node(
         package='turtlesim',
         executable='turtlesim_node',
         name='sim',
         parameters=[{
            'background_r': LaunchConfiguration('r'),
            'background_g': LaunchConfiguration('g'),
            'background_b': LaunchConfiguration('b'),
         }]
      ),
   ])
```

### 2. 命令行参数传递

也可以通过命令行直接传递参数：

```bash
ros2 run turtlesim turtlesim_node --ros-args -p background_r:=255 -p background_g:=255 -p background_b:=255
```

---

## 三、资源重映射

资源重映射是指在节点启动时，将节点内部使用的话题、服务等资源名临时替换为你指定的新名字，无需修改节点源码。

`remapping.launch.py` 示例：

```python
Node(
    package='turtlesim',
    executable='mimic',
    name='mimic',
    remappings=[
        ('/input/pose', '/turtlesim1/turtle1/pose'),
        ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
    ]
)
```

这样，`mimic` 节点内部订阅 `/input/pose` 实际会订阅 `/turtlesim1/turtle1/pose`，发布 `/output/cmd_vel` 实际会发布到 `/turtlesim2/turtle1/cmd_vel`。

---

## 四、为launch文件添加参数

通过 `DeclareLaunchArgument` 可以为 launch 文件添加参数，方便在启动时灵活配置。例如：

```python
DeclareLaunchArgument('r', default_value='0')
```

启动时可以通过命令行覆盖：

```bash
ros2 launch learning_launch parameters.launch.py r:=255
```

---

## 五、通过参数文件配置

参数文件（YAML）可以集中管理节点参数，便于维护和复用。

`parameters_yaml.launch.py` 示例：

```python
config = os.path.join(
    get_package_share_directory('learning_launch'),
    'config',
    'turtlesim.yaml'
)
Node(
    package='turtlesim',
    executable='turtlesim_node',
    namespace='turtlesim2',
    name='sim',
    parameters=[config]
)
```

YAML 文件内容示例：

```yaml
ros__parameters:
  background_r: 255
  background_g: 255
  background_b: 255
```

注意事项：
- YAML 文件必须被正确安装到包的 share 目录（需在 setup.py 的 data_files 中声明）。
- 格式必须规范。顶层必须是节点名或命名空间
  如果你用的是 launch 文件的parameters=[config] 方式，推荐如下写法：

```yaml
turtlesim_node:
  ros__parameters:
    background_r: 255
    background_g: 255
    background_b: 255
```
或者如果有命名空间：

```yaml
turtlesim2:
  sim:
    ros__parameters:
      background_r: 255
      background_g: 255
      background_b: 255
```
---

## 六、launch文件包含其他launch文件

复杂系统可通过主 launch 文件包含多个子 launch 文件，实现分层管理。

`namespaces.launch.py` 示例：

```python
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import PushRosNamespace

parameter_yaml = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([
        os.path.join(get_package_share_directory('learning_launch'), 'launch'),
        '/parameters_nonamespace.launch.py'])
)

parameter_yaml_with_namespace = GroupAction(
    actions=[
        PushRosNamespace('turtlesim2'),
        parameter_yaml
    ]
)

return LaunchDescription([
    parameter_yaml_with_namespace
])
```
一个 launch 文件如何包含其他多个 launch 文件
方法一：使用 IncludeLaunchDescription
你可以在主 launch 文件中包含其他 launch 文件：

```python
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
import os

def generate_launch_description():
    launch_dir = os.path.join(
        get_package_share_directory('your_package'),
        'launch'
    )
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'sub1.launch.py'))
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'sub2.launch.py'))
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        )
    ])
```
方法二：参数传递
你可以在包含时传递参数：
```python
IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(launch_dir, 'sub.launch.py')),
    launch_arguments={'param1': 'value1'}.items()
)
```


**注意事项：**
- 使用 `IncludeLaunchDescription` 包含其他 launch 文件时，路径要正确。
- 可以通过 `GroupAction` 和 `PushRosNamespace` 给包含的节点统一加命名空间。
- 参数和命名空间的传递要保持一致，避免冲突。

---

## 七、其他实用案例

### 启动 RViz 并加载配置

`rviz.launch.py` 示例：

```python
rviz_config = os.path.join(
    get_package_share_directory('learning_launch'),
    'rviz',
    'test.rviz'
)
Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    arguments=['-d', rviz_config]
)
```

---

## 总结

通过本篇博客，你可以掌握 ROS2 launch 文件的多节点启动、参数传递、资源重映射、参数文件配置、launch文件嵌套等实用技巧。  
建议结合实际代码多练习，遇到问题多查日志和路径，逐步提升 ROS2 项目开发能力！

如需启动示例：

```bash
ros2 launch learning_launch rviz.launch.py
```
