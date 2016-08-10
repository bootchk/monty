#from pyparsing import Word, alphas, OneOrMore, ParserElement, LineEnd # White, 
from pyparsing import *

# newlines are significant to grammar
ParserElement.setDefaultWhitespaceChars(" \t")

'''
grammar
'''
NL = LineEnd()
#NL = Suppress(LineEnd())  # suppress lineEnd from results
# NL = White('\n').suppress()

name = Word( alphas )
className = Word( alphas ) + NL

blankLine = NL.setDebug()

nameSequence = ZeroOrMore(name + NL).setDebug()

superclassNames =  nameSequence + blankLine

attributeDefs = nameSequence + blankLine

methodDefs = nameSequence

classBody = "{" + Optional(superclassNames) + attributeDefs + methodDefs + "}"
classDef =  className + classBody  # "," + Word( alphas ) + "!" 

#Group( element + Optional( Word( digits ), default="1" ) )
module = OneOrMore( classDef )

