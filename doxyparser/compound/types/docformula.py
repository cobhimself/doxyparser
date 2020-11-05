#!/usr/bin/env python3
"""
Model representation of a docformula type from doxygen

<xsd:complexType name="docFormulaType" mixed="true">
  <xsd:attribute name="id" type="xsd:string" />
</xsd:complexType>
"""
from ...node import Node

class DocFormula(Node):
  def __init__(self, node):
      super.__init__(node)
  
  def get_id(self):
    return self.get('id')