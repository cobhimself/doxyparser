# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@element('xrefdescription', 'descriptionType')
@element('xreftitle', 'simple')
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
