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
from ....node import Node
from ....decorators import boolattr, attr, collection, element

@attr('id')
@boolattr('abstract')
@boolattr('final')
@boolattr('inline')
@boolattr('sealed')
@collection('basecompoundref', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('basecompoundref', '/[@virt={}]', {
    'non_virtuals': 'non-virtual',
    'virtuals': 'virtual',
    'pure_virtuals': 'pure-virtual',
})
@collection('derivedcompoundref', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('derivedcompoundref', '/[@virt={}]', {
    'non_virtuals': 'non-virtual',
    'virtuals': 'virtual',
    'pure_virtuals': 'pure-virtual',
})
@collection('innerclass', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('innerdir', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('innerfile', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('innergroup', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('innernamespace', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('innerpage', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@collection('sectiondef', '/[@kind={}]', {
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
})
@element('briefdescription', 'descriptionType')
@element('collaborationgraph', 'graphType')
@element('compoundname', 'simple')
@element('detaileddescription', 'descriptionType')
@element('incdepgraph', 'graphType')
@element('includedby', 'incType')
@element('includes', 'incType')
@element('inheritancegraph', 'graphType')
@element('invincdepgraph', 'graphType')
@element('listofallmembers', 'listofallmembersType')
@element('location', 'locationType')
@element('programlisting', 'listingType')
@element('tableofcontents', 'tableofcontentsType')
@element('templateparamlist', 'templateparamlistType')
@element('title', 'simple')
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
