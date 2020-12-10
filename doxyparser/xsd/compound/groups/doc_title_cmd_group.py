# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@collection('dot', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('image', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('msc', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('plantuml', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('ref', '/[@kindref={}]', {
    'compounds': 'compound',
    'members': 'member',
})
@element('anchor', 'docAnchorType')
@element('bold', 'docMarkupType')
@element('center', 'docMarkupType')
@element('computeroutput', 'docMarkupType')
@element('del', 'docMarkupType')
@element('docbookonly', 'simple')
@element('emoji', 'docEmojiType')
@element('emphasis', 'docMarkupType')
@element('formula', 'docFormulaType')
@element('htmlonly', 'docHtmlOnlyType')
@element('ins', 'docMarkupType')
@element('latexonly', 'simple')
@element('manonly', 'simple')
@element('rtfonly', 'simple')
@element('s', 'docMarkupType')
@element('small', 'docMarkupType')
@element('strike', 'docMarkupType')
@element('subscript', 'docMarkupType')
@element('superscript', 'docMarkupType')
@element('ulink', 'docURLLink')
@element('underline', 'docMarkupType')
@element('xmlonly', 'simple')
@placeholders([
    'linebreak',
    'nonbreakablespace',
    'iexcl',
    'cent',
    'pound',
    'curren',
    'yen',
    'brvbar',
    'sect',
    'umlaut',
    'copy',
    'ordf',
    'laquo',
    'not',
    'shy',
    'registered',
    'macr',
    'deg',
    'plusmn',
    'sup2',
    'sup3',
    'acute',
    'micro',
    'para',
    'middot',
    'cedil',
    'sup1',
    'ordm',
    'raquo',
    'frac14',
    'frac12',
    'frac34',
    'iquest',
    'Agrave',
    'Aacute',
    'Acirc',
    'Atilde',
    'Aumlaut',
    'Aring',
    'AElig',
    'Ccedil',
    'Egrave',
    'Eacute',
    'Ecirc',
    'Eumlaut',
    'Igrave',
    'Iacute',
    'Icirc',
    'Iumlaut',
    'ETH',
    'Ntilde',
    'Ograve',
    'Oacute',
    'Ocirc',
    'Otilde',
    'Oumlaut',
    'times',
    'Oslash',
    'Ugrave',
    'Uacute',
    'Ucirc',
    'Uumlaut',
    'Yacute',
    'THORN',
    'szlig',
    'agrave',
    'aacute',
    'acirc',
    'atilde',
    'aumlaut',
    'aring',
    'aelig',
    'ccedil',
    'egrave',
    'eacute',
    'ecirc',
    'eumlaut',
    'igrave',
    'iacute',
    'icirc',
    'iumlaut',
    'eth',
    'ntilde',
    'ograve',
    'oacute',
    'ocirc',
    'otilde',
    'oumlaut',
    'divide',
    'oslash',
    'ugrave',
    'uacute',
    'ucirc',
    'uumlaut',
    'yacute',
    'thorn',
    'yumlaut',
    'fnof',
    'Alpha',
    'Beta',
    'Gamma',
    'Delta',
    'Epsilon',
    'Zeta',
    'Eta',
    'Theta',
    'Iota',
    'Kappa',
    'Lambda',
    'Mu',
    'Nu',
    'Xi',
    'Omicron',
    'Pi',
    'Rho',
    'Sigma',
    'Tau',
    'Upsilon',
    'Phi',
    'Chi',
    'Psi',
    'Omega',
    'alpha',
    'beta',
    'gamma',
    'delta',
    'epsilon',
    'zeta',
    'eta',
    'theta',
    'iota',
    'kappa',
    'lambda',
    'mu',
    'nu',
    'xi',
    'omicron',
    'pi',
    'rho',
    'sigmaf',
    'sigma',
    'tau',
    'upsilon',
    'phi',
    'chi',
    'psi',
    'omega',
    'thetasym',
    'upsih',
    'piv',
    'bull',
    'hellip',
    'prime',
    'Prime',
    'oline',
    'frasl',
    'weierp',
    'imaginary',
    'real',
    'trademark',
    'alefsym',
    'larr',
    'uarr',
    'rarr',
    'darr',
    'harr',
    'crarr',
    'lArr',
    'uArr',
    'rArr',
    'dArr',
    'hArr',
    'forall',
    'part',
    'exist',
    'empty',
    'nabla',
    'isin',
    'notin',
    'ni',
    'prod',
    'sum',
    'minus',
    'lowast',
    'radic',
    'prop',
    'infin',
    'ang',
    'and',
    'or',
    'cap',
    'cup',
    'int',
    'there4',
    'sim',
    'cong',
    'asymp',
    'ne',
    'equiv',
    'le',
    'ge',
    'sub',
    'sup',
    'nsub',
    'sube',
    'supe',
    'oplus',
    'otimes',
    'perp',
    'sdot',
    'lceil',
    'rceil',
    'lfloor',
    'rfloor',
    'lang',
    'rang',
    'loz',
    'spades',
    'clubs',
    'hearts',
    'diams',
    'OElig',
    'oelig',
    'Scaron',
    'scaron',
    'Yumlaut',
    'circ',
    'tilde',
    'ensp',
    'emsp',
    'thinsp',
    'zwnj',
    'zwj',
    'lrm',
    'rlm',
    'ndash',
    'mdash',
    'lsquo',
    'rsquo',
    'sbquo',
    'ldquo',
    'rdquo',
    'bdquo',
    'dagger',
    'Dagger',
    'permil',
    'lsaquo',
    'rsaquo',
    'euro',
    'tm'
])
class DocTitleCmdGroup(Node):
    """Model representation of a doxygen docTitleCmdGroup group.

    Type XSD:

    <xsd:group xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docTitleCmdGroup">
        <xsd:choice>
          <xsd:element name="ulink" type="docURLLink" />
          <xsd:element name="bold" type="docMarkupType" />
          <xsd:element name="s" type="docMarkupType" />
          <xsd:element name="strike" type="docMarkupType" />
          <xsd:element name="underline" type="docMarkupType" />
          <xsd:element name="emphasis" type="docMarkupType" />
          <xsd:element name="computeroutput" type="docMarkupType" />
          <xsd:element name="subscript" type="docMarkupType" />
          <xsd:element name="superscript" type="docMarkupType" />
          <xsd:element name="center" type="docMarkupType" />
          <xsd:element name="small" type="docMarkupType" />
          <xsd:element name="del" type="docMarkupType" />
          <xsd:element name="ins" type="docMarkupType" />
          <xsd:element name="htmlonly" type="docHtmlOnlyType" />
          <xsd:element name="manonly" type="xsd:string" />
          <xsd:element name="xmlonly" type="xsd:string" />
          <xsd:element name="rtfonly" type="xsd:string" />
          <xsd:element name="latexonly" type="xsd:string" />
          <xsd:element name="docbookonly" type="xsd:string" />
          <xsd:element name="image" type="docImageType" />
          <xsd:element name="dot" type="docImageType" />
          <xsd:element name="msc" type="docImageType" />
          <xsd:element name="plantuml" type="docImageType" />
          <xsd:element name="anchor" type="docAnchorType" />
          <xsd:element name="formula" type="docFormulaType" />
          <xsd:element name="ref" type="docRefTextType" />
          <xsd:element name="emoji" type="docEmojiType" />
          <xsd:element name="linebreak" type="docEmptyType" />
          <xsd:element name="nonbreakablespace" type="docEmptyType" />
          <xsd:element name="iexcl" type="docEmptyType" />
          <xsd:element name="cent" type="docEmptyType" />
          <xsd:element name="pound" type="docEmptyType" />
          <xsd:element name="curren" type="docEmptyType" />
          <xsd:element name="yen" type="docEmptyType" />
          <xsd:element name="brvbar" type="docEmptyType" />
          <xsd:element name="sect" type="docEmptyType" />
          <xsd:element name="umlaut" type="docEmptyType" />
          <xsd:element name="copy" type="docEmptyType" />
          <xsd:element name="ordf" type="docEmptyType" />
          <xsd:element name="laquo" type="docEmptyType" />
          <xsd:element name="not" type="docEmptyType" />
          <xsd:element name="shy" type="docEmptyType" />
          <xsd:element name="registered" type="docEmptyType" />
          <xsd:element name="macr" type="docEmptyType" />
          <xsd:element name="deg" type="docEmptyType" />
          <xsd:element name="plusmn" type="docEmptyType" />
          <xsd:element name="sup2" type="docEmptyType" />
          <xsd:element name="sup3" type="docEmptyType" />
          <xsd:element name="acute" type="docEmptyType" />
          <xsd:element name="micro" type="docEmptyType" />
          <xsd:element name="para" type="docEmptyType" />
          <xsd:element name="middot" type="docEmptyType" />
          <xsd:element name="cedil" type="docEmptyType" />
          <xsd:element name="sup1" type="docEmptyType" />
          <xsd:element name="ordm" type="docEmptyType" />
          <xsd:element name="raquo" type="docEmptyType" />
          <xsd:element name="frac14" type="docEmptyType" />
          <xsd:element name="frac12" type="docEmptyType" />
          <xsd:element name="frac34" type="docEmptyType" />
          <xsd:element name="iquest" type="docEmptyType" />
          <xsd:element name="Agrave" type="docEmptyType" />
          <xsd:element name="Aacute" type="docEmptyType" />
          <xsd:element name="Acirc" type="docEmptyType" />
          <xsd:element name="Atilde" type="docEmptyType" />
          <xsd:element name="Aumlaut" type="docEmptyType" />
          <xsd:element name="Aring" type="docEmptyType" />
          <xsd:element name="AElig" type="docEmptyType" />
          <xsd:element name="Ccedil" type="docEmptyType" />
          <xsd:element name="Egrave" type="docEmptyType" />
          <xsd:element name="Eacute" type="docEmptyType" />
          <xsd:element name="Ecirc" type="docEmptyType" />
          <xsd:element name="Eumlaut" type="docEmptyType" />
          <xsd:element name="Igrave" type="docEmptyType" />
          <xsd:element name="Iacute" type="docEmptyType" />
          <xsd:element name="Icirc" type="docEmptyType" />
          <xsd:element name="Iumlaut" type="docEmptyType" />
          <xsd:element name="ETH" type="docEmptyType" />
          <xsd:element name="Ntilde" type="docEmptyType" />
          <xsd:element name="Ograve" type="docEmptyType" />
          <xsd:element name="Oacute" type="docEmptyType" />
          <xsd:element name="Ocirc" type="docEmptyType" />
          <xsd:element name="Otilde" type="docEmptyType" />
          <xsd:element name="Oumlaut" type="docEmptyType" />
          <xsd:element name="times" type="docEmptyType" />
          <xsd:element name="Oslash" type="docEmptyType" />
          <xsd:element name="Ugrave" type="docEmptyType" />
          <xsd:element name="Uacute" type="docEmptyType" />
          <xsd:element name="Ucirc" type="docEmptyType" />
          <xsd:element name="Uumlaut" type="docEmptyType" />
          <xsd:element name="Yacute" type="docEmptyType" />
          <xsd:element name="THORN" type="docEmptyType" />
          <xsd:element name="szlig" type="docEmptyType" />
          <xsd:element name="agrave" type="docEmptyType" />
          <xsd:element name="aacute" type="docEmptyType" />
          <xsd:element name="acirc" type="docEmptyType" />
          <xsd:element name="atilde" type="docEmptyType" />
          <xsd:element name="aumlaut" type="docEmptyType" />
          <xsd:element name="aring" type="docEmptyType" />
          <xsd:element name="aelig" type="docEmptyType" />
          <xsd:element name="ccedil" type="docEmptyType" />
          <xsd:element name="egrave" type="docEmptyType" />
          <xsd:element name="eacute" type="docEmptyType" />
          <xsd:element name="ecirc" type="docEmptyType" />
          <xsd:element name="eumlaut" type="docEmptyType" />
          <xsd:element name="igrave" type="docEmptyType" />
          <xsd:element name="iacute" type="docEmptyType" />
          <xsd:element name="icirc" type="docEmptyType" />
          <xsd:element name="iumlaut" type="docEmptyType" />
          <xsd:element name="eth" type="docEmptyType" />
          <xsd:element name="ntilde" type="docEmptyType" />
          <xsd:element name="ograve" type="docEmptyType" />
          <xsd:element name="oacute" type="docEmptyType" />
          <xsd:element name="ocirc" type="docEmptyType" />
          <xsd:element name="otilde" type="docEmptyType" />
          <xsd:element name="oumlaut" type="docEmptyType" />
          <xsd:element name="divide" type="docEmptyType" />
          <xsd:element name="oslash" type="docEmptyType" />
          <xsd:element name="ugrave" type="docEmptyType" />
          <xsd:element name="uacute" type="docEmptyType" />
          <xsd:element name="ucirc" type="docEmptyType" />
          <xsd:element name="uumlaut" type="docEmptyType" />
          <xsd:element name="yacute" type="docEmptyType" />
          <xsd:element name="thorn" type="docEmptyType" />
          <xsd:element name="yumlaut" type="docEmptyType" />
          <xsd:element name="fnof" type="docEmptyType" />
          <xsd:element name="Alpha" type="docEmptyType" />
          <xsd:element name="Beta" type="docEmptyType" />
          <xsd:element name="Gamma" type="docEmptyType" />
          <xsd:element name="Delta" type="docEmptyType" />
          <xsd:element name="Epsilon" type="docEmptyType" />
          <xsd:element name="Zeta" type="docEmptyType" />
          <xsd:element name="Eta" type="docEmptyType" />
          <xsd:element name="Theta" type="docEmptyType" />
          <xsd:element name="Iota" type="docEmptyType" />
          <xsd:element name="Kappa" type="docEmptyType" />
          <xsd:element name="Lambda" type="docEmptyType" />
          <xsd:element name="Mu" type="docEmptyType" />
          <xsd:element name="Nu" type="docEmptyType" />
          <xsd:element name="Xi" type="docEmptyType" />
          <xsd:element name="Omicron" type="docEmptyType" />
          <xsd:element name="Pi" type="docEmptyType" />
          <xsd:element name="Rho" type="docEmptyType" />
          <xsd:element name="Sigma" type="docEmptyType" />
          <xsd:element name="Tau" type="docEmptyType" />
          <xsd:element name="Upsilon" type="docEmptyType" />
          <xsd:element name="Phi" type="docEmptyType" />
          <xsd:element name="Chi" type="docEmptyType" />
          <xsd:element name="Psi" type="docEmptyType" />
          <xsd:element name="Omega" type="docEmptyType" />
          <xsd:element name="alpha" type="docEmptyType" />
          <xsd:element name="beta" type="docEmptyType" />
          <xsd:element name="gamma" type="docEmptyType" />
          <xsd:element name="delta" type="docEmptyType" />
          <xsd:element name="epsilon" type="docEmptyType" />
          <xsd:element name="zeta" type="docEmptyType" />
          <xsd:element name="eta" type="docEmptyType" />
          <xsd:element name="theta" type="docEmptyType" />
          <xsd:element name="iota" type="docEmptyType" />
          <xsd:element name="kappa" type="docEmptyType" />
          <xsd:element name="lambda" type="docEmptyType" />
          <xsd:element name="mu" type="docEmptyType" />
          <xsd:element name="nu" type="docEmptyType" />
          <xsd:element name="xi" type="docEmptyType" />
          <xsd:element name="omicron" type="docEmptyType" />
          <xsd:element name="pi" type="docEmptyType" />
          <xsd:element name="rho" type="docEmptyType" />
          <xsd:element name="sigmaf" type="docEmptyType" />
          <xsd:element name="sigma" type="docEmptyType" />
          <xsd:element name="tau" type="docEmptyType" />
          <xsd:element name="upsilon" type="docEmptyType" />
          <xsd:element name="phi" type="docEmptyType" />
          <xsd:element name="chi" type="docEmptyType" />
          <xsd:element name="psi" type="docEmptyType" />
          <xsd:element name="omega" type="docEmptyType" />
          <xsd:element name="thetasym" type="docEmptyType" />
          <xsd:element name="upsih" type="docEmptyType" />
          <xsd:element name="piv" type="docEmptyType" />
          <xsd:element name="bull" type="docEmptyType" />
          <xsd:element name="hellip" type="docEmptyType" />
          <xsd:element name="prime" type="docEmptyType" />
          <xsd:element name="Prime" type="docEmptyType" />
          <xsd:element name="oline" type="docEmptyType" />
          <xsd:element name="frasl" type="docEmptyType" />
          <xsd:element name="weierp" type="docEmptyType" />
          <xsd:element name="imaginary" type="docEmptyType" />
          <xsd:element name="real" type="docEmptyType" />
          <xsd:element name="trademark" type="docEmptyType" />
          <xsd:element name="alefsym" type="docEmptyType" />
          <xsd:element name="larr" type="docEmptyType" />
          <xsd:element name="uarr" type="docEmptyType" />
          <xsd:element name="rarr" type="docEmptyType" />
          <xsd:element name="darr" type="docEmptyType" />
          <xsd:element name="harr" type="docEmptyType" />
          <xsd:element name="crarr" type="docEmptyType" />
          <xsd:element name="lArr" type="docEmptyType" />
          <xsd:element name="uArr" type="docEmptyType" />
          <xsd:element name="rArr" type="docEmptyType" />
          <xsd:element name="dArr" type="docEmptyType" />
          <xsd:element name="hArr" type="docEmptyType" />
          <xsd:element name="forall" type="docEmptyType" />
          <xsd:element name="part" type="docEmptyType" />
          <xsd:element name="exist" type="docEmptyType" />
          <xsd:element name="empty" type="docEmptyType" />
          <xsd:element name="nabla" type="docEmptyType" />
          <xsd:element name="isin" type="docEmptyType" />
          <xsd:element name="notin" type="docEmptyType" />
          <xsd:element name="ni" type="docEmptyType" />
          <xsd:element name="prod" type="docEmptyType" />
          <xsd:element name="sum" type="docEmptyType" />
          <xsd:element name="minus" type="docEmptyType" />
          <xsd:element name="lowast" type="docEmptyType" />
          <xsd:element name="radic" type="docEmptyType" />
          <xsd:element name="prop" type="docEmptyType" />
          <xsd:element name="infin" type="docEmptyType" />
          <xsd:element name="ang" type="docEmptyType" />
          <xsd:element name="and" type="docEmptyType" />
          <xsd:element name="or" type="docEmptyType" />
          <xsd:element name="cap" type="docEmptyType" />
          <xsd:element name="cup" type="docEmptyType" />
          <xsd:element name="int" type="docEmptyType" />
          <xsd:element name="there4" type="docEmptyType" />
          <xsd:element name="sim" type="docEmptyType" />
          <xsd:element name="cong" type="docEmptyType" />
          <xsd:element name="asymp" type="docEmptyType" />
          <xsd:element name="ne" type="docEmptyType" />
          <xsd:element name="equiv" type="docEmptyType" />
          <xsd:element name="le" type="docEmptyType" />
          <xsd:element name="ge" type="docEmptyType" />
          <xsd:element name="sub" type="docEmptyType" />
          <xsd:element name="sup" type="docEmptyType" />
          <xsd:element name="nsub" type="docEmptyType" />
          <xsd:element name="sube" type="docEmptyType" />
          <xsd:element name="supe" type="docEmptyType" />
          <xsd:element name="oplus" type="docEmptyType" />
          <xsd:element name="otimes" type="docEmptyType" />
          <xsd:element name="perp" type="docEmptyType" />
          <xsd:element name="sdot" type="docEmptyType" />
          <xsd:element name="lceil" type="docEmptyType" />
          <xsd:element name="rceil" type="docEmptyType" />
          <xsd:element name="lfloor" type="docEmptyType" />
          <xsd:element name="rfloor" type="docEmptyType" />
          <xsd:element name="lang" type="docEmptyType" />
          <xsd:element name="rang" type="docEmptyType" />
          <xsd:element name="loz" type="docEmptyType" />
          <xsd:element name="spades" type="docEmptyType" />
          <xsd:element name="clubs" type="docEmptyType" />
          <xsd:element name="hearts" type="docEmptyType" />
          <xsd:element name="diams" type="docEmptyType" />
          <xsd:element name="OElig" type="docEmptyType" />
          <xsd:element name="oelig" type="docEmptyType" />
          <xsd:element name="Scaron" type="docEmptyType" />
          <xsd:element name="scaron" type="docEmptyType" />
          <xsd:element name="Yumlaut" type="docEmptyType" />
          <xsd:element name="circ" type="docEmptyType" />
          <xsd:element name="tilde" type="docEmptyType" />
          <xsd:element name="ensp" type="docEmptyType" />
          <xsd:element name="emsp" type="docEmptyType" />
          <xsd:element name="thinsp" type="docEmptyType" />
          <xsd:element name="zwnj" type="docEmptyType" />
          <xsd:element name="zwj" type="docEmptyType" />
          <xsd:element name="lrm" type="docEmptyType" />
          <xsd:element name="rlm" type="docEmptyType" />
          <xsd:element name="ndash" type="docEmptyType" />
          <xsd:element name="mdash" type="docEmptyType" />
          <xsd:element name="lsquo" type="docEmptyType" />
          <xsd:element name="rsquo" type="docEmptyType" />
          <xsd:element name="sbquo" type="docEmptyType" />
          <xsd:element name="ldquo" type="docEmptyType" />
          <xsd:element name="rdquo" type="docEmptyType" />
          <xsd:element name="bdquo" type="docEmptyType" />
          <xsd:element name="dagger" type="docEmptyType" />
          <xsd:element name="Dagger" type="docEmptyType" />
          <xsd:element name="permil" type="docEmptyType" />
          <xsd:element name="lsaquo" type="docEmptyType" />
          <xsd:element name="rsaquo" type="docEmptyType" />
          <xsd:element name="euro" type="docEmptyType" />
          <xsd:element name="tm" type="docEmptyType" />
        </xsd:choice>
      </xsd:group>
    """
