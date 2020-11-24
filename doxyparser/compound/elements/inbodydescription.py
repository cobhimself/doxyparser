from ..types.description import DescriptionType
from ...decorators import tag


@tag('inbodydescription')
class InBodyDescription(DescriptionType):
    """
    Model representation of an inbodydescription Element from doxygen

    <xsd:element name="inbodydescription" type="descriptionType" minOccurs="0" />
    """
