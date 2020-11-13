from doxyparser.loader import Loader
from doxyparser.index.types.compound import Compound
from doxyparser.parser import Parser
from doxyparser.index.types.doxygenindex import DoxygenIndex
from doxyparser.compound.types.doxygen import Doxygen
from . import helper

from xml.etree.ElementTree import ElementTree
import pytest

loader = Loader(helper.get_doxygen_build_dir())
parser = Parser(loader)


def test_parse_index():
    index = parser.parse_index()
    assert type(index) == DoxygenIndex


def test_parser_refid():
    node = parser.parser_ref_id('namespace_src')
    assert type(node) == Doxygen
