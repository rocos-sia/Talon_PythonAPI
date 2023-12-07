# Talon_PythonAPI
    基于proto和grpc实现的对Talon机械臂的python控制
## 功能描述
详细说明：演示Talon_controller.py的使用方法，包括连接机械臂、使能机械臂、关节空间运动、笛卡尔空间运动、获取关节角度、获取法兰位姿
## 运行环境
- python3
- grpcio
- grpcio-tools
- numpy
- protobuf
## 安装
```bash

pip install grpcio
pip install grpcio-tools
pip install numpy
pip install protobuf
```
## 使用方法
```bash
运行机械臂的 grpc 服务
代码在Talon的demo.cpp有示例
核心代码如下：
auto robotService = RobotServiceImpl::getInstance(&robot);
robotService->runServer();
运行启动机械臂的主站和服务程序，以demo.cpp为例
cd build/bin
sudo ./demo

运行python程序
cd Talon_PythonAPI
python3 main.py
```
## 特别说明
机械臂控制柜提供网口，如果远程连接请配置好网口的IP地址，同时修改main.py中的ip。如果是本地连接请将IP地址设置为127.0.0.1
