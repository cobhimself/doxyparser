# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('lineno')
@attr('refid')
@boolattr('external')
@collection('highlight', '/[@class={}]', {
    'comments': 'comment',
    'normals': 'normal',
    'preprocessors': 'preprocessor',
    'keywords': 'keyword',
    'keywordtypes': 'keywordtype',
    'keywordflows': 'keywordflow',
    'stringliterals': 'stringliteral',
    'charliterals': 'charliteral',
    'vhdlkeywords': 'vhdlkeyword',
    'vhdllogics': 'vhdllogic',
    'vhdlchars': 'vhdlchar',
    'vhdldigits': 'vhdldigit',
})
class CodelineType(Node):
    """Model representation of a doxygen codelineType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="codelineType">
        <xsd:sequence>
          <xsd:element name="highlight" type="highlightType" minOccurs="0" maxOccurs="unbounded" />
        </xsd:sequence>
        <xsd:attribute name="lineno" type="xsd:integer" />
        <xsd:attribute name="refid" type="xsd:string" />
        <xsd:attribute name="refkind" type="DoxRefKind" />
        <xsd:attribute name="external" type="DoxBool" />
      </xsd:complexType>
    """
