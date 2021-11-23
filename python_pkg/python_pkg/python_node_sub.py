import rclpy
from custom_msg_srv.srv import Customsrvcpp
from rclpy.node import Node
from std_msgs.msg import String
import time

class Py_Subscriber(Node):
    def __init__(self):
        #suscriber
        super().__init__('python_subscriber_client')
        self.subscription = self.create_subscription(String,'cpp_str_msg', self.listener_callback,10)
        self.subscription
        #client
        self.cli = self.create_client(Customsrvcpp, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not avaible, waiting again...')
        self.req = Customsrvcpp.Request()
        
                

    def send_request(self):
        self.req.a=1
        self.req.b=2
        wait = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, wait)        
        if wait.result() is not None:  
            self.get_logger().info("Request was '%f' '%f'. Response is '%f'" %(self.req.a, self.req.b, wait.result().sum))   
        else:            
            self.get_logger().info("Request failed")
    
    def listener_callback(self,msg):
        self.get_logger().info('I heard from c++: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    subscriber=Py_Subscriber()
    while rclpy.ok():
        time.sleep(0.5)
        subscriber.send_request()
        rclpy.spin_once(subscriber)
            
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()