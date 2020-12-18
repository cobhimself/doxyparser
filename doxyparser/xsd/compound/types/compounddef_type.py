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

from ....decorators.attr import Attr
from ....decorators.boolattr import BoolAttr
from ....decorators.collection import Collection
from ....decorators.element import Element
from ....node import Node
from ..types.compound_ref_type import CompoundRefType
from ..types.description_type import DescriptionType
from ..types.graph_type import GraphType
from ..types.inc_type import IncType
from ..types.listing_type import ListingType
from ..types.listofallmembers_type import ListofallmembersType
from ..types.location_type import LocationType
from ..types.ref_type import RefType
from ..types.sectiondef_type import SectiondefType
from ..types.tableofcontents_type import TableofcontentsType
from ..types.templateparamlist_type import TemplateparamlistType

@Attr('id', str)
@Attr('kind', ['class', 'struct', 'union', 'interface', 'protocol', 'category', 'exception', 'service', 'singleton', 'module', 'type', 'file', 'namespace', 'group', 'page', 'example', 'dir'])
@Attr('language', ['Unknown', 'IDL', 'Java', 'C#', 'D', 'PHP', 'Objective-C', 'C++', 'JavaScript', 'Python', 'Fortran', 'VHDL', 'XML', 'SQL', 'Markdown'])
@Attr('prot', ['public', 'protected', 'private', 'package'])
@BoolAttr('abstract')
@BoolAttr('final')
@BoolAttr('inline')
@BoolAttr('sealed')
@Collection('basecompoundref', 'compoundRefType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    },
    '/[@virt={}': {
        'non_virtuals': 'non-virtual',
        'virtuals': 'virtual',
        'pure_virtuals': 'pure-virtual',
    }
})
@Collection('derivedcompoundref', 'compoundRefType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    },
    '/[@virt={}': {
        'non_virtuals': 'non-virtual',
        'virtuals': 'virtual',
        'pure_virtuals': 'pure-virtual',
    }
})
@Collection('innerclass', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('innerdir', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('innerfile', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('innergroup', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('innernamespace', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('innerpage', 'refType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Collection('sectiondef', 'sectiondefType', {
    '/[@kind={}': {
        'user_defineds': 'user-defined',
        'public_types': 'public-type',
        'public_funcs': 'public-func',
        'public_attribs': 'public-attrib',
        'public_slots': 'public-slot',
        'signals': 'signal',
        'dcop_funcs': 'dcop-func',
        'properties': 'property',
        'events': 'event',
        'public_static_funcs': 'public-static-func',
        'public_static_attribs': 'public-static-attrib',
        'protected_types': 'protected-type',
        'protected_funcs': 'protected-func',
        'protected_attribs': 'protected-attrib',
        'protected_slots': 'protected-slot',
        'protected_static_funcs': 'protected-static-func',
        'protected_static_attribs': 'protected-static-attrib',
        'package_types': 'package-type',
        'package_funcs': 'package-func',
        'package_attribs': 'package-attrib',
        'package_static_funcs': 'package-static-func',
        'package_static_attribs': 'package-static-attrib',
        'private_types': 'private-type',
        'private_funcs': 'private-func',
        'private_attribs': 'private-attrib',
        'private_slots': 'private-slot',
        'private_static_funcs': 'private-static-func',
        'private_static_attribs': 'private-static-attrib',
        'friends': 'friend',
        'relateds': 'related',
        'defines': 'define',
        'prototypes': 'prototype',
        'typedefs': 'typedef',
        'enums': 'enum',
        'funcs': 'func',
        'vars': 'var',
    }
})
@Element('briefdescription', 'descriptionType')
@Element('collaborationgraph', 'graphType')
@Element('compoundname', str)
@Element('detaileddescription', 'descriptionType')
@Element('incdepgraph', 'graphType')
@Element('includedby', 'incType')
@Element('includes', 'incType')
@Element('inheritancegraph', 'graphType')
@Element('invincdepgraph', 'graphType')
@Element('listofallmembers', 'listofallmembersType')
@Element('location', 'locationType')
@Element('programlisting', 'listingType')
@Element('tableofcontents', 'tableofcontentsType')
@Element('templateparamlist', 'templateparamlistType')
@Element('title', str)
class CompounddefType(Node):
    """Model representation of a doxygen compounddefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="compounddefType">
        <xsd:sequence>
          <xsd:element name="compoundname" type="xsd:string" />
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
        <xsd:attribute name="language" type="DoxLanguage" use="optional" />
        <xsd:attribute name="prot" type="DoxProtectionKind" />
        <xsd:attribute name="final" type="DoxBool" use="optional" />
        <xsd:attribute name="inline" type="DoxBool" use="optional" />
        <xsd:attribute name="sealed" type="DoxBool" use="optional" />
        <xsd:attribute name="abstract" type="DoxBool" use="optional" />
      </xsd:complexType>
    """


class Basecompoundref(CompoundRefType):
    """Model representation of a doxygen basecompoundref element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="basecompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    """


class Briefdescription(DescriptionType):
    """Model representation of a doxygen briefdescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="briefdescription" type="descriptionType" minOccurs="0" />
    """


class Collaborationgraph(GraphType):
    """Model representation of a doxygen collaborationgraph element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="collaborationgraph" type="graphType" minOccurs="0" />
    """


class Derivedcompoundref(CompoundRefType):
    """Model representation of a doxygen derivedcompoundref element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="derivedcompoundref" type="compoundRefType" minOccurs="0" maxOccurs="unbounded" />
    """


class Detaileddescription(DescriptionType):
    """Model representation of a doxygen detaileddescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="detaileddescription" type="descriptionType" minOccurs="0" />
    """


class Incdepgraph(GraphType):
    """Model representation of a doxygen incdepgraph element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="incdepgraph" type="graphType" minOccurs="0" />
    """


class Includedby(IncType):
    """Model representation of a doxygen includedby element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="includedby" type="incType" minOccurs="0" maxOccurs="unbounded" />
    """


class Includes(IncType):
    """Model representation of a doxygen includes element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="includes" type="incType" minOccurs="0" maxOccurs="unbounded" />
    """


class Inheritancegraph(GraphType):
    """Model representation of a doxygen inheritancegraph element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="inheritancegraph" type="graphType" minOccurs="0" />
    """


class Innerclass(RefType):
    """Model representation of a doxygen innerclass element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innerclass" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Innerdir(RefType):
    """Model representation of a doxygen innerdir element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innerdir" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Innerfile(RefType):
    """Model representation of a doxygen innerfile element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innerfile" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Innergroup(RefType):
    """Model representation of a doxygen innergroup element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innergroup" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Innernamespace(RefType):
    """Model representation of a doxygen innernamespace element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innernamespace" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Innerpage(RefType):
    """Model representation of a doxygen innerpage element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="innerpage" type="refType" minOccurs="0" maxOccurs="unbounded" />
    """


class Invincdepgraph(GraphType):
    """Model representation of a doxygen invincdepgraph element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="invincdepgraph" type="graphType" minOccurs="0" />
    """


class Listofallmembers(ListofallmembersType):
    """Model representation of a doxygen listofallmembers element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="listofallmembers" type="listofallmembersType" minOccurs="0" />
    """


class Location(LocationType):
    """Model representation of a doxygen location element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="location" type="locationType" minOccurs="0" />
    """


class Programlisting(ListingType):
    """Model representation of a doxygen programlisting element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="programlisting" type="listingType" minOccurs="0" />
    """


class Sectiondef(SectiondefType):
    """Model representation of a doxygen sectiondef element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="sectiondef" type="sectiondefType" minOccurs="0" maxOccurs="unbounded" />
    """


class Tableofcontents(TableofcontentsType):
    """Model representation of a doxygen tableofcontents element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="tableofcontents" type="tableofcontentsType" minOccurs="0" maxOccurs="1" />
    """


class Templateparamlist(TemplateparamlistType):
    """Model representation of a doxygen templateparamlist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="templateparamlist" type="templateparamlistType" minOccurs="0" />
    """
