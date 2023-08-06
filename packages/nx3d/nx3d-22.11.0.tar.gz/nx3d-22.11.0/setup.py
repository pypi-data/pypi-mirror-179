# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nx3d', 'nx3d.examples']

package_data = \
{'': ['*']}

install_requires = \
['Panda3D>=1.10,<2.0',
 'loguru>=0.6.0,<0.7.0',
 'networkx>=2.8,<3.0',
 'numpy>=1.23,<2.0',
 'pyvista>=0.36.1,<0.37.0']

setup_kwargs = {
    'name': 'nx3d',
    'version': '22.11.0',
    'description': 'A 3D plotting library for networkx',
    'long_description': '# nx3d\n\n[![-missing homepage-](https://img.shields.io/badge/home-GitHub-blueviolet)](https://github.com/ekalosak/nx3d)\n[![-missing docs-](https://img.shields.io/badge/docs-ReadTheDocs-blue)](https://nx3d.readthedocs.io/en/latest/)\n[![-missing pypi-](https://img.shields.io/pypi/v/nx3d)](https://pypi.org/project/nx3d/)\n[![-missing build status-](https://img.shields.io/github/workflow/status/ekalosak/nx3d/Build%20nx3d%20and%20publish%20to%20PyPi)](https://github.com/ekalosak/nx3d/actions)\n\n[![-missing project maturity-](https://img.shields.io/badge/status-experimental-green)](https://nx3d.readthedocs.io/en/latest/maturity.html)\n[![-missing download count-](https://img.shields.io/pypi/dw/nx3d)](https://pypistats.org/packages/nx3d)\n\nA 3D plotting library for `networkx` built on `panda3d`.\n\n![-missing gif of frucht graph-](https://raw.githubusercontent.com/ekalosak/nx3d/main/docs/data/frucht_thin.gif)\n\n# Installation\n```sh\npip install nx3d\n```\n\n# Check your installation\n\n## The four nx.Graph classes\n\n### nx.Graph demo\n```sh\npython -m nx3d\n```\n\n### nx.DiGraph demo\n```sh\npython -m nx3d dir\n```\n\n### nx.MultiGraph demo\n```sh\npython -m nx3d mul\n```\n\n### nx.MultiDiGraph demo\n```sh\npython -m nx3d mul dir\n```\n\n## Dynamic graph processes\n\n### Diffusion demo\n```sh\npython -m nx3d diffusion watt nolabel\n```\n\n### Game of Life demo\n```sh\npython -m nx3d life nofilter\n```\n\n# Usage\nIn your Python code:\n```python\nimport networkx as nx\nimport nx3d\n\ng = nx.frucht_graph()\nnx3d.plot(g)\n```\n\n# Next steps\nCheck out the [docs](https://nx3d.readthedocs.io/en/latest/) for tutorials, how-to-guides, explanations, and reference\nmaterial.\n',
    'author': 'Eric Kalosa-Kenyon',
    'author_email': 'helloateric@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ekalosak/nx3d',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
