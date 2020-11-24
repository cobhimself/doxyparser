from ..types.description import DescriptionType
from ...decorators import tag


@tag('detaileddescription')
class DetailedDescription(DescriptionType):
    """
    Model representation of a detaileddescription Element from doxygen

    <xsd:element name="detaileddescription" type="descriptionType" minOccurs="0" />
    """
