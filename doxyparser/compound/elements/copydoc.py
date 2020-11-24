from ..types.doccopy import DocCopyType
from ...decorators import tag


@tag('copydoc')
class CopyDoc(DocCopyType):
    """
    Model representation of a copydoc Element from doxygen

    <xsd:element name="emoji" type="docEmojiType" />
    """
