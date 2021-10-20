
import unittest
from src.handler import rivr

  
class TestRivrS(unittest.TestCase):
    def test_rivr(self):
        self.assertIn("This is a test for cicd", str(rivr(None, None)), 'dummy message')
  
if __name__ == '__main__':
    unittest.main()
    
