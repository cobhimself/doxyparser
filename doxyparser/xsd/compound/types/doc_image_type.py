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
from ....decorators.boolattr import BoolAttr
from ..groups.doc_title_cmd_group import DocTitleCmdGroup

@Attr('caption', str)
@Attr('height', str)
@Attr('name', str)
@Attr('type', ['html', 'latex', 'docbook', 'rtf'])
@Attr('width', str)
@BoolAttr('inline')
class DocImageType(DocTitleCmdGroup):
    """Model representation of a doxygen docImageType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docImageType" mixed="true">
        <xsd:group ref="docTitleCmdGroup" minOccurs="0" maxOccurs="unbounded" />
        <xsd:attribute name="type" type="DoxImageKind" use="optional" />
        <xsd:attribute name="name" type="xsd:string" use="optional" />
        <xsd:attribute name="width" type="xsd:string" use="optional" />
        <xsd:attribute name="height" type="xsd:string" use="optional" />
        <xsd:attribute name="inline" type="DoxBool" use="optional" />
        <xsd:attribute name="caption" type="xsd:string" use="optional" />
      </xsd:complexType>
    """
