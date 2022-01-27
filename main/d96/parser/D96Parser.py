# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u01a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\7\2X\n\2\f\2\16")
        buf.write("\2[\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3c\n\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\7\4l\n\4\f\4\16\4o\13\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7")
        buf.write("\u0081\n\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b\u0089\n\b\f\b\16")
        buf.write("\b\u008c\13\b\3\b\3\b\3\b\5\b\u0091\n\b\3\b\3\b\5\b\u0095")
        buf.write("\n\b\3\t\3\t\3\t\3\t\7\t\u009b\n\t\f\t\16\t\u009e\13\t")
        buf.write("\3\t\3\t\3\t\5\t\u00a3\n\t\3\t\3\t\5\t\u00a7\n\t\3\n\3")
        buf.write("\n\3\n\7\n\u00ac\n\n\f\n\16\n\u00af\13\n\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u00b5\n\13\f\13\16\13\u00b8\13\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u00bf\n\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00ca\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\5\20\u00d6\n\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\7\21\u00de\n\21\f\21\16\21\u00e1\13\21")
        buf.write("\3\22\3\22\5\22\u00e5\n\22\3\22\3\22\3\22\7\22\u00ea\n")
        buf.write("\22\f\22\16\22\u00ed\13\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u00f5\n\23\f\23\16\23\u00f8\13\23\3\23\3\23\3")
        buf.write("\24\3\24\5\24\u00fe\n\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u0108\n\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0118")
        buf.write("\n\27\3\27\3\27\3\27\3\30\3\30\7\30\u011f\n\30\f\30\16")
        buf.write("\30\u0122\13\30\3\30\5\30\u0125\n\30\3\31\3\31\3\31\5")
        buf.write("\31\u012a\n\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\5\33\u0135\n\33\3\33\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0140\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u014c\n\36\3\37\3\37\3")
        buf.write(" \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\5&\u0160")
        buf.write("\n&\3\'\3\'\3\'\3\'\7\'\u0166\n\'\f\'\16\'\u0169\13\'")
        buf.write("\3(\3(\5(\u016d\n(\3)\3)\3)\3)\3)\3)\5)\u0175\n)\3)\3")
        buf.write(")\3)\5)\u017a\n)\7)\u017c\n)\f)\16)\u017f\13)\5)\u0181")
        buf.write("\n)\3)\5)\u0184\n)\3*\3*\3*\3*\3*\3*\5*\u018c\n*\3*\3")
        buf.write("*\3*\5*\u0191\n*\7*\u0193\n*\f*\16*\u0196\13*\5*\u0198")
        buf.write("\n*\3*\5*\u019b\n*\3+\3+\3+\7+\u01a0\n+\f+\16+\u01a3\13")
        buf.write("+\3+\3+\3+\3\u01a1\2,\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\n\3\2>?\4")
        buf.write("\2\6\6>>\6\2!\"%*..\60\61\5\2!\"%(\60\61\3\2#$\3\2%)\4")
        buf.write("\2##+-\6\2!\"**,,\60\61\2\u01bd\2Y\3\2\2\2\4^\3\2\2\2")
        buf.write("\6f\3\2\2\2\br\3\2\2\2\nx\3\2\2\2\f\u0080\3\2\2\2\16\u0084")
        buf.write("\3\2\2\2\20\u0096\3\2\2\2\22\u00a8\3\2\2\2\24\u00b0\3")
        buf.write("\2\2\2\26\u00be\3\2\2\2\30\u00c0\3\2\2\2\32\u00c9\3\2")
        buf.write("\2\2\34\u00cb\3\2\2\2\36\u00d2\3\2\2\2 \u00da\3\2\2\2")
        buf.write("\"\u00e4\3\2\2\2$\u00ee\3\2\2\2&\u00fd\3\2\2\2(\u0107")
        buf.write("\3\2\2\2*\u010b\3\2\2\2,\u010e\3\2\2\2.\u011c\3\2\2\2")
        buf.write("\60\u0126\3\2\2\2\62\u012e\3\2\2\2\64\u0131\3\2\2\2\66")
        buf.write("\u013f\3\2\2\28\u0141\3\2\2\2:\u014b\3\2\2\2<\u014d\3")
        buf.write("\2\2\2>\u014f\3\2\2\2@\u0151\3\2\2\2B\u0153\3\2\2\2D\u0155")
        buf.write("\3\2\2\2F\u0157\3\2\2\2H\u0159\3\2\2\2J\u015f\3\2\2\2")
        buf.write("L\u0161\3\2\2\2N\u016c\3\2\2\2P\u016e\3\2\2\2R\u0185\3")
        buf.write("\2\2\2T\u019c\3\2\2\2VX\5\4\3\2WV\3\2\2\2X[\3\2\2\2YW")
        buf.write("\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\2\2\3]\3")
        buf.write("\3\2\2\2^_\7\32\2\2_b\7>\2\2`a\7\63\2\2ac\7>\2\2b`\3\2")
        buf.write("\2\2bc\3\2\2\2cd\3\2\2\2de\5\6\4\2e\5\3\2\2\2fm\78\2\2")
        buf.write("gl\5\f\7\2hl\5\36\20\2il\5\b\5\2jl\5\n\6\2kg\3\2\2\2k")
        buf.write("h\3\2\2\2ki\3\2\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3")
        buf.write("\2\2\2np\3\2\2\2om\3\2\2\2pq\79\2\2q\7\3\2\2\2rs\7\35")
        buf.write("\2\2st\7\66\2\2tu\5 \21\2uv\7\67\2\2vw\5$\23\2w\t\3\2")
        buf.write("\2\2xy\7\36\2\2yz\7\66\2\2z{\5 \21\2{|\7\67\2\2|}\5$\23")
        buf.write("\2}\13\3\2\2\2~\u0081\5\20\t\2\177\u0081\5\16\b\2\u0080")
        buf.write("~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0083\7:\2\2\u0083\r\3\2\2\2\u0084\u0085\7\34\2\2\u0085")
        buf.write("\u008a\7?\2\2\u0086\u0087\7;\2\2\u0087\u0089\7?\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008a\3")
        buf.write("\2\2\2\u008d\u0090\7\63\2\2\u008e\u0091\5\26\f\2\u008f")
        buf.write("\u0091\5\34\17\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2")
        buf.write("\2\u0091\u0094\3\2\2\2\u0092\u0093\7/\2\2\u0093\u0095")
        buf.write("\5\22\n\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\17\3\2\2\2\u0096\u0097\7\33\2\2\u0097\u009c\7>\2\2\u0098")
        buf.write("\u0099\7;\2\2\u0099\u009b\7>\2\2\u009a\u0098\3\2\2\2\u009b")
        buf.write("\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a2\7")
        buf.write("\63\2\2\u00a0\u00a3\5\26\f\2\u00a1\u00a3\5\34\17\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2")
        buf.write("\u00a4\u00a5\7/\2\2\u00a5\u00a7\5\22\n\2\u00a6\u00a4\3")
        buf.write("\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\21\3\2\2\2\u00a8\u00ad")
        buf.write("\5\24\13\2\u00a9\u00aa\7;\2\2\u00aa\u00ac\5\24\13\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\23\3\2\2\2\u00af\u00ad\3\2")
        buf.write("\2\2\u00b0\u00b6\5\66\34\2\u00b1\u00b2\5\32\16\2\u00b2")
        buf.write("\u00b3\5\66\34\2\u00b3\u00b5\3\2\2\2\u00b4\u00b1\3\2\2")
        buf.write("\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\25\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bf")
        buf.write("\7\23\2\2\u00ba\u00bf\7\25\2\2\u00bb\u00bf\7\27\2\2\u00bc")
        buf.write("\u00bf\7\26\2\2\u00bd\u00bf\5\30\r\2\u00be\u00b9\3\2\2")
        buf.write("\2\u00be\u00ba\3\2\2\2\u00be\u00bb\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\27\3\2\2\2\u00c0\u00c1")
        buf.write("\7\37\2\2\u00c1\u00c2\7>\2\2\u00c2\u00c3\7\66\2\2\u00c3")
        buf.write("\u00c4\7\67\2\2\u00c4\31\3\2\2\2\u00c5\u00ca\5<\37\2\u00c6")
        buf.write("\u00ca\5:\36\2\u00c7\u00ca\5> \2\u00c8\u00ca\5@!\2\u00c9")
        buf.write("\u00c5\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00c8\3\2\2\2\u00ca\33\3\2\2\2\u00cb\u00cc\7\22")
        buf.write("\2\2\u00cc\u00cd\7<\2\2\u00cd\u00ce\5\26\f\2\u00ce\u00cf")
        buf.write("\7;\2\2\u00cf\u00d0\7\6\2\2\u00d0\u00d1\7=\2\2\u00d1\35")
        buf.write("\3\2\2\2\u00d2\u00d3\t\2\2\2\u00d3\u00d5\7\66\2\2\u00d4")
        buf.write("\u00d6\5 \21\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7\67\2\2\u00d8\u00d9")
        buf.write("\5$\23\2\u00d9\37\3\2\2\2\u00da\u00df\5\"\22\2\u00db\u00dc")
        buf.write("\7:\2\2\u00dc\u00de\5\"\22\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0!\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e5\5\26\f")
        buf.write("\2\u00e3\u00e5\5\34\17\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00eb\7>\2\2\u00e7")
        buf.write("\u00e8\7;\2\2\u00e8\u00ea\7>\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec#\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f6\78\2\2")
        buf.write("\u00ef\u00f5\5\f\7\2\u00f0\u00f5\5(\25\2\u00f1\u00f5\5")
        buf.write("*\26\2\u00f2\u00f5\5.\30\2\u00f3\u00f5\5,\27\2\u00f4\u00ef")
        buf.write("\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3")
        buf.write("\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\79\2\2\u00fa%\3")
        buf.write("\2\2\2\u00fb\u00fe\7>\2\2\u00fc\u00fe\58\35\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\7/\2\2\u0100\u0101\5\24\13\2\u0101\'\3\2\2\2\u0102")
        buf.write("\u0108\5&\24\2\u0103\u0108\5*\26\2\u0104\u0108\5N(\2\u0105")
        buf.write("\u0108\7\f\2\2\u0106\u0108\7\r\2\2\u0107\u0102\3\2\2\2")
        buf.write("\u0107\u0103\3\2\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3")
        buf.write("\2\2\2\u0107\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write("\7:\2\2\u010a)\3\2\2\2\u010b\u010c\7\30\2\2\u010c\u010d")
        buf.write("\5\24\13\2\u010d+\3\2\2\2\u010e\u010f\7\21\2\2\u010f\u0110")
        buf.write("\7\66\2\2\u0110\u0111\7>\2\2\u0111\u0112\7\24\2\2\u0112")
        buf.write("\u0113\7\6\2\2\u0113\u0114\7\64\2\2\u0114\u0117\7\6\2")
        buf.write("\2\u0115\u0116\7 \2\2\u0116\u0118\7\6\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\7\67\2\2\u011a\u011b\5$\23\2\u011b-\3\2\2\2\u011c")
        buf.write("\u0120\5\60\31\2\u011d\u011f\5\64\33\2\u011e\u011d\3\2")
        buf.write("\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121")
        buf.write("\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0125\5\62\32\2\u0124\u0123\3\2\2\2\u0124\u0125\3\2\2")
        buf.write("\2\u0125/\3\2\2\2\u0126\u0127\7\16\2\2\u0127\u0129\7\66")
        buf.write("\2\2\u0128\u012a\5L\'\2\u0129\u0128\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7\67\2\2\u012c")
        buf.write("\u012d\5$\23\2\u012d\61\3\2\2\2\u012e\u012f\7\20\2\2\u012f")
        buf.write("\u0130\5$\23\2\u0130\63\3\2\2\2\u0131\u0132\7\17\2\2\u0132")
        buf.write("\u0134\7\66\2\2\u0133\u0135\5L\'\2\u0134\u0133\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137\7")
        buf.write("\67\2\2\u0137\u0138\5$\23\2\u0138\65\3\2\2\2\u0139\u0140")
        buf.write("\7\3\2\2\u013a\u0140\7\6\2\2\u013b\u0140\7\4\2\2\u013c")
        buf.write("\u0140\7\5\2\2\u013d\u0140\5N(\2\u013e\u0140\7>\2\2\u013f")
        buf.write("\u0139\3\2\2\2\u013f\u013a\3\2\2\2\u013f\u013b\3\2\2\2")
        buf.write("\u013f\u013c\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3")
        buf.write("\2\2\2\u0140\67\3\2\2\2\u0141\u0142\7\22\2\2\u0142\u0143")
        buf.write("\7<\2\2\u0143\u0144\t\3\2\2\u0144\u0145\7=\2\2\u01459")
        buf.write("\3\2\2\2\u0146\u014c\7+\2\2\u0147\u0148\7,\2\2\u0148\u014c")
        buf.write("\7-\2\2\u0149\u014c\7.\2\2\u014a\u014c\7*\2\2\u014b\u0146")
        buf.write("\3\2\2\2\u014b\u0147\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014a\3\2\2\2\u014c;\3\2\2\2\u014d\u014e\t\4\2\2\u014e")
        buf.write("=\3\2\2\2\u014f\u0150\t\5\2\2\u0150?\3\2\2\2\u0151\u0152")
        buf.write("\t\6\2\2\u0152A\3\2\2\2\u0153\u0154\t\7\2\2\u0154C\3\2")
        buf.write("\2\2\u0155\u0156\t\b\2\2\u0156E\3\2\2\2\u0157\u0158\7")
        buf.write("$\2\2\u0158G\3\2\2\2\u0159\u015a\t\t\2\2\u015aI\3\2\2")
        buf.write("\2\u015b\u0160\5H%\2\u015c\u0160\5F$\2\u015d\u0160\5D")
        buf.write("#\2\u015e\u0160\5B\"\2\u015f\u015b\3\2\2\2\u015f\u015c")
        buf.write("\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("K\3\2\2\2\u0161\u0167\5\66\34\2\u0162\u0163\5J&\2\u0163")
        buf.write("\u0164\5\66\34\2\u0164\u0166\3\2\2\2\u0165\u0162\3\2\2")
        buf.write("\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168M\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016d")
        buf.write("\5P)\2\u016b\u016d\5R*\2\u016c\u016a\3\2\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016dO\3\2\2\2\u016e\u016f\7>\2\2\u016f\u0170")
        buf.write("\7\65\2\2\u0170\u0183\7>\2\2\u0171\u0180\7\66\2\2\u0172")
        buf.write("\u0175\5\66\34\2\u0173\u0175\7>\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0174\u0173\3\2\2\2\u0175\u017d\3\2\2\2\u0176\u0179")
        buf.write("\7;\2\2\u0177\u017a\5\66\34\2\u0178\u017a\7>\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017c\3\2\2\2")
        buf.write("\u017b\u0176\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0174\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0182\3\2\2\2\u0182\u0184\7\67\2\2\u0183\u0171\3\2\2")
        buf.write("\2\u0183\u0184\3\2\2\2\u0184Q\3\2\2\2\u0185\u0186\7>\2")
        buf.write("\2\u0186\u0187\7\62\2\2\u0187\u019a\7?\2\2\u0188\u0197")
        buf.write("\7\66\2\2\u0189\u018c\5\66\34\2\u018a\u018c\7>\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018a\3\2\2\2\u018c\u0194\3\2\2\2")
        buf.write("\u018d\u0190\7;\2\2\u018e\u0191\5\66\34\2\u018f\u0191")
        buf.write("\7>\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0193\3\2\2\2\u0192\u018d\3\2\2\2\u0193\u0196\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0198\3")
        buf.write("\2\2\2\u0196\u0194\3\2\2\2\u0197\u018b\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\7\67\2\2\u019a")
        buf.write("\u0188\3\2\2\2\u019a\u019b\3\2\2\2\u019bS\3\2\2\2\u019c")
        buf.write("\u019d\7\22\2\2\u019d\u01a1\7\66\2\2\u019e\u01a0\13\2")
        buf.write("\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\7\67\2\2\u01a5U\3\2\2\2.Yb")
        buf.write("km\u0080\u008a\u0090\u0094\u009c\u00a2\u00a6\u00ad\u00b6")
        buf.write("\u00be\u00c9\u00d5\u00df\u00e4\u00eb\u00f4\u00f6\u00fd")
        buf.write("\u0107\u0117\u0120\u0124\u0129\u0134\u013f\u014b\u015f")
        buf.write("\u0167\u016c\u0174\u0179\u017d\u0180\u0183\u018b\u0190")
        buf.write("\u0194\u0197\u019a\u01a1")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'Array'", 
                     "'Int'", "'In'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'NULL'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'>='", 
                     "'<='", "'==.'", "'+.'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!='", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'>'", "'<'", "'::'", "':'", "'..'", "'.'", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "Float", "String", "Boolean", "Integer", 
                      "Poinfloat", "Exponentfloat", "BinaryConstant", "HexadecimalConstant", 
                      "OctalConstant", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "ARRAYTYPE", "INT", "IN", "FLOATTYPE", 
                      "BOOLEANTYPE", "STRINGTYPE", "RETURN", "NULL", "CLASS", 
                      "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                      "BY", "GREQUAL", "LESEQUAL", "DOUEQUALDOT", "ADDDOT", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "NOTEQUAL", "NOT", 
                      "DOUAND", "DOUOR", "DOUEQUAL", "EQUAL", "GREATER", 
                      "LESS", "COLON", "SINGCOLON", "DOTDOT", "DOT", "LB", 
                      "RB", "LP", "RP", "SEMI", "COMMA", "LBR", "RBR", "IDENT", 
                      "DOLLAR", "COMMENT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_classUse = 1
    RULE_bodyclass = 2
    RULE_constructor = 3
    RULE_destructor = 4
    RULE_attribute = 5
    RULE_var = 6
    RULE_val = 7
    RULE_calculators = 8
    RULE_calculator = 9
    RULE_typeNumber = 10
    RULE_classType = 11
    RULE_math = 12
    RULE_arrayType = 13
    RULE_methodClass = 14
    RULE_listParams = 15
    RULE_param = 16
    RULE_blockStatement = 17
    RULE_calculsingle = 18
    RULE_statement = 19
    RULE_returnself = 20
    RULE_foreach = 21
    RULE_ifElse = 22
    RULE_if1 = 23
    RULE_else1 = 24
    RULE_elseIf = 25
    RULE_number = 26
    RULE_arrayIndex = 27
    RULE_booleanType = 28
    RULE_integerType = 29
    RULE_floatType = 30
    RULE_stringType = 31
    RULE_arithmeticOperators = 32
    RULE_booleanOperators = 33
    RULE_stringOperators = 34
    RULE_relationalOperators = 35
    RULE_operators = 36
    RULE_expressions = 37
    RULE_attributecall = 38
    RULE_instanceAttribute = 39
    RULE_staticAttribute = 40
    RULE_array = 41

    ruleNames =  [ "program", "classUse", "bodyclass", "constructor", "destructor", 
                   "attribute", "var", "val", "calculators", "calculator", 
                   "typeNumber", "classType", "math", "arrayType", "methodClass", 
                   "listParams", "param", "blockStatement", "calculsingle", 
                   "statement", "returnself", "foreach", "ifElse", "if1", 
                   "else1", "elseIf", "number", "arrayIndex", "booleanType", 
                   "integerType", "floatType", "stringType", "arithmeticOperators", 
                   "booleanOperators", "stringOperators", "relationalOperators", 
                   "operators", "expressions", "attributecall", "instanceAttribute", 
                   "staticAttribute", "array" ]

    EOF = Token.EOF
    Float=1
    String=2
    Boolean=3
    Integer=4
    Poinfloat=5
    Exponentfloat=6
    BinaryConstant=7
    HexadecimalConstant=8
    OctalConstant=9
    BREAK=10
    CONTINUE=11
    IF=12
    ELSEIF=13
    ELSE=14
    FOREACH=15
    ARRAYTYPE=16
    INT=17
    IN=18
    FLOATTYPE=19
    BOOLEANTYPE=20
    STRINGTYPE=21
    RETURN=22
    NULL=23
    CLASS=24
    VAL=25
    VAR=26
    CONSTRUCTOR=27
    DESTRUCTOR=28
    NEW=29
    BY=30
    GREQUAL=31
    LESEQUAL=32
    DOUEQUALDOT=33
    ADDDOT=34
    ADD=35
    SUB=36
    MUL=37
    DIV=38
    MOD=39
    NOTEQUAL=40
    NOT=41
    DOUAND=42
    DOUOR=43
    DOUEQUAL=44
    EQUAL=45
    GREATER=46
    LESS=47
    COLON=48
    SINGCOLON=49
    DOTDOT=50
    DOT=51
    LB=52
    RB=53
    LP=54
    RP=55
    SEMI=56
    COMMA=57
    LBR=58
    RBR=59
    IDENT=60
    DOLLAR=61
    COMMENT=62
    WS=63
    ERROR_CHAR=64
    ILLEGAL_ESCAPE=65
    UNCLOSE_STRING=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classUse(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassUseContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassUseContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS:
                self.state = 84
                self.classUse()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassUseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENT)
            else:
                return self.getToken(D96Parser.IDENT, i)

        def bodyclass(self):
            return self.getTypedRuleContext(D96Parser.BodyclassContext,0)


        def SINGCOLON(self):
            return self.getToken(D96Parser.SINGCOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classUse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassUse" ):
                return visitor.visitClassUse(self)
            else:
                return visitor.visitChildren(self)




    def classUse(self):

        localctx = D96Parser.ClassUseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classUse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(D96Parser.CLASS)
            self.state = 93
            self.match(D96Parser.IDENT)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.SINGCOLON:
                self.state = 94
                self.match(D96Parser.SINGCOLON)
                self.state = 95
                self.match(D96Parser.IDENT)


            self.state = 98
            self.bodyclass()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.AttributeContext)
            else:
                return self.getTypedRuleContext(D96Parser.AttributeContext,i)


        def methodClass(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MethodClassContext)
            else:
                return self.getTypedRuleContext(D96Parser.MethodClassContext,i)


        def constructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ConstructorContext)
            else:
                return self.getTypedRuleContext(D96Parser.ConstructorContext,i)


        def destructor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.DestructorContext)
            else:
                return self.getTypedRuleContext(D96Parser.DestructorContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_bodyclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodyclass" ):
                return visitor.visitBodyclass(self)
            else:
                return visitor.visitChildren(self)




    def bodyclass(self):

        localctx = D96Parser.BodyclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bodyclass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(D96Parser.LP)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.IDENT) | (1 << D96Parser.DOLLAR))) != 0):
                self.state = 105
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.VAL, D96Parser.VAR]:
                    self.state = 101
                    self.attribute()
                    pass
                elif token in [D96Parser.IDENT, D96Parser.DOLLAR]:
                    self.state = 102
                    self.methodClass()
                    pass
                elif token in [D96Parser.CONSTRUCTOR]:
                    self.state = 103
                    self.constructor()
                    pass
                elif token in [D96Parser.DESTRUCTOR]:
                    self.state = 104
                    self.destructor()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listParams(self):
            return self.getTypedRuleContext(D96Parser.ListParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 113
            self.match(D96Parser.LB)
            self.state = 114
            self.listParams()
            self.state = 115
            self.match(D96Parser.RB)
            self.state = 116
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listParams(self):
            return self.getTypedRuleContext(D96Parser.ListParamsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(D96Parser.DESTRUCTOR)
            self.state = 119
            self.match(D96Parser.LB)
            self.state = 120
            self.listParams()
            self.state = 121
            self.match(D96Parser.RB)
            self.state = 122
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def val(self):
            return self.getTypedRuleContext(D96Parser.ValContext,0)


        def var(self):
            return self.getTypedRuleContext(D96Parser.VarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL]:
                self.state = 124
                self.val()
                pass
            elif token in [D96Parser.VAR]:
                self.state = 125
                self.var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def DOLLAR(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR)
            else:
                return self.getToken(D96Parser.DOLLAR, i)

        def SINGCOLON(self):
            return self.getToken(D96Parser.SINGCOLON, 0)

        def typeNumber(self):
            return self.getTypedRuleContext(D96Parser.TypeNumberContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def calculators(self):
            return self.getTypedRuleContext(D96Parser.CalculatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = D96Parser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(D96Parser.VAR)
            self.state = 131
            self.match(D96Parser.DOLLAR)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 132
                self.match(D96Parser.COMMA)
                self.state = 133
                self.match(D96Parser.DOLLAR)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(D96Parser.SINGCOLON)
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOATTYPE, D96Parser.BOOLEANTYPE, D96Parser.STRINGTYPE, D96Parser.NEW]:
                self.state = 140
                self.typeNumber()
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.state = 141
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.EQUAL:
                self.state = 144
                self.match(D96Parser.EQUAL)
                self.state = 145
                self.calculators()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENT)
            else:
                return self.getToken(D96Parser.IDENT, i)

        def SINGCOLON(self):
            return self.getToken(D96Parser.SINGCOLON, 0)

        def typeNumber(self):
            return self.getTypedRuleContext(D96Parser.TypeNumberContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def calculators(self):
            return self.getTypedRuleContext(D96Parser.CalculatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal" ):
                return visitor.visitVal(self)
            else:
                return visitor.visitChildren(self)




    def val(self):

        localctx = D96Parser.ValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(D96Parser.VAL)
            self.state = 149
            self.match(D96Parser.IDENT)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 150
                self.match(D96Parser.COMMA)
                self.state = 151
                self.match(D96Parser.IDENT)
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(D96Parser.SINGCOLON)
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOATTYPE, D96Parser.BOOLEANTYPE, D96Parser.STRINGTYPE, D96Parser.NEW]:
                self.state = 158
                self.typeNumber()
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.state = 159
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.EQUAL:
                self.state = 162
                self.match(D96Parser.EQUAL)
                self.state = 163
                self.calculators()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalculatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def calculator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.CalculatorContext)
            else:
                return self.getTypedRuleContext(D96Parser.CalculatorContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_calculators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculators" ):
                return visitor.visitCalculators(self)
            else:
                return visitor.visitChildren(self)




    def calculators(self):

        localctx = D96Parser.CalculatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_calculators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.calculator()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 167
                self.match(D96Parser.COMMA)
                self.state = 168
                self.calculator()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalculatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.NumberContext)
            else:
                return self.getTypedRuleContext(D96Parser.NumberContext,i)


        def math(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.MathContext)
            else:
                return self.getTypedRuleContext(D96Parser.MathContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_calculator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculator" ):
                return visitor.visitCalculator(self)
            else:
                return visitor.visitChildren(self)




    def calculator(self):

        localctx = D96Parser.CalculatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_calculator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.number()
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREQUAL) | (1 << D96Parser.LESEQUAL) | (1 << D96Parser.DOUEQUALDOT) | (1 << D96Parser.ADDDOT) | (1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.NOT) | (1 << D96Parser.DOUAND) | (1 << D96Parser.DOUEQUAL) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESS))) != 0):
                self.state = 175
                self.math()
                self.state = 176
                self.number()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOATTYPE(self):
            return self.getToken(D96Parser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(D96Parser.STRINGTYPE, 0)

        def BOOLEANTYPE(self):
            return self.getToken(D96Parser.BOOLEANTYPE, 0)

        def classType(self):
            return self.getTypedRuleContext(D96Parser.ClassTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typeNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeNumber" ):
                return visitor.visitTypeNumber(self)
            else:
                return visitor.visitChildren(self)




    def typeNumber(self):

        localctx = D96Parser.TypeNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeNumber)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(D96Parser.FLOATTYPE)
                pass
            elif token in [D96Parser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(D96Parser.STRINGTYPE)
                pass
            elif token in [D96Parser.BOOLEANTYPE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(D96Parser.BOOLEANTYPE)
                pass
            elif token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.classType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_classType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassType" ):
                return visitor.visitClassType(self)
            else:
                return visitor.visitChildren(self)




    def classType(self):

        localctx = D96Parser.ClassTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.NEW)
            self.state = 191
            self.match(D96Parser.IDENT)
            self.state = 192
            self.match(D96Parser.LB)
            self.state = 193
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerType(self):
            return self.getTypedRuleContext(D96Parser.IntegerTypeContext,0)


        def booleanType(self):
            return self.getTypedRuleContext(D96Parser.BooleanTypeContext,0)


        def floatType(self):
            return self.getTypedRuleContext(D96Parser.FloatTypeContext,0)


        def stringType(self):
            return self.getTypedRuleContext(D96Parser.StringTypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_math

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = D96Parser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_math)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.integerType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.booleanType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.floatType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.stringType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LBR(self):
            return self.getToken(D96Parser.LBR, 0)

        def typeNumber(self):
            return self.getTypedRuleContext(D96Parser.TypeNumberContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def Integer(self):
            return self.getToken(D96Parser.Integer, 0)

        def RBR(self):
            return self.getToken(D96Parser.RBR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = D96Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(D96Parser.ARRAYTYPE)
            self.state = 202
            self.match(D96Parser.LBR)
            self.state = 203
            self.typeNumber()
            self.state = 204
            self.match(D96Parser.COMMA)
            self.state = 205
            self.match(D96Parser.Integer)
            self.state = 206
            self.match(D96Parser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def DOLLAR(self):
            return self.getToken(D96Parser.DOLLAR, 0)

        def listParams(self):
            return self.getTypedRuleContext(D96Parser.ListParamsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodClass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodClass" ):
                return visitor.visitMethodClass(self)
            else:
                return visitor.visitChildren(self)




    def methodClass(self):

        localctx = D96Parser.MethodClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methodClass)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==D96Parser.IDENT or _la==D96Parser.DOLLAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 209
            self.match(D96Parser.LB)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.INT) | (1 << D96Parser.FLOATTYPE) | (1 << D96Parser.BOOLEANTYPE) | (1 << D96Parser.STRINGTYPE) | (1 << D96Parser.NEW))) != 0):
                self.state = 210
                self.listParams()


            self.state = 213
            self.match(D96Parser.RB)
            self.state = 214
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParamContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParamContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_listParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




    def listParams(self):

        localctx = D96Parser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.param()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 217
                self.match(D96Parser.SEMI)
                self.state = 218
                self.param()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENT)
            else:
                return self.getToken(D96Parser.IDENT, i)

        def typeNumber(self):
            return self.getTypedRuleContext(D96Parser.TypeNumberContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(D96Parser.ArrayTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOATTYPE, D96Parser.BOOLEANTYPE, D96Parser.STRINGTYPE, D96Parser.NEW]:
                self.state = 224
                self.typeNumber()
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.state = 225
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 228
            self.match(D96Parser.IDENT)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 229
                self.match(D96Parser.COMMA)
                self.state = 230
                self.match(D96Parser.IDENT)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.AttributeContext)
            else:
                return self.getTypedRuleContext(D96Parser.AttributeContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def returnself(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ReturnselfContext)
            else:
                return self.getTypedRuleContext(D96Parser.ReturnselfContext,i)


        def ifElse(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IfElseContext)
            else:
                return self.getTypedRuleContext(D96Parser.IfElseContext,i)


        def foreach(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ForeachContext)
            else:
                return self.getTypedRuleContext(D96Parser.ForeachContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_blockStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = D96Parser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(D96Parser.LP)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAYTYPE) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.IDENT))) != 0):
                self.state = 242
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 237
                    self.attribute()
                    pass

                elif la_ == 2:
                    self.state = 238
                    self.statement()
                    pass

                elif la_ == 3:
                    self.state = 239
                    self.returnself()
                    pass

                elif la_ == 4:
                    self.state = 240
                    self.ifElse()
                    pass

                elif la_ == 5:
                    self.state = 241
                    self.foreach()
                    pass


                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalculsingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def calculator(self):
            return self.getTypedRuleContext(D96Parser.CalculatorContext,0)


        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def arrayIndex(self):
            return self.getTypedRuleContext(D96Parser.ArrayIndexContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_calculsingle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculsingle" ):
                return visitor.visitCalculsingle(self)
            else:
                return visitor.visitChildren(self)




    def calculsingle(self):

        localctx = D96Parser.CalculsingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_calculsingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENT]:
                self.state = 249
                self.match(D96Parser.IDENT)
                pass
            elif token in [D96Parser.ARRAYTYPE]:
                self.state = 250
                self.arrayIndex()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 253
            self.match(D96Parser.EQUAL)
            self.state = 254
            self.calculator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def calculsingle(self):
            return self.getTypedRuleContext(D96Parser.CalculsingleContext,0)


        def returnself(self):
            return self.getTypedRuleContext(D96Parser.ReturnselfContext,0)


        def attributecall(self):
            return self.getTypedRuleContext(D96Parser.AttributecallContext,0)


        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 256
                self.calculsingle()
                pass

            elif la_ == 2:
                self.state = 257
                self.returnself()
                pass

            elif la_ == 3:
                self.state = 258
                self.attributecall()
                pass

            elif la_ == 4:
                self.state = 259
                self.match(D96Parser.BREAK)
                pass

            elif la_ == 5:
                self.state = 260
                self.match(D96Parser.CONTINUE)
                pass


            self.state = 263
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnselfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def calculator(self):
            return self.getTypedRuleContext(D96Parser.CalculatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnself

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnself" ):
                return visitor.visitReturnself(self)
            else:
                return visitor.visitChildren(self)




    def returnself(self):

        localctx = D96Parser.ReturnselfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnself)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(D96Parser.RETURN)
            self.state = 266
            self.calculator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForeachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.Integer)
            else:
                return self.getToken(D96Parser.Integer, i)

        def DOTDOT(self):
            return self.getToken(D96Parser.DOTDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_foreach

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach" ):
                return visitor.visitForeach(self)
            else:
                return visitor.visitChildren(self)




    def foreach(self):

        localctx = D96Parser.ForeachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_foreach)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(D96Parser.FOREACH)
            self.state = 269
            self.match(D96Parser.LB)
            self.state = 270
            self.match(D96Parser.IDENT)
            self.state = 271
            self.match(D96Parser.IN)
            self.state = 272
            self.match(D96Parser.Integer)
            self.state = 273
            self.match(D96Parser.DOTDOT)
            self.state = 274
            self.match(D96Parser.Integer)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 275
                self.match(D96Parser.BY)
                self.state = 276
                self.match(D96Parser.Integer)


            self.state = 279
            self.match(D96Parser.RB)
            self.state = 280
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if1(self):
            return self.getTypedRuleContext(D96Parser.If1Context,0)


        def elseIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ElseIfContext)
            else:
                return self.getTypedRuleContext(D96Parser.ElseIfContext,i)


        def else1(self):
            return self.getTypedRuleContext(D96Parser.Else1Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifElse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)




    def ifElse(self):

        localctx = D96Parser.IfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ifElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.if1()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 283
                self.elseIf()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 289
                self.else1()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def expressions(self):
            return self.getTypedRuleContext(D96Parser.ExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf1" ):
                return visitor.visitIf1(self)
            else:
                return visitor.visitChildren(self)




    def if1(self):

        localctx = D96Parser.If1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.IF)
            self.state = 293
            self.match(D96Parser.LB)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Float) | (1 << D96Parser.String) | (1 << D96Parser.Boolean) | (1 << D96Parser.Integer) | (1 << D96Parser.IDENT))) != 0):
                self.state = 294
                self.expressions()


            self.state = 297
            self.match(D96Parser.RB)
            self.state = 298
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse1" ):
                return visitor.visitElse1(self)
            else:
                return visitor.visitChildren(self)




    def else1(self):

        localctx = D96Parser.Else1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(D96Parser.ELSE)
            self.state = 301
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(D96Parser.BlockStatementContext,0)


        def expressions(self):
            return self.getTypedRuleContext(D96Parser.ExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseIf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIf" ):
                return visitor.visitElseIf(self)
            else:
                return visitor.visitChildren(self)




    def elseIf(self):

        localctx = D96Parser.ElseIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseIf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(D96Parser.ELSEIF)
            self.state = 304
            self.match(D96Parser.LB)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Float) | (1 << D96Parser.String) | (1 << D96Parser.Boolean) | (1 << D96Parser.Integer) | (1 << D96Parser.IDENT))) != 0):
                self.state = 305
                self.expressions()


            self.state = 308
            self.match(D96Parser.RB)
            self.state = 309
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(D96Parser.Float, 0)

        def Integer(self):
            return self.getToken(D96Parser.Integer, 0)

        def String(self):
            return self.getToken(D96Parser.String, 0)

        def Boolean(self):
            return self.getToken(D96Parser.Boolean, 0)

        def attributecall(self):
            return self.getTypedRuleContext(D96Parser.AttributecallContext,0)


        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = D96Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_number)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(D96Parser.Float)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(D96Parser.Integer)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 313
                self.match(D96Parser.String)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.match(D96Parser.Boolean)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 315
                self.attributecall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 316
                self.match(D96Parser.IDENT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayIndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LBR(self):
            return self.getToken(D96Parser.LBR, 0)

        def RBR(self):
            return self.getToken(D96Parser.RBR, 0)

        def Integer(self):
            return self.getToken(D96Parser.Integer, 0)

        def IDENT(self):
            return self.getToken(D96Parser.IDENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrayIndex

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayIndex" ):
                return visitor.visitArrayIndex(self)
            else:
                return visitor.visitChildren(self)




    def arrayIndex(self):

        localctx = D96Parser.ArrayIndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arrayIndex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.ARRAYTYPE)
            self.state = 320
            self.match(D96Parser.LBR)
            self.state = 321
            _la = self._input.LA(1)
            if not(_la==D96Parser.Integer or _la==D96Parser.IDENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 322
            self.match(D96Parser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def DOUAND(self):
            return self.getToken(D96Parser.DOUAND, 0)

        def DOUOR(self):
            return self.getToken(D96Parser.DOUOR, 0)

        def DOUEQUAL(self):
            return self.getToken(D96Parser.DOUEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_booleanType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanType" ):
                return visitor.visitBooleanType(self)
            else:
                return visitor.visitChildren(self)




    def booleanType(self):

        localctx = D96Parser.BooleanTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_booleanType)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.match(D96Parser.NOT)
                pass
            elif token in [D96Parser.DOUAND]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(D96Parser.DOUAND)
                self.state = 326
                self.match(D96Parser.DOUOR)
                pass
            elif token in [D96Parser.DOUEQUAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(D96Parser.DOUEQUAL)
                pass
            elif token in [D96Parser.NOTEQUAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.match(D96Parser.NOTEQUAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def DOUEQUAL(self):
            return self.getToken(D96Parser.DOUEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def GREQUAL(self):
            return self.getToken(D96Parser.GREQUAL, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def LESEQUAL(self):
            return self.getToken(D96Parser.LESEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_integerType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerType" ):
                return visitor.visitIntegerType(self)
            else:
                return visitor.visitChildren(self)




    def integerType(self):

        localctx = D96Parser.IntegerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_integerType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREQUAL) | (1 << D96Parser.LESEQUAL) | (1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.DOUEQUAL) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def GREQUAL(self):
            return self.getToken(D96Parser.GREQUAL, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def LESEQUAL(self):
            return self.getToken(D96Parser.LESEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_floatType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)




    def floatType(self):

        localctx = D96Parser.FloatTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_floatType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREQUAL) | (1 << D96Parser.LESEQUAL) | (1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDDOT(self):
            return self.getToken(D96Parser.ADDDOT, 0)

        def DOUEQUALDOT(self):
            return self.getToken(D96Parser.DOUEQUALDOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stringType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)




    def stringType(self):

        localctx = D96Parser.StringTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stringType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not(_la==D96Parser.DOUEQUALDOT or _la==D96Parser.ADDDOT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arithmeticOperators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticOperators" ):
                return visitor.visitArithmeticOperators(self)
            else:
                return visitor.visitChildren(self)




    def arithmeticOperators(self):

        localctx = D96Parser.ArithmeticOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arithmeticOperators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def DOUAND(self):
            return self.getToken(D96Parser.DOUAND, 0)

        def DOUOR(self):
            return self.getToken(D96Parser.DOUOR, 0)

        def DOUEQUALDOT(self):
            return self.getToken(D96Parser.DOUEQUALDOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_booleanOperators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanOperators" ):
                return visitor.visitBooleanOperators(self)
            else:
                return visitor.visitChildren(self)




    def booleanOperators(self):

        localctx = D96Parser.BooleanOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_booleanOperators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.DOUEQUALDOT) | (1 << D96Parser.NOT) | (1 << D96Parser.DOUAND) | (1 << D96Parser.DOUOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDDOT(self):
            return self.getToken(D96Parser.ADDDOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stringOperators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringOperators" ):
                return visitor.visitStringOperators(self)
            else:
                return visitor.visitChildren(self)




    def stringOperators(self):

        localctx = D96Parser.StringOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stringOperators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(D96Parser.ADDDOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUAND(self):
            return self.getToken(D96Parser.DOUAND, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def GREQUAL(self):
            return self.getToken(D96Parser.GREQUAL, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def LESEQUAL(self):
            return self.getToken(D96Parser.LESEQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_relationalOperators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalOperators" ):
                return visitor.visitRelationalOperators(self)
            else:
                return visitor.visitChildren(self)




    def relationalOperators(self):

        localctx = D96Parser.RelationalOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relationalOperators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREQUAL) | (1 << D96Parser.LESEQUAL) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.DOUAND) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalOperators(self):
            return self.getTypedRuleContext(D96Parser.RelationalOperatorsContext,0)


        def stringOperators(self):
            return self.getTypedRuleContext(D96Parser.StringOperatorsContext,0)


        def booleanOperators(self):
            return self.getTypedRuleContext(D96Parser.BooleanOperatorsContext,0)


        def arithmeticOperators(self):
            return self.getTypedRuleContext(D96Parser.ArithmeticOperatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = D96Parser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 345
                self.relationalOperators()
                pass

            elif la_ == 2:
                self.state = 346
                self.stringOperators()
                pass

            elif la_ == 3:
                self.state = 347
                self.booleanOperators()
                pass

            elif la_ == 4:
                self.state = 348
                self.arithmeticOperators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.NumberContext)
            else:
                return self.getTypedRuleContext(D96Parser.NumberContext,i)


        def operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.OperatorsContext)
            else:
                return self.getTypedRuleContext(D96Parser.OperatorsContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_expressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = D96Parser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.number()
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GREQUAL) | (1 << D96Parser.LESEQUAL) | (1 << D96Parser.DOUEQUALDOT) | (1 << D96Parser.ADDDOT) | (1 << D96Parser.ADD) | (1 << D96Parser.SUB) | (1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.NOT) | (1 << D96Parser.DOUAND) | (1 << D96Parser.DOUOR) | (1 << D96Parser.GREATER) | (1 << D96Parser.LESS))) != 0):
                self.state = 352
                self.operators()
                self.state = 353
                self.number()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributecallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceAttribute(self):
            return self.getTypedRuleContext(D96Parser.InstanceAttributeContext,0)


        def staticAttribute(self):
            return self.getTypedRuleContext(D96Parser.StaticAttributeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attributecall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributecall" ):
                return visitor.visitAttributecall(self)
            else:
                return visitor.visitChildren(self)




    def attributecall(self):

        localctx = D96Parser.AttributecallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_attributecall)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.instanceAttribute()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.staticAttribute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENT)
            else:
                return self.getToken(D96Parser.IDENT, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.NumberContext)
            else:
                return self.getTypedRuleContext(D96Parser.NumberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_instanceAttribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceAttribute" ):
                return visitor.visitInstanceAttribute(self)
            else:
                return visitor.visitChildren(self)




    def instanceAttribute(self):

        localctx = D96Parser.InstanceAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instanceAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(D96Parser.IDENT)
            self.state = 365
            self.match(D96Parser.DOT)
            self.state = 366
            self.match(D96Parser.IDENT)
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LB:
                self.state = 367
                self.match(D96Parser.LB)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Float) | (1 << D96Parser.String) | (1 << D96Parser.Boolean) | (1 << D96Parser.Integer) | (1 << D96Parser.IDENT))) != 0):
                    self.state = 370
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        self.state = 368
                        self.number()
                        pass

                    elif la_ == 2:
                        self.state = 369
                        self.match(D96Parser.IDENT)
                        pass


                    self.state = 379
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 372
                        self.match(D96Parser.COMMA)
                        self.state = 375
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                        if la_ == 1:
                            self.state = 373
                            self.number()
                            pass

                        elif la_ == 2:
                            self.state = 374
                            self.match(D96Parser.IDENT)
                            pass


                        self.state = 381
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 384
                self.match(D96Parser.RB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENT)
            else:
                return self.getToken(D96Parser.IDENT, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def DOLLAR(self):
            return self.getToken(D96Parser.DOLLAR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.NumberContext)
            else:
                return self.getTypedRuleContext(D96Parser.NumberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_staticAttribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticAttribute" ):
                return visitor.visitStaticAttribute(self)
            else:
                return visitor.visitChildren(self)




    def staticAttribute(self):

        localctx = D96Parser.StaticAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_staticAttribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(D96Parser.IDENT)
            self.state = 388
            self.match(D96Parser.COLON)
            self.state = 389
            self.match(D96Parser.DOLLAR)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.LB:
                self.state = 390
                self.match(D96Parser.LB)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.Float) | (1 << D96Parser.String) | (1 << D96Parser.Boolean) | (1 << D96Parser.Integer) | (1 << D96Parser.IDENT))) != 0):
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        self.state = 391
                        self.number()
                        pass

                    elif la_ == 2:
                        self.state = 392
                        self.match(D96Parser.IDENT)
                        pass


                    self.state = 402
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==D96Parser.COMMA:
                        self.state = 395
                        self.match(D96Parser.COMMA)
                        self.state = 398
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                        if la_ == 1:
                            self.state = 396
                            self.number()
                            pass

                        elif la_ == 2:
                            self.state = 397
                            self.match(D96Parser.IDENT)
                            pass


                        self.state = 404
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 407
                self.match(D96Parser.RB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYTYPE(self):
            return self.getToken(D96Parser.ARRAYTYPE, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = D96Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.ARRAYTYPE)
            self.state = 411
            self.match(D96Parser.LB)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 412
                    self.matchWildcard() 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

            self.state = 418
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





