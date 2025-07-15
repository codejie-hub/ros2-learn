<!-- 创建第一个ros 节点 -->


<!-- 运行节点 -->
<!-- 注意这里chapter01不是一个包，运行会失败 -->
ros2 run chapter01 first_node.py
<!-- success -->
python3 first_node.py

<!-- 查看节点列表 -->
ros2 node list


<!-- 环境变量配置，修改日志的输出格式 -->
export RCUTILS_CONSOLE_OUTPUT_FORMAT=[{function_name}:{line_number}]:{message}
