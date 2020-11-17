from ... import helper
import pytest

# Expectations for the compounddef type. They pertain to namespace_src.xml
# doxygen file. We want the data from inside 'compound'
_dp_compounddef_expectations = helper.get_data_provider(
    'test_compounddef.yml', 'compounddef'
)
doxygen = helper.get_parser().parse_ref_id('namespace_src')


@pytest.mark.parametrize("node_getter,expectations", _dp_compounddef_expectations)
def test_index_parser(node_getter: str, expectations: list):
    helper.confirm_node_expectations(doxygen, node_getter, expectations)


def test_get_version():
    assert doxygen.get_version() == "1.8.20"
