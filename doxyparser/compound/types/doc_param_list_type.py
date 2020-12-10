# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('parameteritem', 'docParamListItem')
class DocParamListType(Node):
    """Model representation of a doxygen docParamListType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docParamListType">
        <xsd:sequence>
          <xsd:element name="parameteritem" type="docParamListItem" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="kind" type="DoxParamListKind" /> 
      </xsd:complexType>
    """
