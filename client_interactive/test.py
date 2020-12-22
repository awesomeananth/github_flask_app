#try:
import unittest
from unittest.mock import patch
import client
#except Exception as e:
#    print("import error {}".format(e))

class FlaskTestClient(unittest.TestCase):
   #check for input strings and return
    @patch('client.get_input', return_value='1')
    @patch('client.get_input', return_value='vlang/v')
    def test_input_repo_type(self, input1, input2):
        self.assertEqual(client.get_user_input(), 200)

    #TODO: any other test cases


if __name__ == "__main__":
    unittest.main()
