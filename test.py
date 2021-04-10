import unittest
from main import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_register(self):
        rv = self.app.get('/register')
        self.assertEqual(rv.status, '200 OK')
        #self.assertEqual(rv.data, b'Done\n')
    def test_login(self):
        rv = self.app.get('/login')
        self.assertEqual(rv.status, '200 OK')
    def test_upload(self):
        rv = self.app.get('/analysis')
        self.assertEqual(rv.status, '200 OK')
    def test_logout(self):
        rv = self.app.get('/login')
        self.assertEqual(rv.status, '200 OK')
    
    
    
if __name__ == '__main__':
    unittest.main()
