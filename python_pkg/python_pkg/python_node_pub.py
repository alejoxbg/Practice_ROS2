import rclpy
from cpp_pkg.srv import Customsrvcpp
from rclpy.node import Node
from cpp_pkg.msg import Custommsg

class Py_node(Node):
    def __init__(self):
        #publisher
        super().__init__('python_publisher_service')
        self.publisher_= self.create_publisher(Custommsg, 'py_str_msg', 10)
        timer_period= 0.5
        self.timer= self.create_timer(timer_period,self.timer_callback)
        self.i=0

        #servive
        self.srv=self.create_service(Customsrvcpp, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        #call to the request data and response data
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        return response


    #Pubisher callback
    def timer_callback(self):
        msg=Custommsg()
        msg.msg='Hello C++: '
        msg.num=self.i
        self.publisher_.publish(msg)
        self.i+=1
        self.get_logger().info('Publishing from python: "%s"' % msg.msg)
        

def main(args=None):
    rclpy.init(args=args)
    publisher= Py_node()
    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()