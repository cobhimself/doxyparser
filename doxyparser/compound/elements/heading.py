from ..types.docheading import DocHeadingType
from ...decorators import tag


@tag('heading')
class Heading(DocHeadingType):
    """
    Model representation of a heading Element from doxygen

    <xsd:element name="heading" type="docHeadingType" />
    """
