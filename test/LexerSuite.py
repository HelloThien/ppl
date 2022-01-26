import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_comment(self):
        self.assertTrue(
            TestLexer.test("## hello thien####", "Error Token #", 101))
        self.assertTrue(TestLexer.test("## hello \n thien##", "<EOF>", 102))

    def test_identifiers(self):
        self.assertTrue(TestLexer.test("test_case", "test_case,<EOF>", 103))
        self.assertTrue(
            TestLexer.test("test_case_20", "test_case_20,<EOF>", 104))
        self.assertTrue(TestLexer.test("ah?cd", "ah,Error Token ?", 1041))

    def test_dollar(self):
        self.assertTrue(TestLexer.test("$", "Error Token $", 105))
        self.assertTrue(
            TestLexer.test("$test_case_12", "$test_case_12,<EOF>", 106))

    def test_operator(self):
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 107))
        self.assertTrue(TestLexer.test("::", "::,<EOF>", 108))

    def test_interger(self):
        self.assertTrue(TestLexer.test("0123", "0123,<EOF>", 109))
        self.assertTrue(TestLexer.test("0x1A", "0x1A,<EOF>", 110))
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 111))
        self.assertTrue(TestLexer.test("1_434", "1434,<EOF>", 112))

    def test_float(self):
        self.assertTrue(TestLexer.test("123.123", "123.123,<EOF>", 115))
        # self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",116))
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 117))

    def test_stringliteral(self):
        self.assertTrue(TestLexer.test("thien", "thien,<EOF>", 113))
        self.assertTrue(TestLexer.test(""" "anh thien" """, "anh thien,<EOF>", 114))
        self.assertTrue(TestLexer.test(""" "anhn fsdf  ""","Unclosed String: anhn fsdf  ",118))
        
    def test_arrayliteral(self):
        self.assertTrue(TestLexer.test("Array(1, 5, 7, 12)", "Array(1, 5, 7, 12),<EOF>", 119))
        self.assertTrue(TestLexer.test( """Array("Kangxi", "Yongzheng", "Qianlong")""", """Array("Kangxi", "Yongzheng", "Qianlong"),<EOF>""", 120))
    
    def test_attribbuteee(self):
        self.assertTrue(TestLexer.test("$Val r ", "val r, s: Int;,<EOF>", 122))
        self.assertTrue(TestLexer.test("Val r , s : Int;", "val r, s: Int;,<EOF>", 121))
         