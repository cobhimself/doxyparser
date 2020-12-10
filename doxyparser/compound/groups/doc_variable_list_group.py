# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('listitem', 'docListItemType')
@element('varlistentry', 'docVarListEntryType')
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
