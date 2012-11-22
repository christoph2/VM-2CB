import sys
import antlr3
from CC2Lexer import CC2Lexer
from CC2Parser import CC2Parser

import codecs

def main(fname):
    ##input = antlr3.ANTLRInputStream(sys.stdin)
    input = antlr3.StringStream(codecs.open(fname, encoding = 'utf-8').read())
    lexer = CC2Lexer(input)

    tokens = antlr3.CommonTokenStream(lexer)
    parser = CC2Parser(tokens)

    file_return = parser.module()

    tree = file_return.getTree()
    #print tree.toStringTree()

    root = file_return.tree
    nodes = antlr3.tree.CommonTreeNodeStream(root)
    nodes.setTokenStream(tokens)

if __name__ == '__main__':
    main(sys.argv[1])


