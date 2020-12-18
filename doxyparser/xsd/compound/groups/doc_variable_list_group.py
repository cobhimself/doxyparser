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
from ....decorators.tag import Tag
from ....node import Node
from ..types.doc_list_item_type import DocListItemType
from ..types.doc_var_list_entry_type import DocVarListEntryType

@Element('listitem', 'docListItemType')
@Element('varlistentry', 'docVarListEntryType')
class DocVariableListGroup(Node):
    """Model representation of a doxygen docVariableListGroup group.

    Type XSD:

    <xsd:group xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docVariableListGroup">
        <xsd:sequence>
          <xsd:element name="varlistentry" type="docVarListEntryType" />
          <xsd:element name="listitem" type="docListItemType" />
        </xsd:sequence>
      </xsd:group>
    """


@Tag('listitem')
class Listitem(DocListItemType):
    """Model representation of a doxygen listitem element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="listitem" type="docListItemType" />
    """


@Tag('varlistentry')
class Varlistentry(DocVarListEntryType):
    """Model representation of a doxygen varlistentry element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="varlistentry" type="docVarListEntryType" />
    """
