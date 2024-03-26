import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64  

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('brojcanik')
        self.publisher_ = self.create_publisher(Int64, '/broj', 10)  #
        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 1

    def timer_callback(self):
        msg = Int64()  
        msg.data = self.i
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    brojcanik = MinimalPublisher()

    rclpy.spin(brojcanik)

    brojcanik.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

