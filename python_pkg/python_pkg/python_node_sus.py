import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Py_Suscriber(Node):
    def __init__(self):
        super().__init__('python_suscriber')
        self.suscription = self.create_subscription(String,'cpp_str_msg', self.listener_callback,10)
        self.suscription
    
    def listener_callback(self,msg):
        self.get_logger().info('I heard from c++: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    suscriber=Py_Suscriber()
    rclpy.spin(suscriber)
    suscriber.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()