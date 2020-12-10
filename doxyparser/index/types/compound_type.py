# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('refid')
@collection('member', '/[@kind={}]', {
    'defines': 'define',
    'properties': 'property',
    'events': 'event',
    'variables': 'variable',
    'typedefs': 'typedef',
    'enums': 'enum',
    'enumvalues': 'enumvalue',
    'functions': 'function',
    'signals': 'signal',
    'prototypes': 'prototype',
    'friends': 'friend',
    'dcops': 'dcop',
    'slots': 'slot',
})
@element('name', 'simple')
class CompoundType(Node):
    """Model representation of a doxygen CompoundType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="CompoundType">
        <xsd:sequence>
          <xsd:element name="name" type="xsd:string" />
          <xsd:element name="member" type="MemberType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="refid" type="xsd:string" use="required" />
        <xsd:attribute name="kind" type="CompoundKind" use="required" />
      </xsd:complexType>
    """
