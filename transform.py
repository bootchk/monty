from offSider import OffSider
from grammar import module

def convertIndentedToBracedText(text):
    offSider = OffSider()
    bracedText = ''
    for line in offSider.parse(text):
        bracedText += line
    return bracedText

def transform(text):
    braceText = convertIndentedToBracedText(text)
    print(braceText)
    result = module.parseString(braceText)
    return result