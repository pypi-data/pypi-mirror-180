# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyperworks_tools',
 'hyperworks_tools.cli',
 'hyperworks_tools.post',
 'hyperworks_tools.post.datastructure']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['hyperworkstools = hyperworks_tools.cli.root:app']}

setup_kwargs = {
    'name': 'hyperworks-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Hyperworks-Tools!\n\n## Purpose\n\nThis repository will be the place where I want to develop Hyperworks tools for automating different stuff. \nThe first thing, which I did here was automatic extraction of objective values from multiple Simulations.\nPreprocessing stuff is planned - like generating template models based on inputs and more. I will update the general info here and the documentation.\nI also want to implement software development standards here, as for automatic testing and deploying but there is still much to learn for me so don't expect it to be perfect right from the start. \n\n## Documentation\n\nFind the documentation [here](https://manuel1618.github.io/hyperworks-tools/) (GitHub Pages/mkdocs)\n\n\n## License\n\nMIT\n\n",
    'author': 'Manuel',
    'author_email': 'manuel.ramsaier89@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.9,<4.0.0',
}


setup(**setup_kwargs)
