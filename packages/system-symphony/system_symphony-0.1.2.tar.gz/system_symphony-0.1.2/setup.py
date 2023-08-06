# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['process_parser', 'supercollider']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'psutil>=5.9.4,<6.0.0', 'python-osc>=1.8.0,<2.0.0']

entry_points = \
{'console_scripts': ['system-symphony = process_parser.main:main']}

setup_kwargs = {
    'name': 'system-symphony',
    'version': '0.1.2',
    'description': 'Explore the sonic world of your computer.',
    'long_description': '# system-symphony\nexplore the sonic world of your computer\n\n## Installation\n### Preqrequisites\n1. Install [Supercollider](https://supercollider.github.io/downloads) on your current platform.\n2. Make sure `sclang` is added to system PATH.\n3. Install `system-symphony` locally or through pypi as directed below.\n### Installing Locally\n1. Run `pip install .` in `src/system-symphony` directory\n\n\n### Installing through pypi\n1. Run `pip install system-symphony`\n\n## Usage\n\n```\nUsage: system-symphony [OPTIONS]\n\n  Explore the sonic world of your computer. Associated supercollider file must\n  be running.\n\nOptions:\n  --poll-rate INTEGER  How fast to poll processes in ms\n  --no-sc              Do not launch the supercollider process.\n  --help               Show this message and exit.\n\n```',
    'author': 'Darwin',
    'author_email': 'darwin78913@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dsmaugy/the-sounds-of-processes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
