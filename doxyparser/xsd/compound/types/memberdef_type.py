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
from ..types.description_type import DescriptionType
from ..types.enumvalue_type import EnumvalueType
from ..types.linked_text_type import LinkedTextType
from ..types.location_type import LocationType
from ..types.param_type import ParamType
from ..types.reference_type import ReferenceType
from ..types.reimplement_type import ReimplementType
from ..types.templateparamlist_type import TemplateparamlistType

@Attr('accessor', ['retain', 'copy', 'assign', 'weak', 'strong', 'unretained'])
@Attr('id', str)
@Attr('kind', ['define', 'property', 'event', 'variable', 'typedef', 'enum', 'function', 'signal', 'prototype', 'friend', 'dcop', 'slot', 'interface', 'service'])
@Attr('prot', ['public', 'protected', 'private', 'package'])
@Attr('refqual', ['lvalue', 'rvalue'])
@Attr('virt', ['non-virtual', 'virtual', 'pure-virtual'])
@BoolAttr('add')
@BoolAttr('attribute')
@BoolAttr('bound')
@BoolAttr('const')
@BoolAttr('constexpr')
@BoolAttr('constrained')
@BoolAttr('explicit')
@BoolAttr('final')
@BoolAttr('gettable')
@BoolAttr('initonly')
@BoolAttr('inline')
@BoolAttr('maybeambiguous')
@BoolAttr('maybedefault')
@BoolAttr('maybevoid')
@BoolAttr('mutable')
@BoolAttr('new')
@BoolAttr('noexcept')
@BoolAttr('optional')
@BoolAttr('privategettable')
@BoolAttr('privatesettable')
@BoolAttr('property')
@BoolAttr('protectedgettable')
@BoolAttr('protectedsettable')
@BoolAttr('raise')
@BoolAttr('readable')
@BoolAttr('readonly')
@BoolAttr('removable')
@BoolAttr('remove')
@BoolAttr('required')
@BoolAttr('sealed')
@BoolAttr('settable')
@BoolAttr('static')
@BoolAttr('strong')
@BoolAttr('transient')
@BoolAttr('volatile')
@BoolAttr('writable')
@Collection('enumvalue', 'enumvalueType', {
    '/[@prot={}': {
        'publics': 'public',
        'protecteds': 'protected',
        'privates': 'private',
        'packages': 'package',
    }
})
@Element('argsstring', 'any')
@Element('bitfield', 'any')
@Element('briefdescription', 'descriptionType')
@Element('definition', 'any')
@Element('detaileddescription', 'descriptionType')
@Element('exceptions', 'linkedTextType')
@Element('inbodydescription', 'descriptionType')
@Element('initializer', 'linkedTextType')
@Element('location', 'locationType')
@Element('name', 'any')
@Element('param', 'paramType')
@Element('read', 'any')
@Element('referencedby', 'referenceType')
@Element('references', 'referenceType')
@Element('reimplementedby', 'reimplementType')
@Element('reimplements', 'reimplementType')
@Element('templateparamlist', 'templateparamlistType')
@Element('type', 'linkedTextType')
@Element('write', 'any')
class MemberdefType(Node):
    """Model representation of a doxygen memberdefType type.

    Type XSD:

    <xsd:complexType xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="memberdefType">
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
        <xsd:attribute name="strong" type="DoxBool" use="optional" />
        <xsd:attribute name="const" type="DoxBool" use="optional" />
        <xsd:attribute name="explicit" type="DoxBool" use="optional" />
        <xsd:attribute name="inline" type="DoxBool" use="optional" />
        <xsd:attribute name="refqual" type="DoxRefQualifierKind" use="optional" />
        <xsd:attribute name="virt" type="DoxVirtualKind" use="optional" />
        <xsd:attribute name="volatile" type="DoxBool" use="optional" />
        <xsd:attribute name="mutable" type="DoxBool" use="optional" />
        <xsd:attribute name="noexcept" type="DoxBool" use="optional" />
        <xsd:attribute name="constexpr" type="DoxBool" use="optional" />

        <xsd:attribute name="readable" type="DoxBool" use="optional" />
        <xsd:attribute name="writable" type="DoxBool" use="optional" />

        <xsd:attribute name="initonly" type="DoxBool" use="optional" />

        <xsd:attribute name="settable" type="DoxBool" use="optional" />
        <xsd:attribute name="privatesettable" type="DoxBool" use="optional" />
        <xsd:attribute name="protectedsettable" type="DoxBool" use="optional" />
        <xsd:attribute name="gettable" type="DoxBool" use="optional" />
        <xsd:attribute name="privategettable" type="DoxBool" use="optional" />
        <xsd:attribute name="protectedgettable" type="DoxBool" use="optional" />

        <xsd:attribute name="final" type="DoxBool" use="optional" />
        <xsd:attribute name="sealed" type="DoxBool" use="optional" />
        <xsd:attribute name="new" type="DoxBool" use="optional" />

        <xsd:attribute name="add" type="DoxBool" use="optional" />
        <xsd:attribute name="remove" type="DoxBool" use="optional" />
        <xsd:attribute name="raise" type="DoxBool" use="optional" />

        <xsd:attribute name="optional" type="DoxBool" use="optional" />
        <xsd:attribute name="required" type="DoxBool" use="optional" />

        <xsd:attribute name="accessor" type="DoxAccessor" use="optional" />

        <xsd:attribute name="attribute" type="DoxBool" use="optional" />
        <xsd:attribute name="property" type="DoxBool" use="optional" />
        <xsd:attribute name="readonly" type="DoxBool" use="optional" />
        <xsd:attribute name="bound" type="DoxBool" use="optional" />
        <xsd:attribute name="removable" type="DoxBool" use="optional" />
        <xsd:attribute name="constrained" type="DoxBool" use="optional" />
        <xsd:attribute name="transient" type="DoxBool" use="optional" />
        <xsd:attribute name="maybevoid" type="DoxBool" use="optional" />
        <xsd:attribute name="maybedefault" type="DoxBool" use="optional" />
        <xsd:attribute name="maybeambiguous" type="DoxBool" use="optional" />

      </xsd:complexType>
    """


class Briefdescription(DescriptionType):
    """Model representation of a doxygen briefdescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="briefdescription" type="descriptionType" minOccurs="0" />
    """


class Detaileddescription(DescriptionType):
    """Model representation of a doxygen detaileddescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="detaileddescription" type="descriptionType" minOccurs="0" />
    """


class Enumvalue(EnumvalueType):
    """Model representation of a doxygen enumvalue element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="enumvalue" type="enumvalueType" minOccurs="0" maxOccurs="unbounded" />
    """


class Exceptions(LinkedTextType):
    """Model representation of a doxygen exceptions element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="exceptions" type="linkedTextType" minOccurs="0" />
    """


class Inbodydescription(DescriptionType):
    """Model representation of a doxygen inbodydescription element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="inbodydescription" type="descriptionType" minOccurs="0" />
    """


class Initializer(LinkedTextType):
    """Model representation of a doxygen initializer element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="initializer" type="linkedTextType" minOccurs="0" />
    """


class Location(LocationType):
    """Model representation of a doxygen location element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="location" type="locationType" />
    """


class Param(ParamType):
    """Model representation of a doxygen param element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="param" type="paramType" minOccurs="0" maxOccurs="unbounded" />
    """


class Referencedby(ReferenceType):
    """Model representation of a doxygen referencedby element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="referencedby" type="referenceType" minOccurs="0" maxOccurs="unbounded" />
    """


class References(ReferenceType):
    """Model representation of a doxygen references element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="references" type="referenceType" minOccurs="0" maxOccurs="unbounded" />
    """


class Reimplementedby(ReimplementType):
    """Model representation of a doxygen reimplementedby element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="reimplementedby" type="reimplementType" minOccurs="0" maxOccurs="unbounded" />
    """


class Reimplements(ReimplementType):
    """Model representation of a doxygen reimplements element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="reimplements" type="reimplementType" minOccurs="0" maxOccurs="unbounded" />
    """


class Templateparamlist(TemplateparamlistType):
    """Model representation of a doxygen templateparamlist element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="templateparamlist" type="templateparamlistType" minOccurs="0" />
    """


class Type(LinkedTextType):
    """Model representation of a doxygen type element.

    Type XSD:

    <xsd:element xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="type" type="linkedTextType" minOccurs="0" />
    """
