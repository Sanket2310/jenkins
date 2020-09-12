"""Testing module"""
import unittest
import app

class TestBlog(unittest.TestCase):
    """TestBlog Class for defining unit test cases"""
    def setUp(self):
        """Setup function for defining app to be tested"""
        app.app.testing = True
        self.app = app.app.test_client()

    def test_root(self):
        """test case 1 for checking index page"""
        response = self.app.get('/')
        self.assertEqual(response.status, '200 OK')
        print("test1 passed")

    def test_aboutme(self):
        """test case 2 for checking about me page"""
        response = self.app.get('/aboutme')
        self.assertEqual(response.status, '200 OK')
        print("test2 passed")

if __name__ == '__main__':
    unittest.main()
