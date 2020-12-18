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
from ....decorators.tag import Tag
from ....node import Node
from ..types.doc_caption_type import DocCaptionType
from ..types.doc_row_type import DocRowType

@Attr('cols', int)
@Attr('rows', int)
@Element('caption', 'docCaptionType')
@Element('row', 'docRowType')
class DocTableType(Node):
    """Model representation of a doxygen docTableType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docTableType">
        <xsd:sequence>
          <xsd:element name="caption" type="docCaptionType" minOccurs="0" maxOccurs="1" />
          <xsd:element name="row" type="docRowType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="rows" type="xsd:integer" />
        <xsd:attribute name="cols" type="xsd:integer" />
      </xsd:complexType>
    """


@Tag('caption')
class Caption(DocCaptionType):
    """Model representation of a doxygen caption element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="caption" type="docCaptionType" minOccurs="0" maxOccurs="1" />
    """


@Tag('row')
class Row(DocRowType):
    """Model representation of a doxygen row element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="row" type="docRowType" minOccurs="0" maxOccurs="unbounded" />
    """
