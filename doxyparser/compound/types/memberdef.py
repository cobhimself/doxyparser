#!/usr/bin/env python3
"""
Model representation of a memberdef Element from doxygen

<xsd:complexType name="memberdefType">
<xsd:sequence>
    <xsd:element name="templateparamlist" type="templateparamlistType" minOccurs="0" />
    <xsd:element name="type" type="linkedTextType" minOccurs="0" />
    <xsd:element name="definition" minOccurs="0" />
    <xsd:element name="argsstring" minOccurs="0" />
    <xsd:element name="name" />
    <xsd:element name="read" minOccurs="0" />
    <xsd:element name="write" minOccurs="0" />
    <xsd:element name="bitfield" minOccurs="0" />
    <xsd:element name="reimplements" type="reimplementType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="reimplementedby" type="reimplementType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="param" type="paramType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="enumvalue" type="enumvalueType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="initializer" type="linkedTextType" minOccurs="0" />
    <xsd:element name="exceptions" type="linkedTextType" minOccurs="0" />
    <xsd:element name="briefdescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="detaileddescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="inbodydescription" type="descriptionType" minOccurs="0" />
    <xsd:element name="location" type="locationType" />
    <xsd:element name="references" type="referenceType" minOccurs="0" maxOccurs="unbounded" />
    <xsd:element name="referencedby" type="referenceType" minOccurs="0" maxOccurs="unbounded" />
</xsd:sequence>
<xsd:attribute name="kind" type="DoxMemberKind" />
<xsd:attribute name="id" type="xsd:string" />
<xsd:attribute name="prot" type="DoxProtectionKind" />
<xsd:attribute name="static" type="DoxBool" />
<xsd:attribute name="strong" type="DoxBool" use="optional"/>
<xsd:attribute name="const" type="DoxBool" use="optional"/>
<xsd:attribute name="explicit" type="DoxBool" use="optional"/>
<xsd:attribute name="inline" type="DoxBool" use="optional"/>
<xsd:attribute name="refqual" type="DoxRefQualifierKind" use="optional"/>
<xsd:attribute name="virt" type="DoxVirtualKind" use="optional"/>
<xsd:attribute name="volatile" type="DoxBool" use="optional"/>
<xsd:attribute name="mutable" type="DoxBool" use="optional"/>
<xsd:attribute name="noexcept" type="DoxBool" use="optional"/>
<xsd:attribute name="constexpr" type="DoxBool" use="optional"/>
<!-- Qt property -->
<xsd:attribute name="readable" type="DoxBool" use="optional"/>
<xsd:attribute name="writable" type="DoxBool" use="optional"/>
<!-- C++/CLI variable -->
<xsd:attribute name="initonly" type="DoxBool" use="optional"/>
<!-- C++/CLI and C# property -->
<xsd:attribute name="settable" type="DoxBool" use="optional"/>
<xsd:attribute name="privatesettable" type="DoxBool" use="optional"/>
<xsd:attribute name="protectedsettable" type="DoxBool" use="optional"/>
<xsd:attribute name="gettable" type="DoxBool" use="optional"/>
<xsd:attribute name="privategettable" type="DoxBool" use="optional"/>
<xsd:attribute name="protectedgettable" type="DoxBool" use="optional"/>
<!-- C++/CLI function -->
<xsd:attribute name="final" type="DoxBool" use="optional"/>
<xsd:attribute name="sealed" type="DoxBool" use="optional"/>
<xsd:attribute name="new" type="DoxBool" use="optional"/>
<!-- C++/CLI event -->
<xsd:attribute name="add" type="DoxBool" use="optional"/>
<xsd:attribute name="remove" type="DoxBool" use="optional"/>
<xsd:attribute name="raise" type="DoxBool" use="optional"/>
<!-- Objective-C 2.0 protocol method -->
<xsd:attribute name="optional" type="DoxBool" use="optional"/>
<xsd:attribute name="required" type="DoxBool" use="optional"/>
<!-- Objective-C 2.0 property accessor -->
<xsd:attribute name="accessor" type="DoxAccessor" use="optional"/>
<!-- UNO IDL -->
<xsd:attribute name="attribute" type="DoxBool" use="optional"/>
<xsd:attribute name="property" type="DoxBool" use="optional"/>
<xsd:attribute name="readonly" type="DoxBool" use="optional"/>
<xsd:attribute name="bound" type="DoxBool" use="optional"/>
<xsd:attribute name="removable" type="DoxBool" use="optional"/>
<xsd:attribute name="constrained" type="DoxBool" use="optional"/>
<xsd:attribute name="transient" type="DoxBool" use="optional"/>
<xsd:attribute name="maybevoid" type="DoxBool" use="optional"/>
<xsd:attribute name="maybedefault" type="DoxBool" use="optional"/>
<xsd:attribute name="maybeambiguous" type="DoxBool" use="optional"/>

</xsd:complexType>
"""
from ...node import Node

class MemberDef(Node):
    def __init__(self, node, parser):
        super.__init__(node, parser, 'memberdef')
    
    def get_kind(self):
        return self.get('kind')
    
    def get_id(self):
        return self.get('id')
    
    def get_prot(self):
        return self.get('prot')
    
    def is_static(self):
        return self.get_bool(self.get('static'))
    
    def is_strong(self):
        return self.get_bool('strong')
    
    def is_const(self):
        return self.get_bool('const')

    def is_explicit(self):
        return self.get_bool('explicit')
    
    def is_inline(self):
        return self.get_bool('inline')
    
    def get_refqual(self):
        return self.get('refqual')
    
    def get_virt(self):
        return self.get('virt')
    
    def get_template_param_list(self):
        return self.get_child('templateparamlist', 'templateparamlist')
    
    def get_type(self):
        return self.get_child('type', 'linkedtext')
    
    def get_definition(self):
        return self.get_text('definition', '')
    
    def get_args_string(self):
        return self.get_text('argsstring', '')
    
    def get_name(self):
        return self.get_text('name')
    
    def get_read(self):
        return self.get_text('read')
    
    def get_write(self):
        return self.get_text('write')
    
    def get_reimplements(self):
        return self.get_children('reimplements', 'Reimplement')
    
    def get_reimplemented_by(self):
        return self.get_children('reimplementedby', 'Reimplement')
    
    def get_params(self):
        return self.get_children('param', 'Param')

    def get_enum_value(self):
        return self.get_children('enumvalue', 'EnumValue')

    def get_initializer(self):
        return self.get_child('initializer', 'LinkedText')
    
    def get_exceptions(self):
        return self.get_child('exceptions', 'LinkedText')

    def get_brief_description(self):
        return self.get_child('briefdescription', 'Description')

    def get_detailed_description(self):
        return self.get_child('detaileddescription', 'Description')

    def get_inbody_description(self):
        return self.get_children('inbodydescription', 'DescriptionType')

    def get_location(self):
        return self.get_child('location', 'Location')

    def get_references(self):
        return self.get_children('references', 'Reference')

    def get_referencedby(self):
        return self.get_children('referencedby', 'Reference')