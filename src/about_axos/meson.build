pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'about_axos')
gnome = import('gnome')

gnome.compile_resources('about_axos',
  'about_axos.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'about_axos.in',
  output: 'about_axos',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

about_axos_sources = [
  'main.py',
]

install_data(about_axos_sources, install_dir: moduledir)
