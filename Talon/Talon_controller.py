import robot_service_pb2_grpc
import robot_service_pb2
import grpc
import robot_info_pb2
import robot_command_pb2
import geometry_pb2
import robot_state_pb2
import numpy as np
import Translate as T
import math

class TalonController:
    def __init__(self, ip='127.0.01', port=30001):
        self.channel = grpc.insecure_channel(f'{ip}:{port}')
        self.stub = robot_service_pb2_grpc.RobotServiceStub(self.channel)

    def moveJ(self, q, speed, acceleration, time=0, radius=0, asynchronous=False):
        request = robot_command_pb2.RobotCommandRequest()
        movej = request.command.motion_command.move_j
        for angle in q:
            print(f"q: {angle}")
            movej.q.data.append(angle)
        movej.speed = speed
        movej.acceleration = acceleration
        movej.time = time
        movej.radius = radius
        movej.asynchronous = asynchronous
        self._send_command(request)
    def moveL(self, pose, speed, acceleration, time=0, radius=0, asynchronous=False):
        request = robot_command_pb2.RobotCommandRequest()
        movel = request.command.motion_command.move_l
        movel.pose.position.x, movel.pose.position.y, movel.pose.position.z = pose[:3]
        
        quat = T.rpy2quat(pose[3:])
        print(f"command: {pose[3:]}")
        movel.pose.rotation.x, movel.pose.rotation.y, movel.pose.rotation.z, movel.pose.rotation.w = quat
        movel.speed = speed
        movel.acceleration = acceleration
        movel.time = time
        movel.radius = radius
        movel.asynchronous = asynchronous
        self._send_command(request)
    def movej_IK(self,pose,speed,acceleration,time=0,radius=0,asyncronous=False):
        # Assuming stub is your gRPC client stub
        request = robot_command_pb2.RobotCommandRequest()
        move_j_ik = request.command.motion_command.move_j_ik
        move_j_ik.pose.position.x = pose[0]
        move_j_ik.pose.position.y = pose[1]
        move_j_ik.pose.position.z = pose[2]
        quat=T.rpy2quat([pose[3],pose[4],pose[5]])
        move_j_ik.pose.rotation.x = quat[0]
        move_j_ik.pose.rotation.y = quat[1]
        move_j_ik.pose.rotation.z = quat[2]
        move_j_ik.pose.rotation.w = quat[3]
        move_j_ik.speed = speed
        move_j_ik.acceleration = acceleration
        move_j_ik.time = time
        move_j_ik.radius = radius
        move_j_ik.asynchronous = asyncronous
        self._send_command(request)
    def moveL_FK(self,q,speed,acceleration,time=0,radius=0,asyncronous=False):
        # Assuming stub is your gRPC client stub
        request = robot_command_pb2.RobotCommandRequest()
        move_l_fk = request.command.motion_command.move_l_fk
        move_l_fk.q.data.append(q[0])
        move_l_fk.q.data.append(q[1])
        move_l_fk.q.data.append(q[2])
        move_l_fk.q.data.append(q[3])
        move_l_fk.q.data.append(q[4])
        move_l_fk.q.data.append(q[5])
        move_l_fk.q.data.append(q[6])
        move_l_fk.speed = speed
        move_l_fk.acceleration = acceleration
        move_l_fk.time = time
        move_l_fk.radius = radius
        move_l_fk.asynchronous = asyncronous
        self._send_command(request)
    def setRobotEnabled(self,state):
    # Assuming stub is your gRPC client stub
        request = robot_command_pb2.RobotCommandRequest()
        if state:
            enabled=request.command.enabled
            enabled.CopyFrom(robot_command_pb2.Enabled())
            self._send_command(request)
        else:
            disabled=request.command.disabled
            disabled.CopyFrom(robot_command_pb2.Disabled())
            self._send_command(request)
    def getjointPosition(self,id):
        response=self.stub.ReadRobotState(robot_state_pb2.RobotStateRequest())
        if response:
            print("Get joint position Ok")
            return response.robot_state.joint_states[id].position
        else:
            print("Get joint position Error")
            return None 
    def getFlangePosition(self):
        response=self.stub.ReadRobotState(robot_state_pb2.RobotStateRequest())
        if response:
            pose = response.robot_state.flange_state.pose
            # 四元数转rpy
            # pos_rpy=T.quat2rpy([pose.position.x,pose.position.y,pose.position.z,pose.rotation.x,pose.rotation.y,pose.rotation.z,pose.rotation.w])
            pos_rpy=T.quat2rpy([pose.rotation.x,pose.rotation.y,pose.rotation.z,pose.rotation.w])
            pos=np.array([pose.position.x,pose.position.y,pose.position.z,pos_rpy[0],pos_rpy[1],pos_rpy[2]])
            print("Get flange position Ok")
            return pos
        else:
            print("Get flange position Error")
            return None
    def _send_command(self, request):
        status = self.stub.WriteRobotCommmand(request)
        if status:
            print("Send command Ok")
        else:
            print("Send command Error")