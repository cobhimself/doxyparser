# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('parameterdescription', 'descriptionType')
@element('parameternamelist', 'docParamNameList')
class DocParamListItem(Node):
    """Model representation of a doxygen docParamListItem type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docParamListItem">
        <xsd:sequence>
          <xsd:element name="parameternamelist" type="docParamNameList" minOccurs="0" maxOccurs="unbounded" />
          <xsd:element name="parameterdescription" type="descriptionType" />
        </xsd:sequence>
      </xsd:complexType>
    """
