from doxyparser.index.types.compound import Compound
from ... import helper
import pytest

_dp_compound_expectations = helper.get_data_provider('test_index.yml', 'compound')

@pytest.mark.parametrize("method,expectations", _dp_compound_expectations)
def test_index_parser(method: str, expectations: list):
    parser = helper.get_parser()
    doxygen = parser.parse_index()
    helper.confirm_node_expectations(doxygen, method, expectations)