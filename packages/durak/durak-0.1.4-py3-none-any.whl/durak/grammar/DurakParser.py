# Generated from DurakParser.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,55,322,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,5,2,65,8,2,10,2,12,2,
        68,9,2,1,2,1,2,1,2,1,2,3,2,74,8,2,1,2,1,2,1,2,5,2,79,8,2,10,2,12,
        2,82,9,2,1,2,1,2,1,2,1,2,3,2,88,8,2,1,2,5,2,91,8,2,10,2,12,2,94,
        9,2,1,2,3,2,97,8,2,1,3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,3,5,115,8,5,1,6,1,6,1,6,1,6,1,6,5,6,122,8,
        6,10,6,12,6,125,9,6,1,6,5,6,128,8,6,10,6,12,6,131,9,6,1,6,1,6,1,
        6,1,6,5,6,137,8,6,10,6,12,6,140,9,6,3,6,142,8,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,5,7,151,8,7,10,7,12,7,154,9,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,5,8,163,8,8,10,8,12,8,166,9,8,1,8,1,8,1,8,1,8,5,8,172,8,8,
        10,8,12,8,175,9,8,3,8,177,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,5,9,188,8,9,10,9,12,9,191,9,9,1,9,1,9,1,9,1,9,1,9,5,9,198,8,9,
        10,9,12,9,201,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,217,8,10,10,10,12,10,220,9,10,1,10,1,10,
        3,10,224,8,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,5,14,243,8,14,10,14,12,14,246,
        9,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,254,8,15,10,15,12,15,257,
        9,15,1,16,1,16,1,16,3,16,262,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        5,17,270,8,17,10,17,12,17,273,9,17,1,18,1,18,1,18,1,18,1,18,1,18,
        5,18,281,8,18,10,18,12,18,284,9,18,1,19,1,19,1,19,1,19,1,19,1,19,
        5,19,292,8,19,10,19,12,19,295,9,19,1,20,1,20,1,20,1,20,1,20,1,20,
        4,20,303,8,20,11,20,12,20,304,5,20,307,8,20,10,20,12,20,310,9,20,
        1,21,1,21,1,21,1,21,1,21,1,21,3,21,318,8,21,1,22,1,22,1,22,0,6,28,
        30,34,36,38,40,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,0,4,1,0,39,44,1,0,33,34,1,0,35,37,1,0,51,53,339,
        0,47,1,0,0,0,2,59,1,0,0,0,4,96,1,0,0,0,6,98,1,0,0,0,8,105,1,0,0,
        0,10,114,1,0,0,0,12,116,1,0,0,0,14,145,1,0,0,0,16,155,1,0,0,0,18,
        180,1,0,0,0,20,223,1,0,0,0,22,225,1,0,0,0,24,230,1,0,0,0,26,234,
        1,0,0,0,28,236,1,0,0,0,30,247,1,0,0,0,32,261,1,0,0,0,34,263,1,0,
        0,0,36,274,1,0,0,0,38,285,1,0,0,0,40,296,1,0,0,0,42,317,1,0,0,0,
        44,319,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,
        0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,52,5,0,0,1,52,1,1,0,0,0,53,
        60,5,2,0,0,54,60,3,4,2,0,55,60,3,10,5,0,56,60,3,24,12,0,57,60,5,
        1,0,0,58,60,5,7,0,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,
        56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,6,0,
        0,62,66,5,8,0,0,63,65,3,6,3,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,
        1,0,0,0,66,67,1,0,0,0,67,73,1,0,0,0,68,66,1,0,0,0,69,70,3,8,4,0,
        70,71,5,50,0,0,71,74,1,0,0,0,72,74,5,10,0,0,73,69,1,0,0,0,73,72,
        1,0,0,0,74,97,1,0,0,0,75,76,5,6,0,0,76,80,5,8,0,0,77,79,3,6,3,0,
        78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,87,1,
        0,0,0,82,80,1,0,0,0,83,84,3,8,4,0,84,85,5,49,0,0,85,88,1,0,0,0,86,
        88,5,9,0,0,87,83,1,0,0,0,87,86,1,0,0,0,88,92,1,0,0,0,89,91,3,2,1,
        0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,
        1,0,0,0,94,92,1,0,0,0,95,97,5,3,0,0,96,61,1,0,0,0,96,75,1,0,0,0,
        97,5,1,0,0,0,98,103,5,12,0,0,99,100,5,11,0,0,100,101,3,26,13,0,101,
        102,5,48,0,0,102,104,1,0,0,0,103,99,1,0,0,0,103,104,1,0,0,0,104,
        7,1,0,0,0,105,106,5,12,0,0,106,107,5,11,0,0,107,108,3,26,13,0,108,
        9,1,0,0,0,109,115,3,12,6,0,110,115,3,16,8,0,111,115,3,18,9,0,112,
        115,3,20,10,0,113,115,3,22,11,0,114,109,1,0,0,0,114,110,1,0,0,0,
        114,111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,115,11,1,0,0,0,116,
        117,5,4,0,0,117,118,5,14,0,0,118,119,3,26,13,0,119,123,5,49,0,0,
        120,122,3,2,1,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,
        123,124,1,0,0,0,124,129,1,0,0,0,125,123,1,0,0,0,126,128,3,14,7,0,
        127,126,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,
        130,141,1,0,0,0,131,129,1,0,0,0,132,133,5,4,0,0,133,134,5,16,0,0,
        134,138,5,23,0,0,135,137,3,2,1,0,136,135,1,0,0,0,137,140,1,0,0,0,
        138,136,1,0,0,0,138,139,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,
        141,132,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,5,3,0,0,
        144,13,1,0,0,0,145,146,5,4,0,0,146,147,5,15,0,0,147,148,3,26,13,
        0,148,152,5,49,0,0,149,151,3,2,1,0,150,149,1,0,0,0,151,154,1,0,0,
        0,152,150,1,0,0,0,152,153,1,0,0,0,153,15,1,0,0,0,154,152,1,0,0,0,
        155,156,5,4,0,0,156,157,5,17,0,0,157,158,5,27,0,0,158,159,5,18,0,
        0,159,160,3,26,13,0,160,164,5,49,0,0,161,163,3,2,1,0,162,161,1,0,
        0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,176,1,0,
        0,0,166,164,1,0,0,0,167,168,5,4,0,0,168,169,5,16,0,0,169,173,5,23,
        0,0,170,172,3,2,1,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,1,0,
        0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,176,167,1,0,
        0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,5,3,0,0,179,17,1,0,0,
        0,180,181,5,4,0,0,181,189,5,19,0,0,182,183,5,25,0,0,183,184,5,20,
        0,0,184,185,3,26,13,0,185,186,5,48,0,0,186,188,1,0,0,0,187,182,1,
        0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,
        0,0,0,191,189,1,0,0,0,192,193,5,25,0,0,193,194,5,20,0,0,194,195,
        3,26,13,0,195,199,5,49,0,0,196,198,3,2,1,0,197,196,1,0,0,0,198,201,
        1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,199,
        1,0,0,0,202,203,5,3,0,0,203,19,1,0,0,0,204,205,5,4,0,0,205,206,5,
        21,0,0,206,207,3,26,13,0,207,208,5,50,0,0,208,224,1,0,0,0,209,210,
        5,4,0,0,210,211,5,21,0,0,211,212,3,26,13,0,212,218,5,49,0,0,213,
        217,3,4,2,0,214,217,5,1,0,0,215,217,5,7,0,0,216,213,1,0,0,0,216,
        214,1,0,0,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,
        219,1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,222,5,3,0,0,222,
        224,1,0,0,0,223,204,1,0,0,0,223,209,1,0,0,0,224,21,1,0,0,0,225,226,
        5,4,0,0,226,227,5,22,0,0,227,228,5,29,0,0,228,229,5,24,0,0,229,23,
        1,0,0,0,230,231,5,5,0,0,231,232,3,26,13,0,232,233,5,50,0,0,233,25,
        1,0,0,0,234,235,3,28,14,0,235,27,1,0,0,0,236,237,6,14,-1,0,237,238,
        3,30,15,0,238,244,1,0,0,0,239,240,10,2,0,0,240,241,5,47,0,0,241,
        243,3,30,15,0,242,239,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
        245,1,0,0,0,245,29,1,0,0,0,246,244,1,0,0,0,247,248,6,15,-1,0,248,
        249,3,32,16,0,249,255,1,0,0,0,250,251,10,2,0,0,251,252,5,46,0,0,
        252,254,3,32,16,0,253,250,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,
        0,255,256,1,0,0,0,256,31,1,0,0,0,257,255,1,0,0,0,258,259,5,45,0,
        0,259,262,3,34,17,0,260,262,3,34,17,0,261,258,1,0,0,0,261,260,1,
        0,0,0,262,33,1,0,0,0,263,264,6,17,-1,0,264,265,3,36,18,0,265,271,
        1,0,0,0,266,267,10,2,0,0,267,268,7,0,0,0,268,270,3,36,18,0,269,266,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,35,1,
        0,0,0,273,271,1,0,0,0,274,275,6,18,-1,0,275,276,3,38,19,0,276,282,
        1,0,0,0,277,278,10,2,0,0,278,279,7,1,0,0,279,281,3,38,19,0,280,277,
        1,0,0,0,281,284,1,0,0,0,282,280,1,0,0,0,282,283,1,0,0,0,283,37,1,
        0,0,0,284,282,1,0,0,0,285,286,6,19,-1,0,286,287,3,40,20,0,287,293,
        1,0,0,0,288,289,10,2,0,0,289,290,7,2,0,0,290,292,3,40,20,0,291,288,
        1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,39,1,
        0,0,0,295,293,1,0,0,0,296,297,6,20,-1,0,297,298,3,42,21,0,298,308,
        1,0,0,0,299,302,10,2,0,0,300,301,5,38,0,0,301,303,5,55,0,0,302,300,
        1,0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,307,
        1,0,0,0,306,299,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,309,
        1,0,0,0,309,41,1,0,0,0,310,308,1,0,0,0,311,312,5,31,0,0,312,313,
        3,26,13,0,313,314,5,32,0,0,314,318,1,0,0,0,315,318,5,55,0,0,316,
        318,3,44,22,0,317,311,1,0,0,0,317,315,1,0,0,0,317,316,1,0,0,0,318,
        43,1,0,0,0,319,320,7,3,0,0,320,45,1,0,0,0,32,49,59,66,73,80,87,92,
        96,103,114,123,129,138,141,152,164,173,176,189,199,216,218,223,244,
        255,261,271,282,293,304,308,317
    ]

class DurakParser ( Parser ):

    grammarFileName = "DurakParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'</>'", "'<!'", 
                     "<INVALID>", "'<'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if'", "'elif'", "'else'", "'foreach'", "'in'", "'let'", 
                     "<INVALID>", "'include'", "'insert'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'mod'", "'.'", "'=='", 
                     "'!='", "'<<'", "'>>'", "'<='", "'>='", "'not'", "'and'", 
                     "'or'", "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "VERBATIM", "CLOSING_TAG", 
                      "DIRECTIVE_OPEN", "INJECTION_OPEN", "TAG_OPEN", "TEXT", 
                      "TAG_NAME", "TAG_END", "TAG_CLOSE", "TAG_EQ", "TAG_ATTRIBUTE_NAME", 
                      "TAG_WS", "DIRECTIVE_IF", "DIRECTIVE_ELIF", "DIRECTIVE_ELSE", 
                      "DIRECTIVE_FOREACH", "DIRECTIVE_IN", "DIRECTIVE_LET", 
                      "DIRECTIVE_EQ", "DIRECTIVE_INCLUDE", "DIRECTIVE_INSERT", 
                      "DIRECTIVE_END", "DIRECTIVE_CLOSE", "DIRECTIVE_IDENTIFIER", 
                      "DIRECTIVE_WS", "DIRECTIVE_FOREACH_IDENTIFIER", "DIRECTIVE_FOREACH_WS", 
                      "DIRECTIVE_INSERT_IDENTIFIER", "DIRECTIVE_INSERT_WS", 
                      "EXPR_LPAREN", "EXPR_RPAREN", "EXPR_PLUS", "EXPR_MINUS", 
                      "EXPR_STAR", "EXPR_SLASH", "EXPR_MOD", "EXPR_DOT", 
                      "EXPR_EQEQ", "EXPR_NEQ", "EXPR_LT", "EXPR_GT", "EXPR_LE", 
                      "EXPR_GE", "EXPR_NOT", "EXPR_AND", "EXPR_OR", "EXPR_COLON", 
                      "EXPR_TAG_END", "EXPR_TAG_CLOSE", "EXPR_INT_LITERAL", 
                      "EXPR_FLOAT_LITERAL", "EXPR_STRING_LITERAL", "EXPR_WS", 
                      "EXPR_IDENT" ]

    RULE_document = 0
    RULE_entity = 1
    RULE_element = 2
    RULE_tag_attribute = 3
    RULE_tag_attribute_last = 4
    RULE_directive = 5
    RULE_if_directive = 6
    RULE_if_directive_elif = 7
    RULE_foreach_directive = 8
    RULE_let_directive = 9
    RULE_include_directive = 10
    RULE_insert_directive = 11
    RULE_injection = 12
    RULE_expr = 13
    RULE_expr_or = 14
    RULE_expr_and = 15
    RULE_expr_not = 16
    RULE_expr_comp = 17
    RULE_expr_addsub = 18
    RULE_expr_multdiv = 19
    RULE_expr_dot = 20
    RULE_expr_atom = 21
    RULE_expr_literal = 22

    ruleNames =  [ "document", "entity", "element", "tag_attribute", "tag_attribute_last", 
                   "directive", "if_directive", "if_directive_elif", "foreach_directive", 
                   "let_directive", "include_directive", "insert_directive", 
                   "injection", "expr", "expr_or", "expr_and", "expr_not", 
                   "expr_comp", "expr_addsub", "expr_multdiv", "expr_dot", 
                   "expr_atom", "expr_literal" ]

    EOF = Token.EOF
    COMMENT=1
    VERBATIM=2
    CLOSING_TAG=3
    DIRECTIVE_OPEN=4
    INJECTION_OPEN=5
    TAG_OPEN=6
    TEXT=7
    TAG_NAME=8
    TAG_END=9
    TAG_CLOSE=10
    TAG_EQ=11
    TAG_ATTRIBUTE_NAME=12
    TAG_WS=13
    DIRECTIVE_IF=14
    DIRECTIVE_ELIF=15
    DIRECTIVE_ELSE=16
    DIRECTIVE_FOREACH=17
    DIRECTIVE_IN=18
    DIRECTIVE_LET=19
    DIRECTIVE_EQ=20
    DIRECTIVE_INCLUDE=21
    DIRECTIVE_INSERT=22
    DIRECTIVE_END=23
    DIRECTIVE_CLOSE=24
    DIRECTIVE_IDENTIFIER=25
    DIRECTIVE_WS=26
    DIRECTIVE_FOREACH_IDENTIFIER=27
    DIRECTIVE_FOREACH_WS=28
    DIRECTIVE_INSERT_IDENTIFIER=29
    DIRECTIVE_INSERT_WS=30
    EXPR_LPAREN=31
    EXPR_RPAREN=32
    EXPR_PLUS=33
    EXPR_MINUS=34
    EXPR_STAR=35
    EXPR_SLASH=36
    EXPR_MOD=37
    EXPR_DOT=38
    EXPR_EQEQ=39
    EXPR_NEQ=40
    EXPR_LT=41
    EXPR_GT=42
    EXPR_LE=43
    EXPR_GE=44
    EXPR_NOT=45
    EXPR_AND=46
    EXPR_OR=47
    EXPR_COLON=48
    EXPR_TAG_END=49
    EXPR_TAG_CLOSE=50
    EXPR_INT_LITERAL=51
    EXPR_FLOAT_LITERAL=52
    EXPR_STRING_LITERAL=53
    EXPR_WS=54
    EXPR_IDENT=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DurakParser.EOF, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_document

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = DurakParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.entity()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.VERBATIM) | (1 << DurakParser.DIRECTIVE_OPEN) | (1 << DurakParser.INJECTION_OPEN) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0)):
                    break

            self.state = 51
            self.match(DurakParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERBATIM(self):
            return self.getToken(DurakParser.VERBATIM, 0)

        def element(self):
            return self.getTypedRuleContext(DurakParser.ElementContext,0)


        def directive(self):
            return self.getTypedRuleContext(DurakParser.DirectiveContext,0)


        def injection(self):
            return self.getTypedRuleContext(DurakParser.InjectionContext,0)


        def COMMENT(self):
            return self.getToken(DurakParser.COMMENT, 0)

        def TEXT(self):
            return self.getToken(DurakParser.TEXT, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_entity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntity" ):
                return visitor.visitEntity(self)
            else:
                return visitor.visitChildren(self)




    def entity(self):

        localctx = DurakParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entity)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DurakParser.VERBATIM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(DurakParser.VERBATIM)
                pass
            elif token in [DurakParser.TAG_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.element()
                pass
            elif token in [DurakParser.DIRECTIVE_OPEN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.directive()
                pass
            elif token in [DurakParser.INJECTION_OPEN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.injection()
                pass
            elif token in [DurakParser.COMMENT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(DurakParser.COMMENT)
                pass
            elif token in [DurakParser.TEXT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.match(DurakParser.TEXT)
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


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_OPEN(self):
            return self.getToken(DurakParser.TAG_OPEN, 0)

        def TAG_NAME(self):
            return self.getToken(DurakParser.TAG_NAME, 0)

        def tag_attribute_last(self):
            return self.getTypedRuleContext(DurakParser.Tag_attribute_lastContext,0)


        def EXPR_TAG_CLOSE(self):
            return self.getToken(DurakParser.EXPR_TAG_CLOSE, 0)

        def TAG_CLOSE(self):
            return self.getToken(DurakParser.TAG_CLOSE, 0)

        def tag_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.Tag_attributeContext)
            else:
                return self.getTypedRuleContext(DurakParser.Tag_attributeContext,i)


        def CLOSING_TAG(self):
            return self.getToken(DurakParser.CLOSING_TAG, 0)

        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def TAG_END(self):
            return self.getToken(DurakParser.TAG_END, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = DurakParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(DurakParser.TAG_OPEN)
                self.state = 62
                self.match(DurakParser.TAG_NAME)
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 63
                        self.tag_attribute() 
                    self.state = 68
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 73
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DurakParser.TAG_ATTRIBUTE_NAME]:
                    self.state = 69
                    self.tag_attribute_last()
                    self.state = 70
                    self.match(DurakParser.EXPR_TAG_CLOSE)
                    pass
                elif token in [DurakParser.TAG_CLOSE]:
                    self.state = 72
                    self.match(DurakParser.TAG_CLOSE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(DurakParser.TAG_OPEN)
                self.state = 76
                self.match(DurakParser.TAG_NAME)
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 77
                        self.tag_attribute() 
                    self.state = 82
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DurakParser.TAG_ATTRIBUTE_NAME]:
                    self.state = 83
                    self.tag_attribute_last()
                    self.state = 84
                    self.match(DurakParser.EXPR_TAG_END)
                    pass
                elif token in [DurakParser.TAG_END]:
                    self.state = 86
                    self.match(DurakParser.TAG_END)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.VERBATIM) | (1 << DurakParser.DIRECTIVE_OPEN) | (1 << DurakParser.INJECTION_OPEN) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0):
                    self.state = 89
                    self.entity()
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 95
                self.match(DurakParser.CLOSING_TAG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_ATTRIBUTE_NAME(self):
            return self.getToken(DurakParser.TAG_ATTRIBUTE_NAME, 0)

        def TAG_EQ(self):
            return self.getToken(DurakParser.TAG_EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_COLON(self):
            return self.getToken(DurakParser.EXPR_COLON, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_tag_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_attribute" ):
                return visitor.visitTag_attribute(self)
            else:
                return visitor.visitChildren(self)




    def tag_attribute(self):

        localctx = DurakParser.Tag_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tag_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DurakParser.TAG_ATTRIBUTE_NAME)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DurakParser.TAG_EQ:
                self.state = 99
                self.match(DurakParser.TAG_EQ)
                self.state = 100
                self.expr()
                self.state = 101
                self.match(DurakParser.EXPR_COLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_attribute_lastContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_ATTRIBUTE_NAME(self):
            return self.getToken(DurakParser.TAG_ATTRIBUTE_NAME, 0)

        def TAG_EQ(self):
            return self.getToken(DurakParser.TAG_EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_tag_attribute_last

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTag_attribute_last" ):
                return visitor.visitTag_attribute_last(self)
            else:
                return visitor.visitChildren(self)




    def tag_attribute_last(self):

        localctx = DurakParser.Tag_attribute_lastContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tag_attribute_last)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(DurakParser.TAG_ATTRIBUTE_NAME)
            self.state = 106
            self.match(DurakParser.TAG_EQ)
            self.state = 107
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_directive(self):
            return self.getTypedRuleContext(DurakParser.If_directiveContext,0)


        def foreach_directive(self):
            return self.getTypedRuleContext(DurakParser.Foreach_directiveContext,0)


        def let_directive(self):
            return self.getTypedRuleContext(DurakParser.Let_directiveContext,0)


        def include_directive(self):
            return self.getTypedRuleContext(DurakParser.Include_directiveContext,0)


        def insert_directive(self):
            return self.getTypedRuleContext(DurakParser.Insert_directiveContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = DurakParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_directive)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.if_directive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.foreach_directive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.let_directive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.include_directive()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 113
                self.insert_directive()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._entity = None # EntityContext
            self.main_body = list() # of EntityContexts
            self.else_body = list() # of EntityContexts

        def DIRECTIVE_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.DIRECTIVE_OPEN)
            else:
                return self.getToken(DurakParser.DIRECTIVE_OPEN, i)

        def DIRECTIVE_IF(self):
            return self.getToken(DurakParser.DIRECTIVE_IF, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def CLOSING_TAG(self):
            return self.getToken(DurakParser.CLOSING_TAG, 0)

        def if_directive_elif(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.If_directive_elifContext)
            else:
                return self.getTypedRuleContext(DurakParser.If_directive_elifContext,i)


        def DIRECTIVE_ELSE(self):
            return self.getToken(DurakParser.DIRECTIVE_ELSE, 0)

        def DIRECTIVE_END(self):
            return self.getToken(DurakParser.DIRECTIVE_END, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_if_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_directive" ):
                return visitor.visitIf_directive(self)
            else:
                return visitor.visitChildren(self)




    def if_directive(self):

        localctx = DurakParser.If_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(DurakParser.DIRECTIVE_OPEN)
            self.state = 117
            self.match(DurakParser.DIRECTIVE_IF)
            self.state = 118
            self.expr()
            self.state = 119
            self.match(DurakParser.EXPR_TAG_END)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    localctx._entity = self.entity()
                    localctx.main_body.append(localctx._entity) 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self.if_directive_elif() 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DurakParser.DIRECTIVE_OPEN:
                self.state = 132
                self.match(DurakParser.DIRECTIVE_OPEN)
                self.state = 133
                self.match(DurakParser.DIRECTIVE_ELSE)
                self.state = 134
                self.match(DurakParser.DIRECTIVE_END)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.VERBATIM) | (1 << DurakParser.DIRECTIVE_OPEN) | (1 << DurakParser.INJECTION_OPEN) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0):
                    self.state = 135
                    localctx._entity = self.entity()
                    localctx.else_body.append(localctx._entity)
                    self.state = 140
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 143
            self.match(DurakParser.CLOSING_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_directive_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_OPEN(self):
            return self.getToken(DurakParser.DIRECTIVE_OPEN, 0)

        def DIRECTIVE_ELIF(self):
            return self.getToken(DurakParser.DIRECTIVE_ELIF, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_if_directive_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_directive_elif" ):
                return visitor.visitIf_directive_elif(self)
            else:
                return visitor.visitChildren(self)




    def if_directive_elif(self):

        localctx = DurakParser.If_directive_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_directive_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(DurakParser.DIRECTIVE_OPEN)
            self.state = 146
            self.match(DurakParser.DIRECTIVE_ELIF)
            self.state = 147
            self.expr()
            self.state = 148
            self.match(DurakParser.EXPR_TAG_END)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.entity() 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Foreach_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._entity = None # EntityContext
            self.main_body = list() # of EntityContexts
            self.else_body = list() # of EntityContexts

        def DIRECTIVE_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.DIRECTIVE_OPEN)
            else:
                return self.getToken(DurakParser.DIRECTIVE_OPEN, i)

        def DIRECTIVE_FOREACH(self):
            return self.getToken(DurakParser.DIRECTIVE_FOREACH, 0)

        def DIRECTIVE_FOREACH_IDENTIFIER(self):
            return self.getToken(DurakParser.DIRECTIVE_FOREACH_IDENTIFIER, 0)

        def DIRECTIVE_IN(self):
            return self.getToken(DurakParser.DIRECTIVE_IN, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def CLOSING_TAG(self):
            return self.getToken(DurakParser.CLOSING_TAG, 0)

        def DIRECTIVE_ELSE(self):
            return self.getToken(DurakParser.DIRECTIVE_ELSE, 0)

        def DIRECTIVE_END(self):
            return self.getToken(DurakParser.DIRECTIVE_END, 0)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_foreach_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForeach_directive" ):
                return visitor.visitForeach_directive(self)
            else:
                return visitor.visitChildren(self)




    def foreach_directive(self):

        localctx = DurakParser.Foreach_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_foreach_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(DurakParser.DIRECTIVE_OPEN)
            self.state = 156
            self.match(DurakParser.DIRECTIVE_FOREACH)
            self.state = 157
            self.match(DurakParser.DIRECTIVE_FOREACH_IDENTIFIER)
            self.state = 158
            self.match(DurakParser.DIRECTIVE_IN)
            self.state = 159
            self.expr()
            self.state = 160
            self.match(DurakParser.EXPR_TAG_END)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    localctx._entity = self.entity()
                    localctx.main_body.append(localctx._entity) 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DurakParser.DIRECTIVE_OPEN:
                self.state = 167
                self.match(DurakParser.DIRECTIVE_OPEN)
                self.state = 168
                self.match(DurakParser.DIRECTIVE_ELSE)
                self.state = 169
                self.match(DurakParser.DIRECTIVE_END)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.VERBATIM) | (1 << DurakParser.DIRECTIVE_OPEN) | (1 << DurakParser.INJECTION_OPEN) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0):
                    self.state = 170
                    localctx._entity = self.entity()
                    localctx.else_body.append(localctx._entity)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 178
            self.match(DurakParser.CLOSING_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Let_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._DIRECTIVE_IDENTIFIER = None # Token
            self.idents = list() # of Tokens
            self._expr = None # ExprContext
            self.vals = list() # of ExprContexts
            self._entity = None # EntityContext
            self.body = list() # of EntityContexts

        def DIRECTIVE_OPEN(self):
            return self.getToken(DurakParser.DIRECTIVE_OPEN, 0)

        def DIRECTIVE_LET(self):
            return self.getToken(DurakParser.DIRECTIVE_LET, 0)

        def DIRECTIVE_EQ(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.DIRECTIVE_EQ)
            else:
                return self.getToken(DurakParser.DIRECTIVE_EQ, i)

        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def CLOSING_TAG(self):
            return self.getToken(DurakParser.CLOSING_TAG, 0)

        def DIRECTIVE_IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.DIRECTIVE_IDENTIFIER)
            else:
                return self.getToken(DurakParser.DIRECTIVE_IDENTIFIER, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.ExprContext)
            else:
                return self.getTypedRuleContext(DurakParser.ExprContext,i)


        def EXPR_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.EXPR_COLON)
            else:
                return self.getToken(DurakParser.EXPR_COLON, i)

        def entity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.EntityContext)
            else:
                return self.getTypedRuleContext(DurakParser.EntityContext,i)


        def getRuleIndex(self):
            return DurakParser.RULE_let_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet_directive" ):
                return visitor.visitLet_directive(self)
            else:
                return visitor.visitChildren(self)




    def let_directive(self):

        localctx = DurakParser.Let_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_let_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(DurakParser.DIRECTIVE_OPEN)
            self.state = 181
            self.match(DurakParser.DIRECTIVE_LET)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    localctx._DIRECTIVE_IDENTIFIER = self.match(DurakParser.DIRECTIVE_IDENTIFIER)
                    localctx.idents.append(localctx._DIRECTIVE_IDENTIFIER)
                    self.state = 183
                    self.match(DurakParser.DIRECTIVE_EQ)
                    self.state = 184
                    localctx._expr = self.expr()
                    localctx.vals.append(localctx._expr)
                    self.state = 185
                    self.match(DurakParser.EXPR_COLON) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 192
            localctx._DIRECTIVE_IDENTIFIER = self.match(DurakParser.DIRECTIVE_IDENTIFIER)
            localctx.idents.append(localctx._DIRECTIVE_IDENTIFIER)
            self.state = 193
            self.match(DurakParser.DIRECTIVE_EQ)
            self.state = 194
            localctx._expr = self.expr()
            localctx.vals.append(localctx._expr)
            self.state = 195
            self.match(DurakParser.EXPR_TAG_END)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.VERBATIM) | (1 << DurakParser.DIRECTIVE_OPEN) | (1 << DurakParser.INJECTION_OPEN) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0):
                self.state = 196
                localctx._entity = self.entity()
                localctx.body.append(localctx._entity)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(DurakParser.CLOSING_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_OPEN(self):
            return self.getToken(DurakParser.DIRECTIVE_OPEN, 0)

        def DIRECTIVE_INCLUDE(self):
            return self.getToken(DurakParser.DIRECTIVE_INCLUDE, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_TAG_CLOSE(self):
            return self.getToken(DurakParser.EXPR_TAG_CLOSE, 0)

        def EXPR_TAG_END(self):
            return self.getToken(DurakParser.EXPR_TAG_END, 0)

        def CLOSING_TAG(self):
            return self.getToken(DurakParser.CLOSING_TAG, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DurakParser.ElementContext)
            else:
                return self.getTypedRuleContext(DurakParser.ElementContext,i)


        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.COMMENT)
            else:
                return self.getToken(DurakParser.COMMENT, i)

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.TEXT)
            else:
                return self.getToken(DurakParser.TEXT, i)

        def getRuleIndex(self):
            return DurakParser.RULE_include_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_directive" ):
                return visitor.visitInclude_directive(self)
            else:
                return visitor.visitChildren(self)




    def include_directive(self):

        localctx = DurakParser.Include_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_include_directive)
        self._la = 0 # Token type
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(DurakParser.DIRECTIVE_OPEN)
                self.state = 205
                self.match(DurakParser.DIRECTIVE_INCLUDE)
                self.state = 206
                self.expr()
                self.state = 207
                self.match(DurakParser.EXPR_TAG_CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(DurakParser.DIRECTIVE_OPEN)
                self.state = 210
                self.match(DurakParser.DIRECTIVE_INCLUDE)
                self.state = 211
                self.expr()
                self.state = 212
                self.match(DurakParser.EXPR_TAG_END)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.COMMENT) | (1 << DurakParser.TAG_OPEN) | (1 << DurakParser.TEXT))) != 0):
                    self.state = 216
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [DurakParser.TAG_OPEN]:
                        self.state = 213
                        self.element()
                        pass
                    elif token in [DurakParser.COMMENT]:
                        self.state = 214
                        self.match(DurakParser.COMMENT)
                        pass
                    elif token in [DurakParser.TEXT]:
                        self.state = 215
                        self.match(DurakParser.TEXT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 221
                self.match(DurakParser.CLOSING_TAG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECTIVE_OPEN(self):
            return self.getToken(DurakParser.DIRECTIVE_OPEN, 0)

        def DIRECTIVE_INSERT(self):
            return self.getToken(DurakParser.DIRECTIVE_INSERT, 0)

        def DIRECTIVE_INSERT_IDENTIFIER(self):
            return self.getToken(DurakParser.DIRECTIVE_INSERT_IDENTIFIER, 0)

        def DIRECTIVE_CLOSE(self):
            return self.getToken(DurakParser.DIRECTIVE_CLOSE, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_insert_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_directive" ):
                return visitor.visitInsert_directive(self)
            else:
                return visitor.visitChildren(self)




    def insert_directive(self):

        localctx = DurakParser.Insert_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_insert_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(DurakParser.DIRECTIVE_OPEN)
            self.state = 226
            self.match(DurakParser.DIRECTIVE_INSERT)
            self.state = 227
            self.match(DurakParser.DIRECTIVE_INSERT_IDENTIFIER)
            self.state = 228
            self.match(DurakParser.DIRECTIVE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InjectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INJECTION_OPEN(self):
            return self.getToken(DurakParser.INJECTION_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_TAG_CLOSE(self):
            return self.getToken(DurakParser.EXPR_TAG_CLOSE, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_injection

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInjection" ):
                return visitor.visitInjection(self)
            else:
                return visitor.visitChildren(self)




    def injection(self):

        localctx = DurakParser.InjectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_injection)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(DurakParser.INJECTION_OPEN)
            self.state = 231
            self.expr()
            self.state = 232
            self.match(DurakParser.EXPR_TAG_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_or(self):
            return self.getTypedRuleContext(DurakParser.Expr_orContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = DurakParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expr_or(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr_orContext
            self.right = None # Expr_andContext

        def expr_and(self):
            return self.getTypedRuleContext(DurakParser.Expr_andContext,0)


        def EXPR_OR(self):
            return self.getToken(DurakParser.EXPR_OR, 0)

        def expr_or(self):
            return self.getTypedRuleContext(DurakParser.Expr_orContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_expr_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or" ):
                return visitor.visitExpr_or(self)
            else:
                return visitor.visitChildren(self)



    def expr_or(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_orContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr_or, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.expr_and(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 244
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_orContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_or)
                    self.state = 239
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 240
                    self.match(DurakParser.EXPR_OR)
                    self.state = 241
                    localctx.right = self.expr_and(0) 
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr_andContext
            self.right = None # Expr_notContext

        def expr_not(self):
            return self.getTypedRuleContext(DurakParser.Expr_notContext,0)


        def EXPR_AND(self):
            return self.getToken(DurakParser.EXPR_AND, 0)

        def expr_and(self):
            return self.getTypedRuleContext(DurakParser.Expr_andContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_expr_and

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and" ):
                return visitor.visitExpr_and(self)
            else:
                return visitor.visitChildren(self)



    def expr_and(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_andContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr_and, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_andContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_and)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    self.match(DurakParser.EXPR_AND)
                    self.state = 252
                    localctx.right = self.expr_not() 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPR_NOT(self):
            return self.getToken(DurakParser.EXPR_NOT, 0)

        def expr_comp(self):
            return self.getTypedRuleContext(DurakParser.Expr_compContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_expr_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_not" ):
                return visitor.visitExpr_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_not(self):

        localctx = DurakParser.Expr_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr_not)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DurakParser.EXPR_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(DurakParser.EXPR_NOT)
                self.state = 259
                self.expr_comp(0)
                pass
            elif token in [DurakParser.EXPR_LPAREN, DurakParser.EXPR_INT_LITERAL, DurakParser.EXPR_FLOAT_LITERAL, DurakParser.EXPR_STRING_LITERAL, DurakParser.EXPR_IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expr_comp(0)
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


    class Expr_compContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr_compContext
            self.op = None # Token
            self.right = None # Expr_addsubContext

        def expr_addsub(self):
            return self.getTypedRuleContext(DurakParser.Expr_addsubContext,0)


        def expr_comp(self):
            return self.getTypedRuleContext(DurakParser.Expr_compContext,0)


        def EXPR_EQEQ(self):
            return self.getToken(DurakParser.EXPR_EQEQ, 0)

        def EXPR_NEQ(self):
            return self.getToken(DurakParser.EXPR_NEQ, 0)

        def EXPR_LT(self):
            return self.getToken(DurakParser.EXPR_LT, 0)

        def EXPR_GT(self):
            return self.getToken(DurakParser.EXPR_GT, 0)

        def EXPR_LE(self):
            return self.getToken(DurakParser.EXPR_LE, 0)

        def EXPR_GE(self):
            return self.getToken(DurakParser.EXPR_GE, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_expr_comp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_comp" ):
                return visitor.visitExpr_comp(self)
            else:
                return visitor.visitChildren(self)



    def expr_comp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_compContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr_comp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expr_addsub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_compContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_comp)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.EXPR_EQEQ) | (1 << DurakParser.EXPR_NEQ) | (1 << DurakParser.EXPR_LT) | (1 << DurakParser.EXPR_GT) | (1 << DurakParser.EXPR_LE) | (1 << DurakParser.EXPR_GE))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 268
                    localctx.right = self.expr_addsub(0) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_addsubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr_addsubContext
            self.op = None # Token
            self.right = None # Expr_multdivContext

        def expr_multdiv(self):
            return self.getTypedRuleContext(DurakParser.Expr_multdivContext,0)


        def expr_addsub(self):
            return self.getTypedRuleContext(DurakParser.Expr_addsubContext,0)


        def EXPR_PLUS(self):
            return self.getToken(DurakParser.EXPR_PLUS, 0)

        def EXPR_MINUS(self):
            return self.getToken(DurakParser.EXPR_MINUS, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_expr_addsub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_addsub" ):
                return visitor.visitExpr_addsub(self)
            else:
                return visitor.visitChildren(self)



    def expr_addsub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_addsubContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr_addsub, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.expr_multdiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_addsubContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_addsub)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==DurakParser.EXPR_PLUS or _la==DurakParser.EXPR_MINUS):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 279
                    localctx.right = self.expr_multdiv(0) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_multdivContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Expr_multdivContext
            self.op = None # Token
            self.right = None # Expr_dotContext

        def expr_dot(self):
            return self.getTypedRuleContext(DurakParser.Expr_dotContext,0)


        def expr_multdiv(self):
            return self.getTypedRuleContext(DurakParser.Expr_multdivContext,0)


        def EXPR_STAR(self):
            return self.getToken(DurakParser.EXPR_STAR, 0)

        def EXPR_SLASH(self):
            return self.getToken(DurakParser.EXPR_SLASH, 0)

        def EXPR_MOD(self):
            return self.getToken(DurakParser.EXPR_MOD, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_expr_multdiv

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_multdiv" ):
                return visitor.visitExpr_multdiv(self)
            else:
                return visitor.visitChildren(self)



    def expr_multdiv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_multdivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr_multdiv, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr_dot(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_multdivContext(self, _parentctx, _parentState)
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_multdiv)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.EXPR_STAR) | (1 << DurakParser.EXPR_SLASH) | (1 << DurakParser.EXPR_MOD))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    localctx.right = self.expr_dot(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_dotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.head = None # Expr_dotContext
            self._EXPR_IDENT = None # Token
            self.tail = list() # of Tokens

        def expr_atom(self):
            return self.getTypedRuleContext(DurakParser.Expr_atomContext,0)


        def expr_dot(self):
            return self.getTypedRuleContext(DurakParser.Expr_dotContext,0)


        def EXPR_DOT(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.EXPR_DOT)
            else:
                return self.getToken(DurakParser.EXPR_DOT, i)

        def EXPR_IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(DurakParser.EXPR_IDENT)
            else:
                return self.getToken(DurakParser.EXPR_IDENT, i)

        def getRuleIndex(self):
            return DurakParser.RULE_expr_dot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_dot" ):
                return visitor.visitExpr_dot(self)
            else:
                return visitor.visitChildren(self)



    def expr_dot(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = DurakParser.Expr_dotContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr_dot, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expr_atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = DurakParser.Expr_dotContext(self, _parentctx, _parentState)
                    localctx.head = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_dot)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 302 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 300
                            self.match(DurakParser.EXPR_DOT)
                            self.state = 301
                            localctx._EXPR_IDENT = self.match(DurakParser.EXPR_IDENT)
                            localctx.tail.append(localctx._EXPR_IDENT)

                        else:
                            raise NoViableAltException(self)
                        self.state = 304 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
             
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPR_LPAREN(self):
            return self.getToken(DurakParser.EXPR_LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(DurakParser.ExprContext,0)


        def EXPR_RPAREN(self):
            return self.getToken(DurakParser.EXPR_RPAREN, 0)

        def EXPR_IDENT(self):
            return self.getToken(DurakParser.EXPR_IDENT, 0)

        def expr_literal(self):
            return self.getTypedRuleContext(DurakParser.Expr_literalContext,0)


        def getRuleIndex(self):
            return DurakParser.RULE_expr_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_atom" ):
                return visitor.visitExpr_atom(self)
            else:
                return visitor.visitChildren(self)




    def expr_atom(self):

        localctx = DurakParser.Expr_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_atom)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DurakParser.EXPR_LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(DurakParser.EXPR_LPAREN)
                self.state = 312
                self.expr()
                self.state = 313
                self.match(DurakParser.EXPR_RPAREN)
                pass
            elif token in [DurakParser.EXPR_IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(DurakParser.EXPR_IDENT)
                pass
            elif token in [DurakParser.EXPR_INT_LITERAL, DurakParser.EXPR_FLOAT_LITERAL, DurakParser.EXPR_STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.expr_literal()
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


    class Expr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPR_INT_LITERAL(self):
            return self.getToken(DurakParser.EXPR_INT_LITERAL, 0)

        def EXPR_FLOAT_LITERAL(self):
            return self.getToken(DurakParser.EXPR_FLOAT_LITERAL, 0)

        def EXPR_STRING_LITERAL(self):
            return self.getToken(DurakParser.EXPR_STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DurakParser.RULE_expr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_literal" ):
                return visitor.visitExpr_literal(self)
            else:
                return visitor.visitChildren(self)




    def expr_literal(self):

        localctx = DurakParser.Expr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DurakParser.EXPR_INT_LITERAL) | (1 << DurakParser.EXPR_FLOAT_LITERAL) | (1 << DurakParser.EXPR_STRING_LITERAL))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expr_or_sempred
        self._predicates[15] = self.expr_and_sempred
        self._predicates[17] = self.expr_comp_sempred
        self._predicates[18] = self.expr_addsub_sempred
        self._predicates[19] = self.expr_multdiv_sempred
        self._predicates[20] = self.expr_dot_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_or_sempred(self, localctx:Expr_orContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_and_sempred(self, localctx:Expr_andContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_comp_sempred(self, localctx:Expr_compContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_addsub_sempred(self, localctx:Expr_addsubContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_multdiv_sempred(self, localctx:Expr_multdivContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr_dot_sempred(self, localctx:Expr_dotContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




