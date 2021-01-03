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
from ....decorators.tag import Tag
from ....node import Node
from ..types.compound_type import CompoundType

@Attr('lang', str)
@Attr('version', str)
@Collection('compound', 'CompoundType', {
    '[@kind="{}"]': {
        'classes': 'class',
        'structs': 'struct',
        'unions': 'union',
        'interfaces': 'interface',
        'protocols': 'protocol',
        'categories': 'category',
        'exceptions': 'exception',
        'files': 'file',
        'namespaces': 'namespace',
        'groups': 'group',
        'pages': 'page',
        'examples': 'example',
        'dirs': 'dir',
        'types': 'type',
    }
})
class DoxygenType(Node):
    """Model representation of a doxygen DoxygenType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="DoxygenType">
        <xsd:sequence>
          <xsd:element name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="version" type="xsd:string" use="required" />
        <xsd:attribute ref="xml:lang" use="required" />
      </xsd:complexType>
    """


@Tag('compound')
class Compound(CompoundType):
    """Model representation of a doxygen compound element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="compound" type="CompoundType" minOccurs="0" maxOccurs="unbounded" />
    """
