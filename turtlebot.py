import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class TurtleBotNavigator(Node):

    def __init__(self):
        super().__init__('turtlebot_navigator')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)  # Publisher to control robot velocity
        self.scan_subscription_ = self.create_subscription(LaserScan, 'scan', self.scan_callback, 10)  # Subscriber for laser scan data
        self.msg_ = Twist()  # Twist message for velocity commands

    def scan_callback(self, msg):
        min_dist = min(msg.ranges)
        if min_dist < 0.5:
            # Obstacle detected, rotate until clear
            self.msg_.linear.x = 0.0
            self.msg_.angular.z = 0.5
        else:
            # No obstacle detected, move forward
            self.msg_.linear.x = 0.5
            self.msg_.angular.z = 0.0
        self.publisher_.publish(self.msg_)

def main(args=None):
    rclpy.init(args=args)
    turtlebot_navigator = TurtleBotNavigator()  # Create an instance of TurtleBotNavigator class
    rclpy.spin(turtlebot_navigator)  # Start the node and spin
    turtlebot_navigator.destroy_node()  # Clean up the node
    rclpy.shutdown()

if __name__ == '__main__':
    main()
