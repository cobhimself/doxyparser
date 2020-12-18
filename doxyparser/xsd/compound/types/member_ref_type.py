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
from ....decorators.element import Element
from ....node import Node

@Attr('ambiguityscope', str)
@Attr('prot', ['public', 'protected', 'private', 'package'])
@Attr('refid', str)
@Attr('virt', ['non-virtual', 'virtual', 'pure-virtual'])
@Element('name', 'any')
@Element('scope', 'any')
class MemberRefType(Node):
    """Model representation of a doxygen memberRefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="memberRefType">
        <xsd:sequence>
          <xsd:element name="scope" />
          <xsd:element name="name" />
        </xsd:sequence>
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="prot" type="DoxProtectionKind" />
        <xsd:attribute name="virt" type="DoxVirtualKind" />
        <xsd:attribute name="ambiguityscope" type="xsd:string" />
      </xsd:complexType>
    """
