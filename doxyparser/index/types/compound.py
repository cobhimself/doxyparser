#!/usr/bin/env python3
"""
Model representation of a CompoundType Element from doxygen

<xsd:complexType name="CompoundType">
  <xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
    <xsd:element name="member" type="MemberType" minOccurs="0" maxOccurs="unbounded"/>
  </xsd:sequence>
  <xsd:attribute name="refid" type="xsd:string" use="required"/>
  <xsd:attribute name="kind" type="CompoundKind" use="required"/>
</xsd:complexType>

"""
from ...node import Node


class Compound(Node):
    def __init__(self, node):
        super().__init__(node)

    def get_name(self):
        return self.get_text('name')

    def get_members(self, kind=None):
        path = '' if kind == None else '/[@kind="' + kind + '"]'
        return self.get_children(
            xsd='index',
            tag='member',
            path=path
        )

    def get_refid(self):
        return self.get('refid')

    def get_kind(self):
        return self.get('kind')

    def get_member_functions(self):
        return self.get_members('function')

    def get_member_variables(self):
        return self.get_members('variable')
