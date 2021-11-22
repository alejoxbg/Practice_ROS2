import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Py_Subscriber(Node):
    def __init__(self):
        super().__init__('python_subscriber')
        self.subscription = self.create_subscription(String,'cpp_str_msg', self.listener_callback,10)
        self.subscription
    
    def listener_callback(self,msg):
        self.get_logger().info('I heard from c++: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    subscriber=Py_Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()