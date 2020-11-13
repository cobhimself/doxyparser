#!/usr/bin/env python3
"""
Model representation of a sectiondef Element from doxygen

<xsd:complexType name="sectiondefType">
<xsd:sequence>
    <xsd:element name="header" type="xsd:string" minOccurs="0" />
    <xsd:element name="description" type="descriptionType" minOccurs="0" />
    <xsd:element name="memberdef" type="memberdefType" maxOccurs="unbounded" />
</xsd:sequence>
<xsd:attribute name="kind" type="DoxSectionKind" />
</xsd:complexType>
"""
from ...node import Node

class SectionDef(Node):
    def __init__(self, node, parser):
        super.__init__(node, parser, 'sectiondef')
    
    def get_member_defs(self):
        return self.get_children('memberdef', 'MemberDef')
    
    def get_header(self):
        return self.get_text('header', '')
    
    def get_description(self):
        return self.get_child('description', 'Description')
    
    def get_kind(self):
        return self.get('kind')