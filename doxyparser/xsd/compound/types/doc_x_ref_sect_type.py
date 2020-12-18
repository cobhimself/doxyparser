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
from ..types.description_type import DescriptionType

@Attr('id', str)
@Element('xrefdescription', 'descriptionType')
@Element('xreftitle', str)
class DocXRefSectType(Node):
    """Model representation of a doxygen docXRefSectType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docXRefSectType">
        <xsd:sequence>
          <xsd:element name="xreftitle" type="xsd:string" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="xrefdescription" type="descriptionType" />
        </xsd:sequence>
        <xsd:attribute name="id" type="xsd:string" /> 
      </xsd:complexType>
    """


@Tag('xrefdescription')
class Xrefdescription(DescriptionType):
    """Model representation of a doxygen xrefdescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="xrefdescription" type="descriptionType" />
    """
