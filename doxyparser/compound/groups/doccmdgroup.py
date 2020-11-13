"""
Model representation of a docCmdGroup type from doxygen

<xsd:group name="docCmdGroup">
  <xsd:choice>
    <xsd:group ref="docTitleCmdGroup"/>
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
from ...nodegroup import NodeGroup


class DocCmdGroup(NodeGroup):

    def get_hruler(self):
        return self.find('hruler') != None

    def get_preformatted(self):
        return self.get_child('preformatted', 'DocMarkup')

    def get_programlisting(self):
        return self.get_child('programlisting', 'Listing')

    def get_verbatim(self):
        return self.get_text('verbatim', '')

    def get_indexentry(self):
        return self.get_child('indexentry', 'DocIndexEntry')

    def get_orderedlist(self):
        return self.get_child('orderedlist', 'DocList')

    def get_itemizedlist(self):
        return self.get_child('itemizedlist', 'DocList')

    def get_simplesect(self):
        return self.get_child('simplesect', 'DocSimpleSect')

    def get_title(self):
        return self.get_child('title', 'DocTitle')

    def get_variablelist(self):
        return self.get_child('variablelist', 'DocVariableList')

    def get_table(self):
        return self.get_child('table', 'DocTable')

    def get_heading(self):
        return self.get_child('heading', 'DocHeading')

    def get_dotfile(self):
        return self.get_child('dotfile', 'DocImage')

    def get_mscfile(self):
        return self.get_child('mscfile', 'DocImage')

    def get_diafile(self):
        return self.get_child('diafile', 'DocImage')

    def get_toclist(self):
        return self.get_child('toc', 'DocTocList')

    def get_language(self):
        return self.get_child('language', 'DocLanguage')

    def get_parameterlist(self):
        return self.get_child('parameterlist', 'DocParamList')

    def get_xrefsect(self):
        return self.get_child('xrefsect', 'DocXRefSect')

    def get_copydoc(self):
        return self.get_child('copydoc', 'DocCopy')

    def get_blockquote(self):
        return self.get_child('blockquote', 'DocBlockQuote')

    def get_parblock(self):
        return self.get_child('parblock', 'DocParBlock')
