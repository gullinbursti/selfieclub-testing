import os.path
import unittest
import client

def fake_urlopen():
	client.clubname()
    	# Map path from url to a file
    	resource_file = os.path.normpath('tests/resources/users/test_user')
	r = open(resource_file, mode='rb')
    	p = r.readline()
    	return int(p)

class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
	self.count = client.count()
	self.count2 = fake_urlopen()

    def test_request(self):
        """Test a simple request."""
        self.assertEqual(self.count, self.count2)
