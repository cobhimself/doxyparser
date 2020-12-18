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

from ....decorators.element import Element
from ....node import Node
from ..types.tableofcontents_type import TableofcontentsType

@Element('name', str)
@Element('reference', str)
@Element('tableofcontents', 'tableofcontentsType')
class TableofcontentsKindType(Node):
    """Model representation of a doxygen tableofcontentsKindType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="tableofcontentsKindType">
        <xsd:sequence>
          <xsd:element name="name" type="xsd:string" minOccurs="1" maxOccurs="1" />
          <xsd:element name="reference" type="xsd:string" minOccurs="1" maxOccurs="1" />
          <xsd:element name="tableofcontents" type="tableofcontentsType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """


@Tag('tableofcontents')
class Tableofcontents(TableofcontentsType):
    """Model representation of a doxygen tableofcontents element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="tableofcontents" type="tableofcontentsType" minOccurs="0" maxOccurs="unbounded" />
    """
