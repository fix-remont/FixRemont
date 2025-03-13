export default {
  '*.{js,ts,css,md,json,vue}': [
    'prettier --plugin-search-dir . --write .',
    'prettier --check --plugin-search-dir=.'
  ]
}