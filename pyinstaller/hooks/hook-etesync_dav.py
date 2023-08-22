from PyInstaller.utils.hooks import copy_metadata, collect_data_files, collect_submodules

datas = copy_metadata('webapp')
datas += collect_data_files('webapp')

hiddenimports = collect_submodules('pkg_resources')
