import modutil
mod, __getattr__ = modutil.lazy_import(__name__, {
  '.doc_cmd_group',
  '.doc_title_cmd_group',
  '.doc_variable_list_group'
})
