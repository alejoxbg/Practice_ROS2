import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Py_node(Node):
    def __init__(self):
        super().__init__('python_publisher')
        self.publisher_= self.create_publisher(String, 'py_str_msg', 10)
        timer_period= 0.5
        self.timer= self.create_timer(timer_period,self.timer_callback)
        self.i=0
    def timer_callback(self):
        msg=String()
        msg.data='Hello C++: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing from python: "%s"' % msg.data)
        self.i+=1

def main(args=None):
    rclpy.init(args=args)
    publisher= Py_node()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()