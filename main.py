'''
Created on 17/07/2014

@author: bootch
'''
from offSider import OffSider
#from shlex import shlex


from pyparsing import Word, alphas, OneOrMore, ParserElement, LineEnd # White, 

# newlines are significant to grammar
ParserElement.setDefaultWhitespaceChars(" \t")

'''
grammar
'''
NL = '\n'
NL = LineEnd()
# NL = White('\n').suppress()
className = Word( alphas ) + NL
classBody = "{" + className + LineEnd() + className + LineEnd() + className + "}"
classDef =  className + classBody  # "," + Word( alphas ) + "!" 
#Group( element + Optional( Word( digits ), default="1" ) )
module = OneOrMore( classDef )


text = r"""foo
  superclass
  
  state
  
  method"""

invalidIndentationText = r"""
foo
  superclass
  
  state
  
  method
 err"""

# Convert indented text to braced text
offSider = OffSider()
bracedText = ''
for line in offSider.parse(text):
  bracedText += line
  
print(bracedText)
      
print(module.parseString(bracedText))

