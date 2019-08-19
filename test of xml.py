# use SAX to parse xml
from xml.parsers.expat import ParserCreate


class DefaultSAXHandler(object):
    def start_element(self, name, attrs):
        print("SAX:start_element: %s, attrs: %s" % (name, str(attrs)))
    
    def end_element(self, name):
        print("SAX:end_element: %s" % name)
    
    def char_data(self, text):
        print("SAX:char_data: %s" % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="ruby">Ruby</a></li>
</ol>
'''
# create a xml example

# parse it
handler = DefaultSAXHandler()
parser = ParserCreate()

parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data # customize handler action

parser.Parse(xml)
