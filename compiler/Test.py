import sys
import antlr3
from CC2Lexer import CC2Lexer
from CC2Parser import CC2Parser


def main(fname):
    ##input = antlr3.ANTLRInputStream(sys.stdin)
    input = antlr3.StringStream(open(fname).read())
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
    main(r'C:\projekte\csProjects\cc2_12\compiler\demo.c2p.vmc')


