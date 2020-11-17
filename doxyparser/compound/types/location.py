from ...node import Node


class Location(Node):
    """
    Model representation of a location Element from doxygen

    <xsd:complexType name="locationType">
        <xsd:attribute name="file" type="xsd:string" />
        <xsd:attribute name="line" type="xsd:integer" />
        <xsd:attribute name="column" type="xsd:integer" use="optional"/>
        <xsd:attribute name="declfile" type="xsd:string" use="optional"/>
        <xsd:attribute name="declline" type="xsd:integer" use="optional"/>
        <xsd:attribute name="declcolumn" type="xsd:integer" use="optional"/>
        <xsd:attribute name="bodyfile" type="xsd:string" />
        <xsd:attribute name="bodystart" type="xsd:integer" />
        <xsd:attribute name="bodyend" type="xsd:integer" />
    </xsd:complexType>
    """

    def get_file(self):
        return self.get('file')
    
    def get_line(self):
        return self.get('line')
    
    def get_column(self):
        return self.get('column')
    
    def get_decl_file(self):
        return self.get('declfile')
    
    def get_decl_line(self):
        return self.get('declline')
    
    def get_decl_column(self):
        return self.get('declcolumn')
    
    def get_body_file(self):
        return self.get('bodyfile')
    
    def get_body_start(self):
        return self.get('bodystart')
    
    def get_body_end(self):
        return self.get('bodyend')
