from ... import helper
import pytest

doxygen = helper.get_parser().parse_ref_id('namespace_src')

def test_doxygen():
    compounddefs = doxygen.get_compounddefs()
    assert len(compounddefs) == 1


def test_get_version():
    assert doxygen.get_version() == "1.8.20"
