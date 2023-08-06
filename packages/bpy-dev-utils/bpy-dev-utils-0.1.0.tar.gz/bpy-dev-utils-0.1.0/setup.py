# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bpydevutil', 'bpydevutil.functions']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.5.1,<13.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['bpy = bpydevutil.main:app']}

setup_kwargs = {
    'name': 'bpy-dev-utils',
    'version': '0.1.0',
    'description': 'This is a personal collection of simple CLI utilities that I made to help my development of Blender addons.',
    'long_description': '\n## BPY Dev Utilities\n\nThis is a personal collection of simple CLI utilities that I made to help my development of Blender addons.\n\n### Installation\n```shell\npip install bpy-dev-utils\n```\n#### OR\n```shell\npoetry add bpy-dev-utils\n```\n\n## Install Tool\n```sh\nbpy install <src-dir> <blender-addons-dir>\n```\nInstalls addons directly from their source files into the specified Blender addons installation directory.\n#### Arguments:\n- src-dir: Directory where addon sources are located. eg ```MyProject\\src```\n- blender-addons-dir: Blender addon installation directory. eg ```\\Blender\\3.2\\scripts\\addons```\n\n#### Options:\n- --excluded-addons: Addon names to be excluded from installation. eg ```["Addon1", "Addon2"]```\n- --remove-suffixes: File types to be deleted before installation. eg ```[".pyc", ".txt"]```\n- --blender-exe: Path to blender exe. eg ```\\Blender\\blender.exe```\n- --reload-blender: Load blender and enable addons, requires --blender-exe to be set. eg ```True```\n- --help: Show help.\n\n## Symlink Tool\n```sh\nbpy symlink <src-dir> <blender-addons-dir>\n```\nCreates symlinks to the addon source in the specified Blender addons installation directory. Requires either symlink creation privileges, either through running as admin or security policy.\n#### Arguments:\n- src-dir: Directory where addon sources are located. eg ```MyProject\\src```\n- blender-addons-dir: Blender addon installation directory. eg ```\\Blender\\3.2\\scripts\\addons```\n\n#### Options:\n- --excluded-addons: Addon names to be excluded from symlink creation. eg ```["Addon1", "Addon2"]```\n- --remove-suffixes: File types to be deleted before symlink creation. eg ```[".pyc", ".txt"]```\n- --blender-exe: Path to blender exe. eg ```\\Blender\\blender.exe```\n- --reload-blender: Load blender and enable addons, requires --blender-exe to be set. eg ```True```\n- --help: Show help.\n\n## Packing Tool\n\n```sh\nbpy pack <src-dir> <release-dir>\n```\nPacks addons into ZIP files and automatically names them based on data extracted from the addon bl_info dictionary.<br>\nExample resulting name: `My Addon (v1.0.0).zip`\n#### Arguments:\n- src-dir: Directory where addon sources are located. eg ```MyProject\\src```\n- output-dir: Directory where the archive should be built. eg ```MyProject\\releases```\n\n#### Options:\n- --excluded-addons: Addon names to be excluded from packing. eg ```Addon1, Addon2```\n- --remove-suffixes: File types to be deleted before packing. eg ```.pyc, .txt```\n- --help: Show help.\n\n## Config File\n\nAll arguments and options can be specified in a ```pyproject.toml``` file, the script looks for this file in the current working directory.\n\n```toml\n[tool.bpydevutil]\nblender-addons-dir = "Blender\\\\3.2\\\\scripts\\\\addons"\nsrc-dir = "blender-addons\\\\my-addon\\\\src"\noutput-dir = "blender-addons\\\\my-addon\\\\output"\nremove-suffixes = [".pyc", ".txt"]\nblender-exe = "Blender\\\\blender.exe"\nreload-blender = true\n```\n',
    'author': 'Matt Ashpole',
    'author_email': 'm.d.ashpole@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
