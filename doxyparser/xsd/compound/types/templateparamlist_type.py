# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@element('param', 'paramType')
class TemplateparamlistType(Node):
    """Model representation of a doxygen templateparamlistType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="templateparamlistType">
        <xsd:sequence>
          <xsd:element name="param" type="paramType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
      </xsd:complexType>
    """
