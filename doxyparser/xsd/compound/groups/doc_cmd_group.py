"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This class has been auto-generated. To add/modify functionality, extend it.
See util/generator/element_generator.py
"""

from ....decorators.collection import Collection
from ....decorators.element import Element
from ....decorators.placeholders import Placeholders
from ..types.doc_block_quote_type import DocBlockQuoteType
from ..types.doc_copy_type import DocCopyType
from ..types.doc_heading_type import DocHeadingType
from ..types.doc_image_type import DocImageType
from ..types.doc_index_entry_type import DocIndexEntryType
from ..types.doc_language_type import DocLanguageType
from ..types.doc_list_type import DocListType
from ..types.doc_markup_type import DocMarkupType
from ..types.doc_par_block_type import DocParBlockType
from ..types.doc_param_list_type import DocParamListType
from ..types.doc_simple_sect_type import DocSimpleSectType
from ..types.doc_table_type import DocTableType
from ..types.doc_title_type import DocTitleType
from ..types.doc_toc_list_type import DocTocListType
from ..types.doc_variable_list_type import DocVariableListType
from ..types.doc_x_ref_sect_type import DocXRefSectType
from ..types.listing_type import ListingType
from .doc_title_cmd_group import DocTitleCmdGroup

@Collection('diafile', 'docImageType', {
    '/[@type={}': {
        'htmls': 'html',
        'latexes': 'latex',
        'docbooks': 'docbook',
        'rtfs': 'rtf',
    }
})
@Collection('dotfile', 'docImageType', {
    '/[@type={}': {
        'htmls': 'html',
        'latexes': 'latex',
        'docbooks': 'docbook',
        'rtfs': 'rtf',
    }
})
@Collection('mscfile', 'docImageType', {
    '/[@type={}': {
        'htmls': 'html',
        'latexes': 'latex',
        'docbooks': 'docbook',
        'rtfs': 'rtf',
    }
})
@Collection('parameterlist', 'docParamListType', {
    '/[@kind={}': {
        'params': 'param',
        'retvals': 'retval',
        'exceptions': 'exception',
        'templateparams': 'templateparam',
    }
})
@Collection('simplesect', 'docSimpleSectType', {
    '/[@kind={}': {
        'sees': 'see',
        'returns': 'return',
        'authors': 'author',
        'author': 'authors',
        'versions': 'version',
        'sinces': 'since',
        'dates': 'date',
        'notes': 'note',
        'warnings': 'warning',
        'pres': 'pre',
        'posts': 'post',
        'copyrights': 'copyright',
        'invariants': 'invariant',
        'remarks': 'remark',
        'attentions': 'attention',
        'pars': 'par',
        'rc': 'rcs',
    }
})
@Element('blockquote', 'docBlockQuoteType')
@Element('copydoc', 'docCopyType')
@Element('heading', 'docHeadingType')
@Element('indexentry', 'docIndexEntryType')
@Element('itemizedlist', 'docListType')
@Element('language', 'docLanguageType')
@Element('orderedlist', 'docListType')
@Element('parblock', 'docParBlockType')
@Element('preformatted', 'docMarkupType')
@Element('programlisting', 'listingType')
@Element('table', 'docTableType')
@Element('title', 'docTitleType')
@Element('toclist', 'docTocListType')
@Element('variablelist', 'docVariableListType')
@Element('verbatim', str)
@Element('xrefsect', 'docXRefSectType')
@Placeholders([
    'hruler'
])
class DocCmdGroup(DocTitleCmdGroup):
    """Model representation of a doxygen docCmdGroup group.

    Type XSD:

    <xsd:group xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="docCmdGroup">
        <xsd:choice>
          <xsd:group ref="docTitleCmdGroup" />
          <xsd:element name="hruler" type="docEmptyType" />
          <xsd:element name="preformatted" type="docMarkupType" />
          <xsd:element name="programlisting" type="listingType" />
          <xsd:element name="verbatim" type="xsd:string" />
          <xsd:element name="indexentry" type="docIndexEntryType" />
          <xsd:element name="orderedlist" type="docListType" />
          <xsd:element name="itemizedlist" type="docListType" />
          <xsd:element name="simplesect" type="docSimpleSectType" />
          <xsd:element name="title" type="docTitleType" />
          <xsd:element name="variablelist" type="docVariableListType" />
          <xsd:element name="table" type="docTableType" />
          <xsd:element name="heading" type="docHeadingType" />
          <xsd:element name="dotfile" type="docImageType" />
          <xsd:element name="mscfile" type="docImageType" />
          <xsd:element name="diafile" type="docImageType" />
          <xsd:element name="toclist" type="docTocListType" />
          <xsd:element name="language" type="docLanguageType" />
          <xsd:element name="parameterlist" type="docParamListType" />
          <xsd:element name="xrefsect" type="docXRefSectType" />
          <xsd:element name="copydoc" type="docCopyType" />
          <xsd:element name="blockquote" type="docBlockQuoteType" />
          <xsd:element name="parblock" type="docParBlockType" />
        </xsd:choice>
      </xsd:group>
    """


@Tag('blockquote')
class Blockquote(DocBlockQuoteType):
    """Model representation of a doxygen blockquote element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="blockquote" type="docBlockQuoteType" />
    """


@Tag('copydoc')
class Copydoc(DocCopyType):
    """Model representation of a doxygen copydoc element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="copydoc" type="docCopyType" />
    """


@Tag('diafile')
class Diafile(DocImageType):
    """Model representation of a doxygen diafile element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="diafile" type="docImageType" />
    """


@Tag('dotfile')
class Dotfile(DocImageType):
    """Model representation of a doxygen dotfile element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="dotfile" type="docImageType" />
    """


@Tag('heading')
class Heading(DocHeadingType):
    """Model representation of a doxygen heading element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="heading" type="docHeadingType" />
    """


@Tag('indexentry')
class Indexentry(DocIndexEntryType):
    """Model representation of a doxygen indexentry element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="indexentry" type="docIndexEntryType" />
    """


@Tag('itemizedlist')
class Itemizedlist(DocListType):
    """Model representation of a doxygen itemizedlist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="itemizedlist" type="docListType" />
    """


@Tag('language')
class Language(DocLanguageType):
    """Model representation of a doxygen language element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="language" type="docLanguageType" />
    """


@Tag('mscfile')
class Mscfile(DocImageType):
    """Model representation of a doxygen mscfile element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="mscfile" type="docImageType" />
    """


@Tag('orderedlist')
class Orderedlist(DocListType):
    """Model representation of a doxygen orderedlist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="orderedlist" type="docListType" />
    """


@Tag('parameterlist')
class Parameterlist(DocParamListType):
    """Model representation of a doxygen parameterlist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="parameterlist" type="docParamListType" />
    """


@Tag('parblock')
class Parblock(DocParBlockType):
    """Model representation of a doxygen parblock element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="parblock" type="docParBlockType" />
    """


@Tag('preformatted')
class Preformatted(DocMarkupType):
    """Model representation of a doxygen preformatted element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="preformatted" type="docMarkupType" />
    """


@Tag('programlisting')
class Programlisting(ListingType):
    """Model representation of a doxygen programlisting element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="programlisting" type="listingType" />
    """


@Tag('simplesect')
class Simplesect(DocSimpleSectType):
    """Model representation of a doxygen simplesect element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="simplesect" type="docSimpleSectType" />
    """


@Tag('table')
class Table(DocTableType):
    """Model representation of a doxygen table element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="table" type="docTableType" />
    """


@Tag('title')
class Title(DocTitleType):
    """Model representation of a doxygen title element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="title" type="docTitleType" />
    """


@Tag('toclist')
class Toclist(DocTocListType):
    """Model representation of a doxygen toclist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="toclist" type="docTocListType" />
    """


@Tag('variablelist')
class Variablelist(DocVariableListType):
    """Model representation of a doxygen variablelist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="variablelist" type="docVariableListType" />
    """


@Tag('xrefsect')
class Xrefsect(DocXRefSectType):
    """Model representation of a doxygen xrefsect element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="xrefsect" type="docXRefSectType" />
    """
