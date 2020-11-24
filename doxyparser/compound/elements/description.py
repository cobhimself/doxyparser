from ..types.description import DescriptionType
from ...decorators import tag


@tag('description')
class Description(DescriptionType):
    """
    Model representation of a description Element from doxygen

    <xsd:element name="description" type="descriptionType" minOccurs="0" />
    """
