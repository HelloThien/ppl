# Generated from d:\Assigment\NLNNLT\main\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u020f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00a5")
        buf.write("\n\2\3\2\3\2\3\3\3\3\3\4\3\4\7\4\u00ad\n\4\f\4\16\4\u00b0")
        buf.write("\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u00ba\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00c5\n\6\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00cb\n\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u00d4\n\t\3\t\3\t\3\n\3\n\7\n\u00da\n\n\f\n\16\n\u00dd")
        buf.write("\13\n\3\13\3\13\5\13\u00e1\n\13\3\13\6\13\u00e4\n\13\r")
        buf.write("\13\16\13\u00e5\3\f\3\f\3\f\3\f\7\f\u00ec\n\f\f\f\16\f")
        buf.write("\u00ef\13\f\3\r\3\r\3\r\3\r\7\r\u00f5\n\r\f\r\16\r\u00f8")
        buf.write("\13\r\3\16\3\16\3\16\7\16\u00fd\n\16\f\16\16\16\u0100")
        buf.write("\13\16\3\17\3\17\7\17\u0104\n\17\f\17\16\17\u0107\13\17")
        buf.write("\3\17\5\17\u010a\n\17\3\20\3\20\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\7D\u01d7\nD\f")
        buf.write("D\16D\u01da\13D\3E\3E\6E\u01de\nE\rE\16E\u01df\3F\3F\3")
        buf.write("F\3F\7F\u01e6\nF\fF\16F\u01e9\13F\3F\3F\3F\3F\3F\3G\6")
        buf.write("G\u01f1\nG\rG\16G\u01f2\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J")
        buf.write("\7J\u01ff\nJ\fJ\16J\u0202\13J\3J\3J\3J\3K\3K\7K\u0209")
        buf.write("\nK\fK\16K\u020c\13K\3K\3K\3\u01e7\2L\3\3\5\2\7\4\t\2")
        buf.write("\13\5\r\6\17\7\21\b\23\2\25\2\27\t\31\n\33\13\35\2\37")
        buf.write("\2!\2#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67")
        buf.write("\269\27;\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W")
        buf.write("&Y\'[(])_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{")
        buf.write("8}9\177:\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008d")
        buf.write("A\u008fB\u0091\2\u0093C\u0095D\3\2\23\t\2))^^ddhhpptt")
        buf.write("vv\4\2$$^^\4\2GGgg\4\2--//\4\2DDdd\3\2\62\63\4\2ZZzz\4")
        buf.write("\2\63;CH\5\2\62;CHaa\3\2\639\4\2\629aa\3\2\63;\4\2\62")
        buf.write(";aa\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\2\u021f\2\3\3\2\2\2\2\7\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u00a4\3\2\2\2\5\u00a8\3\2\2\2\7\u00aa\3\2\2")
        buf.write("\2\t\u00b9\3\2\2\2\13\u00c4\3\2\2\2\r\u00ca\3\2\2\2\17")
        buf.write("\u00ce\3\2\2\2\21\u00d3\3\2\2\2\23\u00d7\3\2\2\2\25\u00de")
        buf.write("\3\2\2\2\27\u00e7\3\2\2\2\31\u00f0\3\2\2\2\33\u00f9\3")
        buf.write("\2\2\2\35\u0109\3\2\2\2\37\u010b\3\2\2\2!\u010d\3\2\2")
        buf.write("\2#\u010f\3\2\2\2%\u0115\3\2\2\2\'\u011e\3\2\2\2)\u0121")
        buf.write("\3\2\2\2+\u0128\3\2\2\2-\u012d\3\2\2\2/\u0135\3\2\2\2")
        buf.write("\61\u013b\3\2\2\2\63\u013f\3\2\2\2\65\u0142\3\2\2\2\67")
        buf.write("\u0148\3\2\2\29\u0150\3\2\2\2;\u0157\3\2\2\2=\u015e\3")
        buf.write("\2\2\2?\u0163\3\2\2\2A\u0169\3\2\2\2C\u016d\3\2\2\2E\u0171")
        buf.write("\3\2\2\2G\u017d\3\2\2\2I\u0188\3\2\2\2K\u018c\3\2\2\2")
        buf.write("M\u018f\3\2\2\2O\u0192\3\2\2\2Q\u0195\3\2\2\2S\u0199\3")
        buf.write("\2\2\2U\u019c\3\2\2\2W\u019e\3\2\2\2Y\u01a0\3\2\2\2[\u01a2")
        buf.write("\3\2\2\2]\u01a4\3\2\2\2_\u01a6\3\2\2\2a\u01a9\3\2\2\2")
        buf.write("c\u01ab\3\2\2\2e\u01ae\3\2\2\2g\u01b1\3\2\2\2i\u01b4\3")
        buf.write("\2\2\2k\u01b6\3\2\2\2m\u01b8\3\2\2\2o\u01ba\3\2\2\2q\u01bd")
        buf.write("\3\2\2\2s\u01bf\3\2\2\2u\u01c2\3\2\2\2w\u01c4\3\2\2\2")
        buf.write("y\u01c6\3\2\2\2{\u01c8\3\2\2\2}\u01ca\3\2\2\2\177\u01cc")
        buf.write("\3\2\2\2\u0081\u01ce\3\2\2\2\u0083\u01d0\3\2\2\2\u0085")
        buf.write("\u01d2\3\2\2\2\u0087\u01d4\3\2\2\2\u0089\u01db\3\2\2\2")
        buf.write("\u008b\u01e1\3\2\2\2\u008d\u01f0\3\2\2\2\u008f\u01f6\3")
        buf.write("\2\2\2\u0091\u01f9\3\2\2\2\u0093\u01fc\3\2\2\2\u0095\u0206")
        buf.write("\3\2\2\2\u0097\u0098\5\35\17\2\u0098\u0099\5\23\n\2\u0099")
        buf.write("\u009a\5\25\13\2\u009a\u00a5\3\2\2\2\u009b\u009c\5\23")
        buf.write("\n\2\u009c\u009d\5\25\13\2\u009d\u00a5\3\2\2\2\u009e\u009f")
        buf.write("\5\35\17\2\u009f\u00a0\5\25\13\2\u00a0\u00a5\3\2\2\2\u00a1")
        buf.write("\u00a2\5\35\17\2\u00a2\u00a3\5\23\n\2\u00a3\u00a5\3\2")
        buf.write("\2\2\u00a4\u0097\3\2\2\2\u00a4\u009b\3\2\2\2\u00a4\u009e")
        buf.write("\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a7\b\2\2\2\u00a7\4\3\2\2\2\u00a8\u00a9\7$\2\2\u00a9")
        buf.write("\6\3\2\2\2\u00aa\u00ae\5\5\3\2\u00ab\u00ad\5\t\5\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b1\u00b2\5\5\3\2\u00b2\u00b3\b\4\3\2\u00b3\b")
        buf.write("\3\2\2\2\u00b4\u00b5\7^\2\2\u00b5\u00ba\t\2\2\2\u00b6")
        buf.write("\u00b7\7)\2\2\u00b7\u00ba\7$\2\2\u00b8\u00ba\n\3\2\2\u00b9")
        buf.write("\u00b4\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba\n\3\2\2\2\u00bb\u00bc\7V\2\2\u00bc\u00bd\7t\2\2")
        buf.write("\u00bd\u00be\7w\2\2\u00be\u00c5\7g\2\2\u00bf\u00c0\7H")
        buf.write("\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c5\7g\2\2\u00c4\u00bb\3\2\2\2\u00c4\u00bf")
        buf.write("\3\2\2\2\u00c5\f\3\2\2\2\u00c6\u00cb\5\35\17\2\u00c7\u00cb")
        buf.write("\5\33\16\2\u00c8\u00cb\5\31\r\2\u00c9\u00cb\5\27\f\2\u00ca")
        buf.write("\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00ca\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\b")
        buf.write("\7\4\2\u00cd\16\3\2\2\2\u00ce\u00cf\5\35\17\2\u00cf\u00d0")
        buf.write("\5\23\n\2\u00d0\20\3\2\2\2\u00d1\u00d4\5\35\17\2\u00d2")
        buf.write("\u00d4\5\17\b\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\5\25\13\2\u00d6\22")
        buf.write("\3\2\2\2\u00d7\u00db\5u;\2\u00d8\u00da\5!\21\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\24\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00e0\t\4\2\2\u00df\u00e1\t\5\2\2\u00e0\u00df\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e4\5")
        buf.write("!\21\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\26\3\2\2\2\u00e7\u00e8")
        buf.write("\7\62\2\2\u00e8\u00e9\t\6\2\2\u00e9\u00ed\7\63\2\2\u00ea")
        buf.write("\u00ec\t\7\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2")
        buf.write("\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\30\3\2")
        buf.write("\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7\62\2\2\u00f1\u00f2")
        buf.write("\t\b\2\2\u00f2\u00f6\t\t\2\2\u00f3\u00f5\t\n\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\32\3\2\2\2\u00f8\u00f6\3\2")
        buf.write("\2\2\u00f9\u00fa\7\62\2\2\u00fa\u00fe\t\13\2\2\u00fb\u00fd")
        buf.write("\t\f\2\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\34\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0101\u0105\t\r\2\2\u0102\u0104\t\16\2")
        buf.write("\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u010a\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0108\u010a\7\62\2\2\u0109\u0101\3\2\2")
        buf.write("\2\u0109\u0108\3\2\2\2\u010a\36\3\2\2\2\u010b\u010c\t")
        buf.write("\r\2\2\u010c \3\2\2\2\u010d\u010e\t\17\2\2\u010e\"\3\2")
        buf.write("\2\2\u010f\u0110\7D\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7c\2\2\u0113\u0114\7m\2\2\u0114$\3")
        buf.write("\2\2\2\u0115\u0116\7E\2\2\u0116\u0117\7q\2\2\u0117\u0118")
        buf.write("\7p\2\2\u0118\u0119\7v\2\2\u0119\u011a\7k\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7w\2\2\u011c\u011d\7g\2\2\u011d&\3")
        buf.write("\2\2\2\u011e\u011f\7K\2\2\u011f\u0120\7h\2\2\u0120(\3")
        buf.write("\2\2\2\u0121\u0122\7G\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7g\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7h\2\2\u0127*\3\2\2\2\u0128\u0129\7G\2\2\u0129\u012a")
        buf.write("\7n\2\2\u012a\u012b\7u\2\2\u012b\u012c\7g\2\2\u012c,\3")
        buf.write("\2\2\2\u012d\u012e\7H\2\2\u012e\u012f\7q\2\2\u012f\u0130")
        buf.write("\7t\2\2\u0130\u0131\7g\2\2\u0131\u0132\7c\2\2\u0132\u0133")
        buf.write("\7e\2\2\u0133\u0134\7j\2\2\u0134.\3\2\2\2\u0135\u0136")
        buf.write("\7C\2\2\u0136\u0137\7t\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7{\2\2\u013a\60\3\2\2\2\u013b\u013c")
        buf.write("\7K\2\2\u013c\u013d\7p\2\2\u013d\u013e\7v\2\2\u013e\62")
        buf.write("\3\2\2\2\u013f\u0140\7K\2\2\u0140\u0141\7p\2\2\u0141\64")
        buf.write("\3\2\2\2\u0142\u0143\7H\2\2\u0143\u0144\7n\2\2\u0144\u0145")
        buf.write("\7q\2\2\u0145\u0146\7c\2\2\u0146\u0147\7v\2\2\u0147\66")
        buf.write("\3\2\2\2\u0148\u0149\7D\2\2\u0149\u014a\7q\2\2\u014a\u014b")
        buf.write("\7q\2\2\u014b\u014c\7n\2\2\u014c\u014d\7g\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7p\2\2\u014f8\3\2\2\2\u0150\u0151")
        buf.write("\7U\2\2\u0151\u0152\7v\2\2\u0152\u0153\7t\2\2\u0153\u0154")
        buf.write("\7k\2\2\u0154\u0155\7p\2\2\u0155\u0156\7i\2\2\u0156:\3")
        buf.write("\2\2\2\u0157\u0158\7T\2\2\u0158\u0159\7g\2\2\u0159\u015a")
        buf.write("\7v\2\2\u015a\u015b\7w\2\2\u015b\u015c\7t\2\2\u015c\u015d")
        buf.write("\7p\2\2\u015d<\3\2\2\2\u015e\u015f\7P\2\2\u015f\u0160")
        buf.write("\7W\2\2\u0160\u0161\7N\2\2\u0161\u0162\7N\2\2\u0162>\3")
        buf.write("\2\2\2\u0163\u0164\7E\2\2\u0164\u0165\7n\2\2\u0165\u0166")
        buf.write("\7c\2\2\u0166\u0167\7u\2\2\u0167\u0168\7u\2\2\u0168@\3")
        buf.write("\2\2\2\u0169\u016a\7X\2\2\u016a\u016b\7c\2\2\u016b\u016c")
        buf.write("\7n\2\2\u016cB\3\2\2\2\u016d\u016e\7X\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7t\2\2\u0170D\3\2\2\2\u0171\u0172")
        buf.write("\7E\2\2\u0172\u0173\7q\2\2\u0173\u0174\7p\2\2\u0174\u0175")
        buf.write("\7u\2\2\u0175\u0176\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178")
        buf.write("\7w\2\2\u0178\u0179\7e\2\2\u0179\u017a\7v\2\2\u017a\u017b")
        buf.write("\7q\2\2\u017b\u017c\7t\2\2\u017cF\3\2\2\2\u017d\u017e")
        buf.write("\7F\2\2\u017e\u017f\7g\2\2\u017f\u0180\7u\2\2\u0180\u0181")
        buf.write("\7v\2\2\u0181\u0182\7t\2\2\u0182\u0183\7w\2\2\u0183\u0184")
        buf.write("\7e\2\2\u0184\u0185\7v\2\2\u0185\u0186\7q\2\2\u0186\u0187")
        buf.write("\7t\2\2\u0187H\3\2\2\2\u0188\u0189\7P\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7y\2\2\u018bJ\3\2\2\2\u018c\u018d")
        buf.write("\7D\2\2\u018d\u018e\7{\2\2\u018eL\3\2\2\2\u018f\u0190")
        buf.write("\7@\2\2\u0190\u0191\7?\2\2\u0191N\3\2\2\2\u0192\u0193")
        buf.write("\7>\2\2\u0193\u0194\7?\2\2\u0194P\3\2\2\2\u0195\u0196")
        buf.write("\7?\2\2\u0196\u0197\7?\2\2\u0197\u0198\7\60\2\2\u0198")
        buf.write("R\3\2\2\2\u0199\u019a\7-\2\2\u019a\u019b\7\60\2\2\u019b")
        buf.write("T\3\2\2\2\u019c\u019d\7-\2\2\u019dV\3\2\2\2\u019e\u019f")
        buf.write("\7/\2\2\u019fX\3\2\2\2\u01a0\u01a1\7,\2\2\u01a1Z\3\2\2")
        buf.write("\2\u01a2\u01a3\7\61\2\2\u01a3\\\3\2\2\2\u01a4\u01a5\7")
        buf.write("\'\2\2\u01a5^\3\2\2\2\u01a6\u01a7\7#\2\2\u01a7\u01a8\7")
        buf.write("?\2\2\u01a8`\3\2\2\2\u01a9\u01aa\7#\2\2\u01aab\3\2\2\2")
        buf.write("\u01ab\u01ac\7(\2\2\u01ac\u01ad\7(\2\2\u01add\3\2\2\2")
        buf.write("\u01ae\u01af\7~\2\2\u01af\u01b0\7~\2\2\u01b0f\3\2\2\2")
        buf.write("\u01b1\u01b2\7?\2\2\u01b2\u01b3\7?\2\2\u01b3h\3\2\2\2")
        buf.write("\u01b4\u01b5\7?\2\2\u01b5j\3\2\2\2\u01b6\u01b7\7@\2\2")
        buf.write("\u01b7l\3\2\2\2\u01b8\u01b9\7>\2\2\u01b9n\3\2\2\2\u01ba")
        buf.write("\u01bb\7<\2\2\u01bb\u01bc\7<\2\2\u01bcp\3\2\2\2\u01bd")
        buf.write("\u01be\7<\2\2\u01ber\3\2\2\2\u01bf\u01c0\7\60\2\2\u01c0")
        buf.write("\u01c1\7\60\2\2\u01c1t\3\2\2\2\u01c2\u01c3\7\60\2\2\u01c3")
        buf.write("v\3\2\2\2\u01c4\u01c5\7*\2\2\u01c5x\3\2\2\2\u01c6\u01c7")
        buf.write("\7+\2\2\u01c7z\3\2\2\2\u01c8\u01c9\7}\2\2\u01c9|\3\2\2")
        buf.write("\2\u01ca\u01cb\7\177\2\2\u01cb~\3\2\2\2\u01cc\u01cd\7")
        buf.write("=\2\2\u01cd\u0080\3\2\2\2\u01ce\u01cf\7.\2\2\u01cf\u0082")
        buf.write("\3\2\2\2\u01d0\u01d1\7]\2\2\u01d1\u0084\3\2\2\2\u01d2")
        buf.write("\u01d3\7_\2\2\u01d3\u0086\3\2\2\2\u01d4\u01d8\t\20\2\2")
        buf.write("\u01d5\u01d7\t\21\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u0088\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\7&\2\2")
        buf.write("\u01dc\u01de\t\21\2\2\u01dd\u01dc\3\2\2\2\u01de\u01df")
        buf.write("\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u008a\3\2\2\2\u01e1\u01e2\7%\2\2\u01e2\u01e3\7%\2\2\u01e3")
        buf.write("\u01e7\3\2\2\2\u01e4\u01e6\13\2\2\2\u01e5\u01e4\3\2\2")
        buf.write("\2\u01e6\u01e9\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e7\u01e5")
        buf.write("\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea")
        buf.write("\u01eb\7%\2\2\u01eb\u01ec\7%\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("\u01ee\bF\5\2\u01ee\u008c\3\2\2\2\u01ef\u01f1\t\22\2\2")
        buf.write("\u01f0\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f0\3")
        buf.write("\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5")
        buf.write("\bG\5\2\u01f5\u008e\3\2\2\2\u01f6\u01f7\13\2\2\2\u01f7")
        buf.write("\u01f8\bH\6\2\u01f8\u0090\3\2\2\2\u01f9\u01fa\7^\2\2\u01fa")
        buf.write("\u01fb\n\2\2\2\u01fb\u0092\3\2\2\2\u01fc\u0200\5\5\3\2")
        buf.write("\u01fd\u01ff\5\t\5\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3")
        buf.write("\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203")
        buf.write("\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\5\u0091I\2\u0204")
        buf.write("\u0205\bJ\7\2\u0205\u0094\3\2\2\2\u0206\u020a\5\5\3\2")
        buf.write("\u0207\u0209\5\t\5\2\u0208\u0207\3\2\2\2\u0209\u020c\3")
        buf.write("\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020d")
        buf.write("\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\bK\b\2\u020e")
        buf.write("\u0096\3\2\2\2\27\2\u00a4\u00ae\u00b9\u00c4\u00ca\u00d3")
        buf.write("\u00db\u00e0\u00e5\u00ed\u00f6\u00fe\u0105\u0109\u01d8")
        buf.write("\u01df\u01e7\u01f2\u0200\u020a\t\3\2\2\3\4\3\3\7\4\b\2")
        buf.write("\2\3H\5\3J\6\3K\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Float = 1
    String = 2
    Boolean = 3
    Integer = 4
    Poinfloat = 5
    Exponentfloat = 6
    BinaryConstant = 7
    HexadecimalConstant = 8
    OctalConstant = 9
    BREAK = 10
    CONTINUE = 11
    IF = 12
    ELSEIF = 13
    ELSE = 14
    FOREACH = 15
    ARRAYTYPE = 16
    INT = 17
    IN = 18
    FLOATTYPE = 19
    BOOLEANTYPE = 20
    STRINGTYPE = 21
    RETURN = 22
    NULL = 23
    CLASS = 24
    VAL = 25
    VAR = 26
    CONSTRUCTOR = 27
    DESTRUCTOR = 28
    NEW = 29
    BY = 30
    GREQUAL = 31
    LESEQUAL = 32
    DOUEQUALDOT = 33
    ADDDOT = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    MOD = 39
    NOTEQUAL = 40
    NOT = 41
    DOUAND = 42
    DOUOR = 43
    DOUEQUAL = 44
    EQUAL = 45
    GREATER = 46
    LESS = 47
    COLON = 48
    SINGCOLON = 49
    DOTDOT = 50
    DOT = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    SEMI = 56
    COMMA = 57
    LBR = 58
    RBR = 59
    IDENT = 60
    DOLLAR = 61
    COMMENT = 62
    WS = 63
    ERROR_CHAR = 64
    ILLEGAL_ESCAPE = 65
    UNCLOSE_STRING = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'Array'", "'Int'", "'In'", "'Float'", "'Boolean'", "'String'", 
            "'Return'", "'NULL'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
            "'Destructor'", "'New'", "'By'", "'>='", "'<='", "'==.'", "'+.'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!='", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'>'", "'<'", "'::'", "':'", "'..'", "'.'", "'('", 
            "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "Float", "String", "Boolean", "Integer", "Poinfloat", "Exponentfloat", 
            "BinaryConstant", "HexadecimalConstant", "OctalConstant", "BREAK", 
            "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAYTYPE", 
            "INT", "IN", "FLOATTYPE", "BOOLEANTYPE", "STRINGTYPE", "RETURN", 
            "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "GREQUAL", "LESEQUAL", "DOUEQUALDOT", "ADDDOT", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOTEQUAL", "NOT", "DOUAND", 
            "DOUOR", "DOUEQUAL", "EQUAL", "GREATER", "LESS", "COLON", "SINGCOLON", 
            "DOTDOT", "DOT", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "LBR", 
            "RBR", "IDENT", "DOLLAR", "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "Float", "DOUBQUOTE", "String", "LEGAL_THIEN", "Boolean", 
                  "Integer", "Poinfloat", "Exponentfloat", "FRACTION", "EXPONENT", 
                  "BinaryConstant", "HexadecimalConstant", "OctalConstant", 
                  "DecimalConstant", "NonzeroDigit", "Digit", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "ARRAYTYPE", "INT", 
                  "IN", "FLOATTYPE", "BOOLEANTYPE", "STRINGTYPE", "RETURN", 
                  "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "GREQUAL", "LESEQUAL", "DOUEQUALDOT", "ADDDOT", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOTEQUAL", "NOT", 
                  "DOUAND", "DOUOR", "DOUEQUAL", "EQUAL", "GREATER", "LESS", 
                  "COLON", "SINGCOLON", "DOTDOT", "DOT", "LB", "RB", "LP", 
                  "RP", "SEMI", "COMMA", "LBR", "RBR", "IDENT", "DOLLAR", 
                  "COMMENT", "WS", "ERROR_CHAR", "ILL_THIEN", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.Float_action 
            actions[2] = self.String_action 
            actions[5] = self.Integer_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Float_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                  self.text = self.text.replace('_' ,'')
                
     

    def String_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
              
                  self.text = self.text[1:]
                  self.text = self.text[:-1]
                
     

    def Integer_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
              self.text = self.text.replace('_','') 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text[1:])
     


