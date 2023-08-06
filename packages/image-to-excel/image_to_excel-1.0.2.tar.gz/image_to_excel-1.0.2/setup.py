# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['image_to_excel', 'image_to_excel._helpers', 'image_to_excel.core']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.5,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'pyyaml>=6.0,<7.0',
 'typeguard>=2.13.3,<3.0.0',
 'xlsxwriter>=3.0.3,<4.0.0']

entry_points = \
{'console_scripts': ['image_to_excel = image_to_excel:cli_main']}

setup_kwargs = {
    'name': 'image-to-excel',
    'version': '1.0.2',
    'description': 'A simple project to convert from an image to an excel file, because my brother wanted something that did this.',
    'long_description': '# image-to-excel\n\nA simple project to convert from an image to an excel file, because my brother wanted something that did this.\n\n## Installation\n\nTo install the project you only need to clone the repo and run pip install within the repo folder:\n\n```bash\npip install .\n```\n\nIf you like using virtual environments, you can easily install the project within one using [pipx](https://pypa.github.io/pipx/):\n\n```bash\npipx install .\n```\n\n## Usage\n\nYou can use image-to-excel as an importable module:\n\n```py\nfrom image_to_excel import BaseClass\nfrom pathlib import Path\n\napp = BaseClass("config.yml")\n\napp.image_to_excel(\n    Path("input.jpg"), 100, Path("output.xlsx")\n)\n```\n\nOr as a command line interface:\n\n```bash\n$ python3 -m image_to_excel\n# or\n$ image_to_excel -w 100 input.jpg output.xslx\n```\n\n## Documentation\n\nDocumentation for image-to-excel can be found within the docs folder.\n',
    'author': 'alex.fayers',
    'author_email': 'alex@fayers.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alexfayers/image-to-excel',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
