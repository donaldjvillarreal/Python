from arm import Arm
from wheel import Wheel

class Robot:
    def __init__(self):
        self.right_arm = Arm()
        self.left_arm = Arm()
        self.front_right_wheel = Wheel()
        self.back_right_wheel = Wheel()
        self.front_left_wheel = Wheel()
        self.back_left_wheel = Wheel()
        
    def move_forward(self):
        self.front_right_wheel.forward()
        self.back_right_wheel.forward()
        self.front_left_wheel.forward()
        self.back_left_wheel.forward()
        
    def turn_right(self):
        self.front_right_wheel.backward()
        self.back_right_wheel.backward()
        self.front_left_wheel.forward()
        self.back_left_wheel.forward()