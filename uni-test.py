import unittest
import port_scanner

class TestPortScanner(unittest.TestCase):

    def test_static_scan(self):
        result = port_scanner.static_scan()
        self.assertIsNotNone(result)

    def test_user_input_scan(self):
        # simulate user input
        port_scanner.input = lambda _: "www.google.com\n80\n"
        result = port_scanner.user_input_scan()
        self.assertIsNotNone(result)

    def test_specific_port(self):
        # simulate user input
        port_scanner.input = lambda _: "www.google.com\n80,443\n"
        result = port_scanner.specific_port()
        self.assertIsNotNone(result)

    def test_p_range(self):
        # simulate user input
        port_scanner.input = lambda _: "www.google.com\n80-90\n"
        result = port_scanner.p_range()
        self.assertIsNotNone(result)

    def test_all(self):
        # simulate user input
        port_scanner.input = lambda _: "www.google.com\n"
        result = port_scanner.all()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()


