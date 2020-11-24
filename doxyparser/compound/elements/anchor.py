from ..types.docanchor import DocAnchorType
from ...decorators import tag


@tag('anchor')
class Anchor(DocAnchorType):
    """
    Model representation of an anchor Element from doxygen

    <xsd:element name="anchor" type="docAnchorType" />
    """
