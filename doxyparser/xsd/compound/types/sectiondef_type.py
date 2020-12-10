# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('memberdef', '/[@accessor={}]', {
    'retains': 'retain',
    'copies': 'copy',
    'assigns': 'assign',
    'weaks': 'weak',
    'strongs': 'strong',
    'unretaineds': 'unretained',
})
@collection('memberdef', '/[@kind={}]', {
    'defines': 'define',
    'properties': 'property',
    'events': 'event',
    'variables': 'variable',
    'typedefs': 'typedef',
    'enums': 'enum',
    'functions': 'function',
    'signals': 'signal',
    'prototypes': 'prototype',
    'friends': 'friend',
    'dcops': 'dcop',
    'slots': 'slot',
    'interfaces': 'interface',
    'services': 'service',
})
@collection('memberdef', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('memberdef', '/[@refqual={}]', {
    'lvalues': 'lvalue',
    'rvalues': 'rvalue',
})
@collection('memberdef', '/[@virt={}]', {
    'non_virtuals': 'non-virtual',
    'virtuals': 'virtual',
    'pure_virtuals': 'pure-virtual',
})
@element('description', 'descriptionType')
@element('header', 'simple')
class SectiondefType(Node):
    """Model representation of a doxygen sectiondefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="sectiondefType">
        <xsd:sequence>
          <xsd:element name="header" type="xsd:string" minOccurs="0" />
          <xsd:element name="description" type="descriptionType" minOccurs="0" />
          <xsd:element name="memberdef" type="memberdefType" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="kind" type="DoxSectionKind" />
      </xsd:complexType>
    """
