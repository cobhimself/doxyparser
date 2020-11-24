from ..types.docentry import DocEntryType
from ...decorators import tag


@tag('entry')
class Entry(DocEntryType):
    """
    Model representation of an entry Element from doxygen

    <xsd:element name="entry" type="docEntryType" minOccurs="0" maxOccurs="unbounded" />
    """
