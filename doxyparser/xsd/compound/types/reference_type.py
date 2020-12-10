# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('compoundref')
@attr('endline')
@attr('refid')
@attr('startline')
class ReferenceType(Node):
    """Model representation of a doxygen referenceType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="referenceType" mixed="true">
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="compoundref" type="xsd:string" use="optional" />
        <xsd:attribute name="startline" type="xsd:integer" />
        <xsd:attribute name="endline" type="xsd:integer" />
      </xsd:complexType>
    """
