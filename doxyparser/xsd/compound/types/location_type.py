# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('bodyend')
@attr('bodyfile')
@attr('bodystart')
@attr('column')
@attr('declcolumn')
@attr('declfile')
@attr('declline')
@attr('file')
@attr('line')
class LocationType(Node):
    """Model representation of a doxygen locationType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="locationType">
        <xsd:attribute name="file" type="xsd:string" />
        <xsd:attribute name="line" type="xsd:integer" />
        <xsd:attribute name="column" type="xsd:integer" use="optional" />
        <xsd:attribute name="declfile" type="xsd:string" use="optional" />
        <xsd:attribute name="declline" type="xsd:integer" use="optional" />
        <xsd:attribute name="declcolumn" type="xsd:integer" use="optional" />
        <xsd:attribute name="bodyfile" type="xsd:string" />
        <xsd:attribute name="bodystart" type="xsd:integer" />
        <xsd:attribute name="bodyend" type="xsd:integer" />
      </xsd:complexType>
    """
