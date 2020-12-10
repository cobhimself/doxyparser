# This class has been auto-generated. To add/modify
# functionality, extend it.
from ...node import Node

@attr('id')
@boolattr('add')
@boolattr('attribute')
@boolattr('bound')
@boolattr('const')
@boolattr('constexpr')
@boolattr('constrained')
@boolattr('explicit')
@boolattr('final')
@boolattr('gettable')
@boolattr('initonly')
@boolattr('inline')
@boolattr('maybeambiguous')
@boolattr('maybedefault')
@boolattr('maybevoid')
@boolattr('mutable')
@boolattr('new')
@boolattr('noexcept')
@boolattr('optional')
@boolattr('privategettable')
@boolattr('privatesettable')
@boolattr('property')
@boolattr('protectedgettable')
@boolattr('protectedsettable')
@boolattr('raise')
@boolattr('readable')
@boolattr('readonly')
@boolattr('removable')
@boolattr('remove')
@boolattr('required')
@boolattr('sealed')
@boolattr('settable')
@boolattr('static')
@boolattr('strong')
@boolattr('transient')
@boolattr('volatile')
@boolattr('writable')
@collection('enumvalue', '/[@prot={}]', {
    'publics': 'public',
    'protecteds': 'protected',
    'privates': 'private',
    'packages': 'package',
})
@element('argsstring', 'any')
@element('bitfield', 'any')
@element('briefdescription', 'descriptionType')
@element('definition', 'any')
@element('detaileddescription', 'descriptionType')
@element('exceptions', 'linkedTextType')
@element('inbodydescription', 'descriptionType')
@element('initializer', 'linkedTextType')
@element('location', 'locationType')
@element('name', 'any')
@element('param', 'paramType')
@element('read', 'any')
@element('referencedby', 'referenceType')
@element('references', 'referenceType')
@element('reimplementedby', 'reimplementType')
@element('reimplements', 'reimplementType')
@element('templateparamlist', 'templateparamlistType')
@element('type', 'linkedTextType')
@element('write', 'any')
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
