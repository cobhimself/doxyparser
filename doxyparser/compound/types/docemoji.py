#!/usr/bin/env python3
"""
Model representation of a docemoji type from doxygen

<xsd:complexType name="docEmojiType">
  <xsd:attribute name="name" type="xsd:string"/>
  <xsd:attribute name="unicode" type="xsd:string"/>
</xsd:complexType>
"""
from ...node import Node

class DocEmoji(Node):
  def __init__(self, node):
      super.__init__(node)
    
  def get_name(self):
    return self.get('name')
  
  def get_unicode(self):
    return self.get('unicode')