import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main {} """
        input = """Class main
         {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """Class main {
            Var $name : Int ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) Ckass main( {}"""
        input = """Class main( {}"""
        expect = "Error on line 1 col 10: ("
        self.assertTrue(TestParser.test(input,expect,203))
    def test_attribute(self):
        """Miss ) Ckass main( {}"""
        input = """Class main {
          Val age , num : Int = 2 +3 ,34;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_attbute(self):
        """Miss ) Ckass main( {}"""
        input = """Class main {
          Val age , num : Int = 2 +3 ,34;
          Var $name , $age : String = "thien", 23;
  
           getArea() {
             Return a + b[5];
             Return Self.length * Self.width;
          }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_attbute(self):
        """Miss ) Ckass main( {}"""
        input =  """
                Class Rectangle: Shape {
                getArea() {
                  Val age , num : Int = 2 +3 ,34;
                  Foreach (i In 1 .. 100 By 2) {
                  Continue;
                  Out.printInt(i);
                  }
                  If(age < 3 ) {

                  }  
                  Elseif() {}
                  Else{}
                  Shape::$getNumOfShape();

                  Break;
                  Return Self.length * Self.width;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_class2(self):
        """Miss ) Ckass main( {}"""
        input =  """
                Class Rectangle: Shape {
                getArea() {
                  Val age , num : Int = 2 +3 ,34;
                  Foreach (i In 1 .. 100 By 2) {
                  Continue;
                  Out.printInt(i);
                  }
                  If(age < 3 ) {

                  }  
                  Elseif() {}
                  Else{}
                  Shape::$getNumOfShape();

                  Break;
                  Return Self.length * Self.width;
                }
            }
                Class Shape{
                  getHeight(){
                    If(){
                      If(){
                        If(){

                        }
                      }
                    }
                  }
                  setWidth(){

                  }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_class2(self): 
        input =  """
                Class Rectangle: Shape {
                getArea() {
                  Val age , num : Int = 2 +3 ,34;
                  Foreach (i In 1 .. 100 By 2) {
                  Continue;
                  Out.printInt(i);
                  }
                  If(age < 3 ) {

                  }  
                  Elseif() {}
                  Else{}
                  Shape::$getNumOfShape();

                  Break;
                  Return Self.length * Self.width;
                }
            }
                Class Shape{
                  getHeight(){
                    If(){
                      If(){
                        If(){
                            self.FindName();
                        }
                      }
                    }
                  }
                  setWidth(){

                  }
                }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    