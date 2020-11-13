#!/usr/bin/env python3
"""
Model representation of a compound def Element from doxygen

<xsd:complexType name="compounddefType">
<xsd:sequence>
    <xsd:element name="compoundname" type="xsd:string"/>
    <xsd:element name="title" type="xsd:string" minOccurs="0" />
    <xsd:element name="basecompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="derivedcompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="includes" type="incType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="includedby" type="incType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="incdepgraph" type="graphType" minOccurs="0" />
    <xsd:element name="invincdepgraph" type="graphType" minOccurs="0" />
    <xsd:element name="innerdir" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="innerfile" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="innerclass" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="innernamespace" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="innerpage" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="innergroup" type="refType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="templateparamlist" type="templateparamlistType" minOccurs="0" />
    <xsd:element name="sectiondef" type="sectiondefType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="tableofcontents" type="tableofcontentsType" minOccurs="0" maxOccurs="1" />
    <xsd:element name="briefdescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="detaileddescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="inheritancegraph" type="graphType" minOccurs="0" />
    <xsd:element name="collaborationgraph" type="graphType" minOccurs="0" />
    <xsd:element name="programlisting" type="listingType" minOccurs="0" />
    <xsd:element name="location" type="locationType" minOccurs="0" />
    <xsd:element name="listofallmembers" type="listofallmembersType" minOccurs="0" />
</xsd:sequence>
<xsd:attribute name="id" type="xsd:string" />
<xsd:attribute name="kind" type="DoxCompoundKind" />
<xsd:attribute name="language" type="DoxLanguage" use="optional"/>
<xsd:attribute name="prot" type="DoxProtectionKind" />
<xsd:attribute name="final" type="DoxBool" use="optional"/>
<xsd:attribute name="inline" type="DoxBool" use="optional"/>
<xsd:attribute name="sealed" type="DoxBool" use="optional"/>
<xsd:attribute name="abstract" type="DoxBool" use="optional"/>
</xsd:complexType>
"""
from ...node import Node

class CompoundDef(Node):
    def __init__(self, node, parser):
        super.__init__(node, parser, 'compounddef')
        self._elements = {
            
        }
    
    def get_id(self):
        return self.get('id')
    
    def get_kind(self):
        return self.get('kind')
    
    def get_language(self):
        return self.get('language')
    
    def get_prot(self):
        return self.get('prot')

    def is_final(self):
        return self.get_bool('final')
    
    def is_inline(self):
        return self.get_bool('inline')
    
    def is_sealed(self):
        return self.get_bool('sealed')
    
    def is_abstract(self):
        return self.get_bool('abstract')
    
    def get_compound_name(self):
        return self.find('compoundname', '')

    def get_title(self):
        return self.find('compoundname', '')
    
    def get_base_compound_refs(self):
        return self.get_children('basecompoundref', 'CompoundRef')

    def get_derived_compound_refs(self):
        return self.get_children('derivedcompoundref', 'CompoundRef')

    def get_includes(self):
        return self.get_children('includes', 'Inc')

    def get_included_by(self):
        return self.get_children('includedby', 'Inc')
    
    def get_inner_dirs(self):
        return self.get_children('innerdir', 'Ref')
    
    def get_inner_files(self):
        return self.get_children('innerfile', 'Ref')

    def get_inner_classes(self):
        return self.get_children('innerclass', 'Ref')

    def get_inner_namespaces(self):
        return self.get_children('innernamespace', 'Ref')

    def get_inner_pages(self):
        return self.get_children('innerpage', 'Ref')

    def get_inner_groups(self):
        return self.get_children('innergroup', 'Ref')

    def get_section_def(self):
        return self.get_children('sectiondef', 'SectionDef')
