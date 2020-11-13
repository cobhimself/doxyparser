from doxyparser.loader import Loader
from . import helper
import pytest
from xml.etree.ElementTree import ElementTree
from doxyparser.index.types.compound import Compound

loader = Loader(helper.get_doxygen_build_dir())


def test_load_index():
    index = loader.load_index()
    assert type(index) == ElementTree
    assert index.getroot().tag == 'doxygenindex'


def test_load_tag_class():
    compound = loader.load_tag_class('index', 'compound')

    assert compound == Compound


def test_load_refid():
    tree = loader.load_refid('namespace_src')
    assert type(tree) == ElementTree


def test_exception_on_unknown_xsd():
    with pytest.raises(Exception) as execinfo:
        loader.load_tag_class('bad', 'tag')

    assert "Unknown doxyparser xsd" in str(execinfo.value)


def test_exception_on_unknown_tag():
    with pytest.raises(Exception) as execinfo:
        loader.load_tag_class('index', 'bad')

    assert "No class mapping for tag" in str(execinfo.value)
