
import xml.etree.ElementTree as ET
from doxyparser.index.types.doxygen import Doxygen

class Parser:
  def __init__(self, xml_dir):
    self._xml_dir = xml_dir

  def parse_index(self):
    tree = ET.parse(self._xml_dir + '/index.xml')
    return Doxygen(tree.getroot())
