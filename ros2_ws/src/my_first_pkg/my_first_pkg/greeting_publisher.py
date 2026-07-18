import rclpy                       # the ROS 2 Python client library
from rclpy.node import Node        # base class for every node
from std_msgs.msg import String    # the message type we will publish


class GreetingPublisher(Node):
    def __init__(self):
        super().__init__("greeting_publisher")          # <- the node name in the graph
        # create a publisher: (message type, topic name, queue size)
        self.pub = self.create_publisher(String, "greetings", 10)
        # call self.tick() every 1.0 seconds
        self.timer = self.create_timer(1.0, self.tick)
        self.count = 0
        self.get_logger().info("greeting_publisher is up. Posting to /greetings ...")

    def tick(self):
        msg = String()
        msg.data = f"Hello from Filippo's first node! #{self.count}"
        self.pub.publish(msg)                           # post to the channel
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1


def main(args=None):
    rclpy.init(args=args)          # start up ROS 2
    node = GreetingPublisher()
    try:
        rclpy.spin(node)           # keep the node alive, firing the timer
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()

