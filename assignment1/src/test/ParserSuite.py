import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: Class main{} """
        input = """Class main  {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_attribute(self):
        """Simple program: Class main{} """
        input = """Class main  {
          Val myconst : Int = 2 + 3 ;
        }"""
        input1 = """Class main  {
          Val myconst , age : Int = 2 + 3, 3 +3 ;
          Var $mysdfs : Float = 2.32 +32.23;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        self.assertTrue(TestParser.test(input1,expect,203))
    def test_blockStatement(self):
        """Simple program: Class main{} """ 
        input1 = """Class main  {
          Val myconst , age : Int = 2 + 3, 3 +3 ;
          Var $mysdfs : Float = 2.32 +32.23;
          main()  {
              val r, s: Int;
               
             
            } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input1,expect,204))
   

    
   