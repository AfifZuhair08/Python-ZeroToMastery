import main
import unittest

class TestMain(unittest.TestCase):
    
    # to check if value match
    def test_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15) # OK
    
    # to check if type is error equals to TypeError
    def test_stuff_2(self):
        test_param = "ASFASCCWAEFF"
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError)) # OK
    
    # to check if null or no values
    def test_stuff_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please return a number")
        
    # to check if ok if empty
    def test_stuff_4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please return a number")

if __name__ == '__main__':
    unittest.main()