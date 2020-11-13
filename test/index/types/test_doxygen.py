from ... import helper
import pytest

# Expectations for our parsing of the index.xml doxygen file. We want the data
# from inside 'compound'
_dp_compound_expectations = helper.get_data_provider('test_index.yml', 'compound')
doxygen = helper.get_parser().parse_index()

@pytest.mark.parametrize("node_getter,expectations", _dp_compound_expectations)
def test_index_parser(node_getter: str, expectations: list):
    helper.confirm_node_expectations(doxygen, node_getter, expectations)

def test_get_version():
    assert doxygen.get_version() == "1.8.20"
    
