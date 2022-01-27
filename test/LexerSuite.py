# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
      
#     def test_comment(self):
#         self.assertTrue(
#             TestLexer.test("## hello thien####", "Error Token #", 101))
#         self.assertTrue(TestLexer.test("## hello \n thien##", "<EOF>", 102))

#     def test_identifiers(self):
#         self.assertTrue(TestLexer.test("test_case", "test_case,<EOF>", 103))
#         self.assertTrue(
#             TestLexer.test("test_case_20", "test_case_20,<EOF>", 104))
#         self.assertTrue(TestLexer.test("ah?cd", "ah,Error Token ?", 1041))

#     def test_dollar(self):
#         self.assertTrue(TestLexer.test("$", "Error Token $", 105))
#         self.assertTrue(
#             TestLexer.test("$test_case_12", "$test_case_12,<EOF>", 106))

#     def test_operator(self):
#         self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 107))
#         self.assertTrue(TestLexer.test("::", "::,<EOF>", 108))

#     def test_interger(self):
#         self.assertTrue(TestLexer.test("0123", "0123,<EOF>", 109))
#         self.assertTrue(TestLexer.test("0x1A", "0x1A,<EOF>", 110))
#         self.assertTrue(TestLexer.test("0", "0,<EOF>", 111))
#         self.assertTrue(TestLexer.test("1_434", "1434,<EOF>", 112))

#     def test_float(self):
#         self.assertTrue(TestLexer.test("123.123", "123.123,<EOF>", 115))
#         # self.assertTrue(TestLexer.test("1_234.567","1234.567,<EOF>",116))
#         self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 117))

#     def test_stringliteral(self):
#         self.assertTrue(TestLexer.test("thien", "thien,<EOF>", 113))
#         self.assertTrue(TestLexer.test(""" "anh thien" """, "anh thien,<EOF>", 114))
#         self.assertTrue(TestLexer.test(""" "anhn fsdf  ""","Unclosed String: anhn fsdf  ",118))
        
#     def test_arrayliteral(self):
#         self.assertTrue(TestLexer.test("Array(1, 5, 7, 12)", "Array(1, 5, 7, 12),<EOF>", 119))
#         self.assertTrue(TestLexer.test( """Array("Kangxi", "Yongzheng", "Qianlong")""", """Array("Kangxi", "Yongzheng", "Qianlong"),<EOF>""", 120))
#     def test_checkstring(self):
#         self.assertTrue(TestLexer.test(""" "thien \\h " """, "Illegal Escape In String: thien \h", 120))
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
   def test_102(self):
      input = """_Phan_tu1 Phan tu so2 """
      expect = "_Phan_tu1,Phan,tu,so2,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 102))
   def test_103(self):
      input = """A_B__1_3 ; D1A2 """
      expect = "A_B__1_3,;,D1A2,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 103))
   def test_104(self):
      input = """$abc$123$2a$HCM1 """
      expect = "$abc,$123,$2a,$HCM1,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 104))
   def test_105(self):
      input = """hoten@gmail.com"""
      expect = "hoten,Error Token @"
      self.assertTrue(TestLexer.test(input,expect, 105))
   def test_106(self):
      input = """Tp.Ho-Chi-Minh"""
      expect = "Tp,.,Ho,-,Chi,-,Minh,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 106))
   def test_107(self):
      input = """123 456 789"""
      expect = "123,456,789,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 107))
   def test_108(self):
      input = """123 0456 0xA1BC2 0B101"""
      expect = "123,0456,0xA1BC2,0B101,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 108))
   def test_109(self):
      input = """0XABCD 0ABCD"""
      expect = "0XABCD,0,ABCD,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 109))
   def test_110(self):
      input = """0b10x456"""
      expect = "0b10,x456,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 110))
   
   def test_112(self):
      input = """1.0 2.23 2e1 10.2e5 """
      expect = "1.0,2.23,2e1,10.2e5,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 112))
  
   def test_114(self):
      input = """abc+.987E654"""
      expect = "abc,+.,987E654,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 114))
   def test_114(self):
      input = """abc+.987E654"""
      expect = "abc,+.,987E654,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 114))
   def test_115(self):
      input = """0120XArray"""
      expect = "0120,XArray,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 115))   
   def test_116(self):
      input = """$a+$1e2-$1.0e3"""
      expect = "$a,+,$1e2,-,$1,.0e3,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 116))
   
   def test_118(self):
      input = """1:10+A-F"""
      expect = "1,:,10,+,A,-,F,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 118))
   def test_119(self):
      input = """True or False"""
      expect = "True,or,False,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 119))
   def test_120(self):
      input = """I like 0xFalse"""
      expect = "I,like,0xF,alse,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 120))
   def test_121(self):
      input = """ "This is a string" """
      expect = "This is a string,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 121))
   def test_122(self):
      input = """ "This is a string" """
      expect = "This is a string,<EOF>"
      self.assertTrue(TestLexer.test(input,expect, 122))
    
   def test_124(self):
      input = """ "This is a string and \\n new line" """
      expect = """This is a string and \\n new line,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 124))
   def test_125(self):
      input = """ "Many escape characters \\n \\t \\f . Example" """
      expect = """Many escape characters \\n \\t \\f . Example,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 125))
   def test_126(self):
      input = """ "ABCD \\k DEFG" """
      expect = """Illegal Escape In String: ABCD \\k"""
      self.assertTrue(TestLexer.test(input,expect, 126))
   def test_127(self):
      input = """ "One two three four """
      expect = """Unclosed String: One two three four """
      self.assertTrue(TestLexer.test(input,expect, 127))
   def test_128(self):
      input = """ "3210 + 123" - "123 """
      expect = """3210 + 123,-,Unclosed String: 123 """
      self.assertTrue(TestLexer.test(input,expect, 128))
   def test_129(self):
      input = """ "Something wrong \\\\ but it's true" """
      expect = """Something wrong \\\\ but it's true,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 129))
   def test_130(self):
      input = """ "Now it's \\wrong" """
      expect = """Illegal Escape In String: Now it's \\w"""
      self.assertTrue(TestLexer.test(input,expect, 130))
   def test_131(self):
      input = """ Array(1, 5, 7, 12) """
      expect = """Array,(,1,,,5,,,7,,,12,),<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 131))
   def test_132(self):
      input = """ Array(1.52, "Yongzheng", True) """
      expect = """Array,(,1.52,,,Yongzheng,,,True,),<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 132))
   def test_133(self):
      input = """ arr = New Array() """
      expect = """arr,=,New,Array,(,),<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 133))
      
   def test_134(self):
      input = """ Array (
Array("Volvo", "22", "18"),
Array("Saab", "5", "2"),
Array("Land Rover", "17", "15")
)"""
      expect = """Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 134))
   def test_135(self):
      input = """ Val a : Array[Int, 5]"""
      expect = """Val,a,:,Array,[,Int,,,5,],<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 135))
   def test_136(self):
      input = """ a[1], a[2], a[3], a[4], a[5] """
      expect = """a,[,1,],,,a,[,2,],,,a,[,3,],,,a,[,4,],,,a,[,5,],<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 136))
   def test_137(self):
      input = """Val My1stCons, My2ndCons: Int = 1 + 5, 2;
Var $x, $y : Int = 0, 0;"""
      expect = """Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,Var,$x,,,$y,:,Int,=,0,,,0,;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 137))
   def test_138(self):
      input = """ Class Shape {
Val $numOfShape: Int = 0;
Var length, width: Int;
} """
      expect = """Class,Shape,{,Val,$numOfShape,:,Int,=,0,;,Var,length,,,width,:,Int,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 138))
   def test_139(self):
      input = """Class Child: Parent{
      getName() {
         Return Self.Firstname + Self.Lastname;
      }
}"""
      expect = """Class,Child,:,Parent,{,getName,(,),{,Return,Self,.,Firstname,+,Self,.,Lastname,;,},},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 139))
   def test_140(self):
      input = """ arr["first"] = "One"; """
      expect = """arr,[,first,],=,One,;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 140))
   def test_141(self):
      input = """ If (a==b) {r = a||b;}
Elseif (a<b)  {r = a;}
Else {r = b;}"""
      expect = """If,(,a,==,b,),{,r,=,a,||,b,;,},Elseif,(,a,<,b,),{,r,=,a,;,},Else,{,r,=,b,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 141))
   def test_142(self):
      input = """Foreach (i In 1 .. 100 By 2) {
Out.printInt(i);
}"""
      expect = """Foreach,(,i,In,1,..,100,By,2,),{,Out,.,printInt,(,i,),;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 142))
   def test_143(self):
      input = """Foreach (x In 5 .. 2) {
Break;
Continue;
}"""
      expect = """Foreach,(,x,In,5,..,2,),{,Break,;,Continue,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 143))
   def test_144(self):
      input = """If (a>=18){
Human.BMI = Human.Height * Human.Height / Human.Weight; 
}"""
      expect = """If,(,a,>=,18,),{,Human,.,BMI,=,Human,.,Height,*,Human,.,Height,/,Human,.,Weight,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 144))
   def test_145(self):
      input = """thongtin = DHBK[STT].getInfo();
ten = DHBK[STT].name;"""
      expect = """thongtin,=,DHBK,[,STT,],.,getInfo,(,),;,ten,=,DHBK,[,STT,],.,name,;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 145))
   def test_146(self):
      input = """{ lh = a + b - c * d / e % f;
str = str.first +. str.second ==. str.third;
}"""
      expect = """{,lh,=,a,+,b,-,c,*,d,/,e,%,f,;,str,=,str,.,first,+.,str,.,second,==.,str,.,third,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 146))
   def test_147(self):
      input = """ () [] {} ({[]})"""
      expect = """(,),[,],{,},(,{,[,],},),<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 147))
   def test_148(self):
      input = """A::$gmail = abc @ gmail.com"""
      expect = """A,::,$gmail,=,abc,Error Token @"""
      self.assertTrue(TestLexer.test(input,expect, 148))
   def test_149(self):
      input = """ A4::$$2 = 20;"""
      expect = """A4,::,Error Token $"""
      self.assertTrue(TestLexer.test(input,expect, 149))
   def test_150(self):
      input = """Class A:B{
   Val $a,b: Array[Int,5] = 12;
}
C = New A();"""
      expect = """Class,A,:,B,{,Val,$a,,,b,:,Array,[,Int,,,5,],=,12,;,},C,=,New,A,(,),;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 150))
   def test_151(self):
      input = """New AB().CD.EF(gh=123)[4+5];"""
      expect = """New,AB,(,),.,CD,.,EF,(,gh,=,123,),[,4,+,5,],;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 151))
   def test_152(self):
      input = """If (Grade::New(Array[String,a[02]])) 1=2;"""
      expect = """If,(,Grade,::,New,(,Array,[,String,,,a,[,02,],],),),1,=,2,;,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 152))
   def test_153(self):
      input = """Foreach ($a In a .. b By 2) If (a % 3 > 0) {Out.print($a);}"""
      expect = """Foreach,(,$a,In,a,..,b,By,2,),If,(,a,%,3,>,0,),{,Out,.,print,(,$a,),;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 153))
   def test_154(self):
      input = """ Arr[New $Color()] = Array("Red", "Blue);"""
      expect = """Arr,[,New,$Color,(,),],=,Array,(,Red,,,Unclosed String: Blue);"""
      self.assertTrue(TestLexer.test(input,expect, 154))
   def test_155(self):
      input = """ A.1>A.2>A.3 == A.4<A.5<A.6  """
      expect = """A,.,1,>,A,.,2,>,A,.,3,==,A,.,4,<,A,.,5,<,A,.,6,<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 155))
   def test_156(self):
      input = """Int Sum(a,b,c){
   Var s : Int = a + b + c;
   Return s;  
}"""
      expect = """Int,Sum,(,a,,,b,,,c,),{,Var,s,:,Int,=,a,+,b,+,c,;,Return,s,;,},<EOF>"""
      self.assertTrue(TestLexer.test(input,expect, 156))
      
      