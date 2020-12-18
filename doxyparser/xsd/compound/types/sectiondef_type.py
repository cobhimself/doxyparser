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
from ....decorators.tag import Tag
from ....node import Node
from ..types.description_type import DescriptionType
from ..types.memberdef_type import MemberdefType

@Attr('kind', ['user-defined', 'public-type', 'public-func', 'public-attrib', 'public-slot', 'signal', 'dcop-func', 'property', 'event', 'public-static-func', 'public-static-attrib', 'protected-type', 'protected-func', 'protected-attrib', 'protected-slot', 'protected-static-func', 'protected-static-attrib', 'package-type', 'package-func', 'package-attrib', 'package-static-func', 'package-static-attrib', 'private-type', 'private-func', 'private-attrib', 'private-slot', 'private-static-func', 'private-static-attrib', 'friend', 'related', 'define', 'prototype', 'typedef', 'enum', 'func', 'var'])
@Collection('memberdef', 'memberdefType', {
    '/[@accessor={}': {
        'retains': 'retain',
        'copies': 'copy',
        'assigns': 'assign',
        'weaks': 'weak',
        'strongs': 'strong',
        'unretaineds': 'unretained',
    },
    '/[@kind={}': {
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
    },
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    },
    '/[@refqual={}': {
        'lvalues': 'lvalue',
        'rvalues': 'rvalue',
    },
    '/[@virt={}': {
        'non_virtuals': 'non-virtual',
        'virtuals': 'virtual',
        'pure_virtuals': 'pure-virtual',
    }
})
@Element('description', 'descriptionType')
@Element('header', str)
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


@Tag('description')
class Description(DescriptionType):
    """Model representation of a doxygen description element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="description" type="descriptionType" minOccurs="0" />
    """


@Tag('memberdef')
class Memberdef(MemberdefType):
    """Model representation of a doxygen memberdef element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="memberdef" type="memberdefType" maxOccurs="unbounded" />
    """
