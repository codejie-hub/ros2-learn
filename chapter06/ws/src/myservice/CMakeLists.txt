cmake_minimum_required(VERSION 3.5)
project(myservice)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/MyService.srv"
)
