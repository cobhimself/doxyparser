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
from .doc_title_cmd_group import DocTitleCmdGroup

@collection('diafile', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('dotfile', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('mscfile', '/[@type={}]', {
    'htmls': 'html',
    'latexes': 'latex',
    'docbooks': 'docbook',
    'rtfs': 'rtf',
})
@collection('parameterlist', '/[@kind={}]', {
    'params': 'param',
    'retvals': 'retval',
    'exceptions': 'exception',
    'templateparams': 'templateparam',
})
@collection('simplesect', '/[@kind={}]', {
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
})
@element('blockquote', 'docBlockQuoteType')
@element('copydoc', 'docCopyType')
@element('heading', 'docHeadingType')
@element('indexentry', 'docIndexEntryType')
@element('itemizedlist', 'docListType')
@element('language', 'docLanguageType')
@element('orderedlist', 'docListType')
@element('parblock', 'docParBlockType')
@element('preformatted', 'docMarkupType')
@element('programlisting', 'listingType')
@element('table', 'docTableType')
@element('title', 'docTitleType')
@element('toclist', 'docTocListType')
@element('variablelist', 'docVariableListType')
@element('verbatim', 'simple')
@element('xrefsect', 'docXRefSectType')
@placeholders([
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
