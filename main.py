# 代码功能：演示Talon_controller.py的使用方法
# 详细说明：演示Talon_controller.py的使用方法，包括连接机械臂、使能机械臂、关节空间运动、笛卡尔空间运动、获取关节角度、获取法兰位姿
# 代码核心：Talon_controller.py
# 代码版本：V1.0

import sys
sys.path.append('Talon')
import Talon_controller as TC

import math
if __name__ == '__main__':
    # 连接机械臂
    ip='127.0.0.1'
    port=30001
    Talon=TC.TalonController(ip,port)
    # 使能机械臂
    Talon.setRobotEnabled(True)
    # 关节空间运动
    q=[0,math.pi/4,0,math.pi/2,0,math.pi/4,math.pi/4] 
    speed=0.7
    acceleration=0.7
    Talon.moveJ(q,speed,acceleration)
    # getjointPosition(id) id代表关节号
    print(Talon.getjointPosition(1))
    # getFlangePosition() 获取法兰的位姿
    pose=Talon.getFlangePosition()
    print(pose)
    # 笛卡尔空间运动
    pose[2]+=0.1
    Talon.moveL(pose,0.1,0.5)
    Talon.setRobotEnabled(False)