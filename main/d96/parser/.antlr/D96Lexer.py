# Generated from d:\Assigment\NLNNLT\main\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2P")
        buf.write("\u020e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\7\2\u00a3\n\2\f\2\16\2")
        buf.write("\u00a6\13\2\3\2\3\2\3\3\3\3\5\3\u00ac\n\3\3\4\3\4\6\4")
        buf.write("\u00b0\n\4\r\4\16\4\u00b1\5\4\u00b4\n\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\5\5\u00bb\n\5\3\6\3\6\3\6\3\6\5\6\u00c1\n\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\b\3\b\5\b\u00ca\n\b\3\b\3\b\3\t\3\t")
        buf.write("\6\t\u00d0\n\t\r\t\16\t\u00d1\3\n\3\n\5\n\u00d6\n\n\3")
        buf.write("\n\6\n\u00d9\n\n\r\n\16\n\u00da\3\13\3\13\3\13\6\13\u00e0")
        buf.write("\n\13\r\13\16\13\u00e1\3\f\3\f\6\f\u00e6\n\f\r\f\16\f")
        buf.write("\u00e7\3\r\3\r\3\r\3\16\3\16\3\17\3\17\7\17\u00f1\n\17")
        buf.write("\f\17\16\17\u00f4\13\17\3\20\3\20\3\21\3\21\7\21\u00fa")
        buf.write("\n\21\f\21\16\21\u00fd\13\21\3\21\5\21\u0100\n\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\39\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3=\3=\3")
        buf.write("=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("F\3F\3G\3G\3H\3H\3I\3I\3J\3J\7J\u01dd\nJ\fJ\16J\u01e0")
        buf.write("\13J\3K\3K\3K\3K\7K\u01e6\nK\fK\16K\u01e9\13K\3K\3K\3")
        buf.write("K\3K\3K\3L\6L\u01f1\nL\rL\16L\u01f2\3L\3L\3M\3M\3M\3N")
        buf.write("\3N\6N\u01fc\nN\rN\16N\u01fd\5N\u0200\nN\3N\3N\3O\3O\3")
        buf.write("O\7O\u0207\nO\fO\16O\u020a\13O\3O\3O\3O\4\u00a4\u01e7")
        buf.write("\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write("\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write("N\u009bO\u009dP\3\2\22\3\2$%\4\2GGgg\4\2--//\4\2DDdd\3")
        buf.write("\2\62\63\4\2ZZzz\5\2\62;CHch\3\2\629\3\2\63;\4\2\62;a")
        buf.write("a\3\2\62;\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\t")
        buf.write("\2$$^^ddhhppttvv\5\2\f\f\17\17^^\2\u0225\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2")
        buf.write("\2\5\u00ab\3\2\2\2\7\u00ad\3\2\2\2\t\u00ba\3\2\2\2\13")
        buf.write("\u00c0\3\2\2\2\r\u00c4\3\2\2\2\17\u00c9\3\2\2\2\21\u00cd")
        buf.write("\3\2\2\2\23\u00d3\3\2\2\2\25\u00dc\3\2\2\2\27\u00e3\3")
        buf.write("\2\2\2\31\u00e9\3\2\2\2\33\u00ec\3\2\2\2\35\u00ee\3\2")
        buf.write("\2\2\37\u00f5\3\2\2\2!\u00ff\3\2\2\2#\u0101\3\2\2\2%\u0103")
        buf.write("\3\2\2\2\'\u0105\3\2\2\2)\u0108\3\2\2\2+\u010e\3\2\2\2")
        buf.write("-\u0117\3\2\2\2/\u011a\3\2\2\2\61\u0121\3\2\2\2\63\u0126")
        buf.write("\3\2\2\2\65\u012e\3\2\2\2\67\u0133\3\2\2\29\u0139\3\2")
        buf.write("\2\2;\u013f\3\2\2\2=\u0142\3\2\2\2?\u0146\3\2\2\2A\u014c")
        buf.write("\3\2\2\2C\u0154\3\2\2\2E\u015b\3\2\2\2G\u0162\3\2\2\2")
        buf.write("I\u0167\3\2\2\2K\u016d\3\2\2\2M\u0171\3\2\2\2O\u0175\3")
        buf.write("\2\2\2Q\u0181\3\2\2\2S\u018c\3\2\2\2U\u0190\3\2\2\2W\u0193")
        buf.write("\3\2\2\2Y\u0195\3\2\2\2[\u0197\3\2\2\2]\u0199\3\2\2\2")
        buf.write("_\u019b\3\2\2\2a\u019d\3\2\2\2c\u019f\3\2\2\2e\u01a2\3")
        buf.write("\2\2\2g\u01a5\3\2\2\2i\u01a8\3\2\2\2k\u01aa\3\2\2\2m\u01ad")
        buf.write("\3\2\2\2o\u01af\3\2\2\2q\u01b2\3\2\2\2s\u01b4\3\2\2\2")
        buf.write("u\u01b7\3\2\2\2w\u01bb\3\2\2\2y\u01be\3\2\2\2{\u01c1\3")
        buf.write("\2\2\2}\u01c3\3\2\2\2\177\u01c6\3\2\2\2\u0081\u01c8\3")
        buf.write("\2\2\2\u0083\u01ca\3\2\2\2\u0085\u01cc\3\2\2\2\u0087\u01ce")
        buf.write("\3\2\2\2\u0089\u01d0\3\2\2\2\u008b\u01d2\3\2\2\2\u008d")
        buf.write("\u01d4\3\2\2\2\u008f\u01d6\3\2\2\2\u0091\u01d8\3\2\2\2")
        buf.write("\u0093\u01da\3\2\2\2\u0095\u01e1\3\2\2\2\u0097\u01f0\3")
        buf.write("\2\2\2\u0099\u01f6\3\2\2\2\u009b\u01f9\3\2\2\2\u009d\u0203")
        buf.write("\3\2\2\2\u009f\u00a0\59\35\2\u00a0\u00a4\5\u0081A\2\u00a1")
        buf.write("\u00a3\13\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2")
        buf.write("\2\u00a4\u00a5\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a7")
        buf.write("\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\5\u0083B\2\u00a8")
        buf.write("\4\3\2\2\2\u00a9\u00ac\5\r\7\2\u00aa\u00ac\5\17\b\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\6\3\2\2\2\u00ad")
        buf.write("\u00b3\5\u0089E\2\u00ae\u00b0\n\2\2\2\u00af\u00ae\3\2")
        buf.write("\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\5\u0089")
        buf.write("E\2\u00b6\u00b7\b\4\2\2\u00b7\b\3\2\2\2\u00b8\u00bb\5")
        buf.write("\65\33\2\u00b9\u00bb\5\67\34\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\n\3\2\2\2\u00bc\u00c1\5!\21\2\u00bd")
        buf.write("\u00c1\5\35\17\2\u00be\u00c1\5\27\f\2\u00bf\u00c1\5\25")
        buf.write("\13\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c3\b\6\3\2\u00c3\f\3\2\2\2\u00c4\u00c5\5!\21\2\u00c5")
        buf.write("\u00c6\5\21\t\2\u00c6\16\3\2\2\2\u00c7\u00ca\5!\21\2\u00c8")
        buf.write("\u00ca\5\r\7\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\5\23\n\2\u00cc\20\3\2")
        buf.write("\2\2\u00cd\u00cf\5\177@\2\u00ce\u00d0\5%\23\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\22\3\2\2\2\u00d3\u00d5\t\3\2\2\u00d4")
        buf.write("\u00d6\t\4\2\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d9\5%\23\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\24\3\2\2\2\u00dc\u00dd\7\62\2\2\u00dd\u00df")
        buf.write("\t\5\2\2\u00de\u00e0\t\6\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2")
        buf.write("\u00e2\26\3\2\2\2\u00e3\u00e5\5\31\r\2\u00e4\u00e6\5\33")
        buf.write("\16\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\30\3\2\2\2\u00e9\u00ea")
        buf.write("\7\62\2\2\u00ea\u00eb\t\7\2\2\u00eb\32\3\2\2\2\u00ec\u00ed")
        buf.write("\t\b\2\2\u00ed\34\3\2\2\2\u00ee\u00f2\7\62\2\2\u00ef\u00f1")
        buf.write("\5\37\20\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\36\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f6\t\t\2\2\u00f6 \3\2\2\2\u00f7")
        buf.write("\u00fb\t\n\2\2\u00f8\u00fa\t\13\2\2\u00f9\u00f8\3\2\2")
        buf.write("\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u0100\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe")
        buf.write("\u0100\7\62\2\2\u00ff\u00f7\3\2\2\2\u00ff\u00fe\3\2\2")
        buf.write("\2\u0100\"\3\2\2\2\u0101\u0102\t\n\2\2\u0102$\3\2\2\2")
        buf.write("\u0103\u0104\t\f\2\2\u0104&\3\2\2\2\u0105\u0106\7&\2\2")
        buf.write("\u0106\u0107\5\u0093J\2\u0107(\3\2\2\2\u0108\u0109\7D")
        buf.write("\2\2\u0109\u010a\7t\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7c\2\2\u010c\u010d\7m\2\2\u010d*\3\2\2\2\u010e\u010f")
        buf.write("\7E\2\2\u010f\u0110\7q\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\u0113\7k\2\2\u0113\u0114\7p\2\2\u0114\u0115")
        buf.write("\7w\2\2\u0115\u0116\7g\2\2\u0116,\3\2\2\2\u0117\u0118")
        buf.write("\7K\2\2\u0118\u0119\7h\2\2\u0119.\3\2\2\2\u011a\u011b")
        buf.write("\7G\2\2\u011b\u011c\7n\2\2\u011c\u011d\7u\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\u011f\7k\2\2\u011f\u0120\7h\2\2\u0120\60")
        buf.write("\3\2\2\2\u0121\u0122\7G\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7u\2\2\u0124\u0125\7g\2\2\u0125\62\3\2\2\2\u0126\u0127")
        buf.write("\7H\2\2\u0127\u0128\7q\2\2\u0128\u0129\7t\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a\u012b\7c\2\2\u012b\u012c\7e\2\2\u012c\u012d")
        buf.write("\7j\2\2\u012d\64\3\2\2\2\u012e\u012f\7V\2\2\u012f\u0130")
        buf.write("\7t\2\2\u0130\u0131\7w\2\2\u0131\u0132\7g\2\2\u0132\66")
        buf.write("\3\2\2\2\u0133\u0134\7H\2\2\u0134\u0135\7c\2\2\u0135\u0136")
        buf.write("\7n\2\2\u0136\u0137\7u\2\2\u0137\u0138\7g\2\2\u01388\3")
        buf.write("\2\2\2\u0139\u013a\7C\2\2\u013a\u013b\7t\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013c\u013d\7c\2\2\u013d\u013e\7{\2\2\u013e:\3")
        buf.write("\2\2\2\u013f\u0140\7K\2\2\u0140\u0141\7p\2\2\u0141<\3")
        buf.write("\2\2\2\u0142\u0143\7K\2\2\u0143\u0144\7p\2\2\u0144\u0145")
        buf.write("\7v\2\2\u0145>\3\2\2\2\u0146\u0147\7H\2\2\u0147\u0148")
        buf.write("\7n\2\2\u0148\u0149\7q\2\2\u0149\u014a\7c\2\2\u014a\u014b")
        buf.write("\7v\2\2\u014b@\3\2\2\2\u014c\u014d\7D\2\2\u014d\u014e")
        buf.write("\7q\2\2\u014e\u014f\7q\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151\u0152\7c\2\2\u0152\u0153\7p\2\2\u0153B\3")
        buf.write("\2\2\2\u0154\u0155\7U\2\2\u0155\u0156\7v\2\2\u0156\u0157")
        buf.write("\7t\2\2\u0157\u0158\7k\2\2\u0158\u0159\7p\2\2\u0159\u015a")
        buf.write("\7i\2\2\u015aD\3\2\2\2\u015b\u015c\7T\2\2\u015c\u015d")
        buf.write("\7g\2\2\u015d\u015e\7v\2\2\u015e\u015f\7w\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160\u0161\7p\2\2\u0161F\3\2\2\2\u0162\u0163")
        buf.write("\7P\2\2\u0163\u0164\7W\2\2\u0164\u0165\7N\2\2\u0165\u0166")
        buf.write("\7N\2\2\u0166H\3\2\2\2\u0167\u0168\7E\2\2\u0168\u0169")
        buf.write("\7n\2\2\u0169\u016a\7c\2\2\u016a\u016b\7u\2\2\u016b\u016c")
        buf.write("\7u\2\2\u016cJ\3\2\2\2\u016d\u016e\7X\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7n\2\2\u0170L\3\2\2\2\u0171\u0172")
        buf.write("\7X\2\2\u0172\u0173\7c\2\2\u0173\u0174\7t\2\2\u0174N\3")
        buf.write("\2\2\2\u0175\u0176\7E\2\2\u0176\u0177\7q\2\2\u0177\u0178")
        buf.write("\7p\2\2\u0178\u0179\7u\2\2\u0179\u017a\7v\2\2\u017a\u017b")
        buf.write("\7t\2\2\u017b\u017c\7w\2\2\u017c\u017d\7e\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017e\u017f\7q\2\2\u017f\u0180\7t\2\2\u0180P\3")
        buf.write("\2\2\2\u0181\u0182\7F\2\2\u0182\u0183\7g\2\2\u0183\u0184")
        buf.write("\7u\2\2\u0184\u0185\7v\2\2\u0185\u0186\7t\2\2\u0186\u0187")
        buf.write("\7w\2\2\u0187\u0188\7e\2\2\u0188\u0189\7v\2\2\u0189\u018a")
        buf.write("\7q\2\2\u018a\u018b\7t\2\2\u018bR\3\2\2\2\u018c\u018d")
        buf.write("\7P\2\2\u018d\u018e\7g\2\2\u018e\u018f\7y\2\2\u018fT\3")
        buf.write("\2\2\2\u0190\u0191\7D\2\2\u0191\u0192\7{\2\2\u0192V\3")
        buf.write("\2\2\2\u0193\u0194\7-\2\2\u0194X\3\2\2\2\u0195\u0196\7")
        buf.write("/\2\2\u0196Z\3\2\2\2\u0197\u0198\7,\2\2\u0198\\\3\2\2")
        buf.write("\2\u0199\u019a\7\61\2\2\u019a^\3\2\2\2\u019b\u019c\7\'")
        buf.write("\2\2\u019c`\3\2\2\2\u019d\u019e\7#\2\2\u019eb\3\2\2\2")
        buf.write("\u019f\u01a0\7(\2\2\u01a0\u01a1\7(\2\2\u01a1d\3\2\2\2")
        buf.write("\u01a2\u01a3\7~\2\2\u01a3\u01a4\7~\2\2\u01a4f\3\2\2\2")
        buf.write("\u01a5\u01a6\7?\2\2\u01a6\u01a7\7?\2\2\u01a7h\3\2\2\2")
        buf.write("\u01a8\u01a9\7?\2\2\u01a9j\3\2\2\2\u01aa\u01ab\7#\2\2")
        buf.write("\u01ab\u01ac\7?\2\2\u01acl\3\2\2\2\u01ad\u01ae\7@\2\2")
        buf.write("\u01aen\3\2\2\2\u01af\u01b0\7@\2\2\u01b0\u01b1\7?\2\2")
        buf.write("\u01b1p\3\2\2\2\u01b2\u01b3\7>\2\2\u01b3r\3\2\2\2\u01b4")
        buf.write("\u01b5\7>\2\2\u01b5\u01b6\7?\2\2\u01b6t\3\2\2\2\u01b7")
        buf.write("\u01b8\7?\2\2\u01b8\u01b9\7?\2\2\u01b9\u01ba\7\60\2\2")
        buf.write("\u01bav\3\2\2\2\u01bb\u01bc\7-\2\2\u01bc\u01bd\7\60\2")
        buf.write("\2\u01bdx\3\2\2\2\u01be\u01bf\7<\2\2\u01bf\u01c0\7<\2")
        buf.write("\2\u01c0z\3\2\2\2\u01c1\u01c2\7<\2\2\u01c2|\3\2\2\2\u01c3")
        buf.write("\u01c4\7\60\2\2\u01c4\u01c5\7\60\2\2\u01c5~\3\2\2\2\u01c6")
        buf.write("\u01c7\7\60\2\2\u01c7\u0080\3\2\2\2\u01c8\u01c9\7*\2\2")
        buf.write("\u01c9\u0082\3\2\2\2\u01ca\u01cb\7+\2\2\u01cb\u0084\3")
        buf.write("\2\2\2\u01cc\u01cd\7}\2\2\u01cd\u0086\3\2\2\2\u01ce\u01cf")
        buf.write("\7\177\2\2\u01cf\u0088\3\2\2\2\u01d0\u01d1\7$\2\2\u01d1")
        buf.write("\u008a\3\2\2\2\u01d2\u01d3\7=\2\2\u01d3\u008c\3\2\2\2")
        buf.write("\u01d4\u01d5\7.\2\2\u01d5\u008e\3\2\2\2\u01d6\u01d7\7")
        buf.write("]\2\2\u01d7\u0090\3\2\2\2\u01d8\u01d9\7_\2\2\u01d9\u0092")
        buf.write("\3\2\2\2\u01da\u01de\t\r\2\2\u01db\u01dd\t\16\2\2\u01dc")
        buf.write("\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u0094\3\2\2\2\u01e0\u01de\3")
        buf.write("\2\2\2\u01e1\u01e2\7%\2\2\u01e2\u01e3\7%\2\2\u01e3\u01e7")
        buf.write("\3\2\2\2\u01e4\u01e6\13\2\2\2\u01e5\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e9\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2")
        buf.write("\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\7")
        buf.write("%\2\2\u01eb\u01ec\7%\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee")
        buf.write("\bK\4\2\u01ee\u0096\3\2\2\2\u01ef\u01f1\t\17\2\2\u01f0")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\b")
        buf.write("L\4\2\u01f5\u0098\3\2\2\2\u01f6\u01f7\13\2\2\2\u01f7\u01f8")
        buf.write("\bM\5\2\u01f8\u009a\3\2\2\2\u01f9\u01ff\5\u0089E\2\u01fa")
        buf.write("\u01fc\n\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3")
        buf.write("\2\2\2\u01ff\u01fb\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0202\bN\6\2\u0202\u009c\3\2\2\2\u0203")
        buf.write("\u0208\7$\2\2\u0204\u0207\t\20\2\2\u0205\u0207\n\21\2")
        buf.write("\2\u0206\u0204\3\2\2\2\u0206\u0205\3\2\2\2\u0207\u020a")
        buf.write("\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209")
        buf.write("\u020b\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020c\7$\2\2")
        buf.write("\u020c\u020d\bO\7\2\u020d\u009e\3\2\2\2\31\2\u00a4\u00ab")
        buf.write("\u00b1\u00b3\u00ba\u00c0\u00c9\u00d1\u00d5\u00da\u00e1")
        buf.write("\u00e7\u00f2\u00fb\u00ff\u01de\u01e7\u01f2\u01fd\u01ff")
        buf.write("\u0206\u0208\b\3\4\2\3\6\3\b\2\2\3M\4\3N\5\3O\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Array = 1
    Float = 2
    String = 3
    Boolean = 4
    Integer = 5
    Poinfloat = 6
    Exponentfloat = 7
    FRACTION = 8
    EXPONENT = 9
    BinaryConstant = 10
    HexadecimalConstant = 11
    HexadecimalPrefix = 12
    HexadecimalDigit = 13
    OctalConstant = 14
    OctalDigit = 15
    DecimalConstant = 16
    NonzeroDigit = 17
    Digit = 18
    DOLLAR = 19
    BREAK = 20
    CONTINUE = 21
    IF = 22
    ELSEIF = 23
    ELSE = 24
    FOREACH = 25
    TRUE = 26
    FALSE = 27
    ARRAYTYPE = 28
    IN = 29
    INT = 30
    FLOATTYPE = 31
    BOOLEANTYPE = 32
    STRINGTYPE = 33
    RETURN = 34
    NULL = 35
    CLASS = 36
    VAL = 37
    VAR = 38
    CONSTRUCTOR = 39
    DESTRUCTOR = 40
    NEW = 41
    BY = 42
    ADD = 43
    SUB = 44
    MUL = 45
    DIV = 46
    MOD = 47
    NOT = 48
    DOUAND = 49
    DOUOR = 50
    DOUEQUAL = 51
    EQUAL = 52
    NOTEQUAL = 53
    GREATER = 54
    GREQUAL = 55
    LESS = 56
    LESEQUAL = 57
    DOUEQUALDOT = 58
    ADDDOT = 59
    COLON = 60
    SINGCOLON = 61
    DOTDOT = 62
    DOT = 63
    LB = 64
    RB = 65
    LP = 66
    RP = 67
    DOUBQUOTE = 68
    SEMI = 69
    COMMA = 70
    LBR = 71
    RBR = 72
    IDENT = 73
    COMMENT = 74
    WS = 75
    ERROR_CHAR = 76
    UNCLOSE_STRING = 77
    ILLEGAL_ESCAPE = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'NULL'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
            "'!='", "'>'", "'>='", "'<'", "'<='", "'==.'", "'+.'", "'::'", 
            "':'", "'..'", "'.'", "'('", "')'", "'{'", "'}'", "'\"'", "';'", 
            "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "Array", "Float", "String", "Boolean", "Integer", "Poinfloat", 
            "Exponentfloat", "FRACTION", "EXPONENT", "BinaryConstant", "HexadecimalConstant", 
            "HexadecimalPrefix", "HexadecimalDigit", "OctalConstant", "OctalDigit", 
            "DecimalConstant", "NonzeroDigit", "Digit", "DOLLAR", "BREAK", 
            "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
            "ARRAYTYPE", "IN", "INT", "FLOATTYPE", "BOOLEANTYPE", "STRINGTYPE", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "DOUAND", 
            "DOUOR", "DOUEQUAL", "EQUAL", "NOTEQUAL", "GREATER", "GREQUAL", 
            "LESS", "LESEQUAL", "DOUEQUALDOT", "ADDDOT", "COLON", "SINGCOLON", 
            "DOTDOT", "DOT", "LB", "RB", "LP", "RP", "DOUBQUOTE", "SEMI", 
            "COMMA", "LBR", "RBR", "IDENT", "COMMENT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "Array", "Float", "String", "Boolean", "Integer", "Poinfloat", 
                  "Exponentfloat", "FRACTION", "EXPONENT", "BinaryConstant", 
                  "HexadecimalConstant", "HexadecimalPrefix", "HexadecimalDigit", 
                  "OctalConstant", "OctalDigit", "DecimalConstant", "NonzeroDigit", 
                  "Digit", "DOLLAR", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAYTYPE", "IN", 
                  "INT", "FLOATTYPE", "BOOLEANTYPE", "STRINGTYPE", "RETURN", 
                  "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "DOUAND", "DOUOR", "DOUEQUAL", "EQUAL", "NOTEQUAL", "GREATER", 
                  "GREQUAL", "LESS", "LESEQUAL", "DOUEQUALDOT", "ADDDOT", 
                  "COLON", "SINGCOLON", "DOTDOT", "DOT", "LB", "RB", "LP", 
                  "RP", "DOUBQUOTE", "SEMI", "COMMA", "LBR", "RBR", "IDENT", 
                  "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[2] = self.String_action 
            actions[4] = self.Integer_action 
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def String_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
              self.text = self.text.replace('"','') 
     

    def Integer_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
              self.text = self.text.replace('_','') 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text.replace('"',''))
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text)
     


