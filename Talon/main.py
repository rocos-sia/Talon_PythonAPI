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
    print(Talon.getjointPosition(1))
    pose=Talon.getFlangePosition()
    
    print(pose)
    # 笛卡尔空间运动
    pose[2]+=0.1
    Talon.moveL(pose,0.1,0.5)
    Talon.setRobotEnabled(False)