from ..types.doccaption import DocCaptionType
from ...decorators import tag


@tag('caption')
class Caption(DocCaptionType):
    """
    Model representation of a caption Element from doxygen

    <xsd:element name="caption" type="docCaptionType" minOccurs="0" maxOccurs="1" />
    """
