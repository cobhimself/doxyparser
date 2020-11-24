from ... import helper
import pytest

# Expectations for the compounddef type. They pertain to namespace_src.xml
# doxygen file. We want the data from inside 'compound'
_dp_compounddef_expectations1 = helper.get_data_provider(
    'test_compounddef1.yml', 'compounddef'
)
doxygen = helper.get_parser().parse_ref_id('namespace_src')


@pytest.mark.parametrize("node_getter,expectations", _dp_compounddef_expectations1)
def test_namespace_src(node_getter: str, expectations: list):
    helper.confirm_node_expectations(doxygen, node_getter, expectations)

# More expectations for the compounddef type. They pertain to
# class_src_1_1_more_1_1_deep_class.xml doxygen file. We want the data from
# inside 'compound'
_dp_compounddef_expectations2 = helper.get_data_provider(
    'test_compounddef2.yml', 'compounddef'
)
doxygen = helper.get_parser().parse_ref_id('class_src_1_1_more_1_1_deep_class')


@pytest.mark.parametrize("node_getter,expectations", _dp_compounddef_expectations2)
def test_deep_class(node_getter: str, expectations: list):
    helper.confirm_node_expectations(doxygen, node_getter, expectations)


def test_get_version():
    assert doxygen.get_version() == "1.8.20"
