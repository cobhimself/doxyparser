"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This class has been auto-generated. To add/modify functionality, extend it.
See util/generator/element_generator.py
"""
from ....node import Node
from ....decorators import element, collection

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
