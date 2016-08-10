'''
Created on 17/07/2014

@author: bootch
'''

class OffSider(object):
  
  def parse(self, text):
    '''
    Parse text, replacing leading indentation with INDENT and DEDENT tokens.
    
    Generator of lines of text (terminated by newline.)
    
    Invariant:
    dentPrefix is string of braces (in or de dent) or empty (for no change in indentation.)
    dentPrefix is at most one {, but can be many }
    '''
    currentSpaceCount = 0
    stack = [0,]  # Start with indent level 0 pushed

    for line in text.split('\n'):
      
      leadingSpaceCount, remainder = self._countLeadingSpacesIn(line)
      if not line:  # or len(remainder) == 0: 
        " Line is empty, i.e. consecutive newlines.  No effect on indentation. "
        yield('\n')
      else:
        " Line not empty"    
      
        if leadingSpaceCount > currentSpaceCount: 
          " Indentation level has increased. "
          dentPrefix = self._emitIndents(stack, leadingSpaceCount)
          currentSpaceCount = leadingSpaceCount
        elif leadingSpaceCount < currentSpaceCount:
          " Indentation level has decreased one or more times. "
          dentPrefix, currentSpaceCount = self._emitDedents(stack, leadingSpaceCount)
          # Check that leadingSpaceCount matches a previous level
          if leadingSpaceCount > currentSpaceCount:
            print("Invalid indentation at line ")
            return  # Premature end generator
        else:
          " No change in indentation level. "
          dentPrefix = ''
          
        " Emit line with leading spaces replaced by indent/dedent. "
        yield( dentPrefix + remainder + '\n')
        
    # Exhausted lines, yield any final dedents
    dentPrefix, currentSpaceCount = self._emitDedents(stack, leadingSpaceCount=0)
    yield( dentPrefix + '\n')
      
  
  def _emitIndents(self, stack, leadingSpaceCount):
    '''
    Adjust currentSpaceCount to the leadingSpaceCount, emitting dedents.
    '''
    stack.append(leadingSpaceCount)
    return "{" # <I+>"
  
  
  def _emitDedents(self, stack, leadingSpaceCount):
    '''
    Adjust currentSpaceCount to the leadingSpaceCount, emitting dedents.
    '''
    dentPrefix = ''
    while True:
      dentPrefix += "}" # <I->"
      currentSpaceCount = stack.pop()
      print("Popped to:", currentSpaceCount)
      if leadingSpaceCount >= currentSpaceCount:
        break
    # TODO this emits one too many, which doesn't hurt the parser
    # How to fix for both callers?
    return dentPrefix, currentSpaceCount
       
 
  def _countLeadingSpacesIn(self, line):
    '''
    Count leading spaces and non-white remainder.
    '''
    spaceCount = 0
    for char in line:
      if char != ' ': 
        break
      else:
        spaceCount += 1
    
    remainder = line[spaceCount:len(line)]

    return spaceCount, remainder
  
  