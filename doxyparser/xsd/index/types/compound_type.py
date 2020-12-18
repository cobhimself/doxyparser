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

from ....decorators.attr import Attr
from ....decorators.collection import Collection
from ....decorators.element import Element
from ....node import Node
from ..types.member_type import MemberType

@Attr('kind', ['class', 'struct', 'union', 'interface', 'protocol', 'category', 'exception', 'file', 'namespace', 'group', 'page', 'example', 'dir', 'type'])
@Attr('refid', str)
@Collection('member', 'MemberType', {
    '/[@kind={}': {
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
    }
})
@Element('name', str)
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


class Member(MemberType):
    """Model representation of a doxygen member element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="member" type="MemberType" minOccurs="0" maxOccurs="unbounded" />
    """
