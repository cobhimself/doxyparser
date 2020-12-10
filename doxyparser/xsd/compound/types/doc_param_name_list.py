# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('parametername', '/[@direction={}]', {
    'ins': 'in',
    'outs': 'out',
    'inouts': 'inout',
})
@element('parametertype', 'docParamType')
class DocParamNameList(Node):
    """Model representation of a doxygen docParamNameList type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docParamNameList">
        <xsd:sequence>
          <xsd:element name="parametertype" type="docParamType" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="parametername" type="docParamName" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """
