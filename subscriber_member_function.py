import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class SquareNumber(Node):

    def __init__(self):
        super().__init__('kvadriranje_broja')
        self.subscription = self.create_subscription(
            Int64,
            '/broj',  # Pretplata na temu /topic
            self.callback,
            10)
        self.publisher = self.create_publisher(
            Int64,
            '/kvadrat_broja',  # Objavljivanje na temu /kvadrat_broja
            10)

    def callback(self, msg):
        # Kvadriranje broja
        squared_number = msg.data ** 2
        # Objavljivanje kvadriranog broja
        self.publisher.publish(Int64(data=squared_number))

def main(args=None):
    rclpy.init(args=args)
    square_node = SquareNumber()
    rclpy.spin(square_node)
    square_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
