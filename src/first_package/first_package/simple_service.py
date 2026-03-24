# The Objective:
# To create a ROS 2 node that provides a service to add two integers and return the sum.

# 1. Import necessary libraries and custom message/service types
import rclpy
from rclpy.node import Node
from first_interfaces.srv import MyService

# 2. Define the AddTwoIntsServer class
class IsOdd(Node):
    def __init__(self):
        super().__init__('is_odd_server')
        
        # 3. Create the service
        # The service name is 'add_two_ints'
        # The service type is 'AddTwoInts'
        # The callback function is 'handle_request'
        self.service = self.create_service(MyService, 'is_odd', self.handle_request)
        self.declare_parameter('inverse', 1)

    # 4. Define the handle_request method to process the request and return the response
    def handle_request(self, request, response):
        # Add the parameter value to the sum
        
        value = self.get_parameter('inverse').get_parameter_value().integer_value
        response.is_odd = (request.number % 2) == value
        self.get_logger().info(f'Received: {request.number} = {response.is_odd}')
        
        # Return the response to the client
        return response

def main(args=None):
    rclpy.init(args=args)
    node = IsOdd()
    rclpy.spin(node)
    rclpy.shutdown()
