'''
Created on 17/07/2014

@author: bootch
'''
from transform import transform
#from shlex import shlex



# test cases

text = r"""foo
  superclass
  superclass
  
  state
  
  method"""
  
" no superclasses: blank line"
text1 = r"""foo
  
  
  state
  state2
  
  method"""

" no superclasses or methods: blank lines"
text2 = r"""foo
  
  
  state
  state2
"""

invalidIndentationText = r"""
foo
  superclass
  
  state
  
  method
 err"""



print(text)      
result = transform(text2)
print(result)

