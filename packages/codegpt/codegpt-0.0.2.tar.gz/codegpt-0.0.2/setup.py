# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codegpt']

package_data = \
{'': ['*']}

install_requires = \
['nltk>=3.7,<4.0',
 'openai>=0.2,<0.3',
 'python-dotenv>=0.21.0,<0.22.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['codegpt = codegpt.codegpt:app']}

setup_kwargs = {
    'name': 'codegpt',
    'version': '0.0.2',
    'description': "A CLI tool for refactoring Python code using OpenAI's text-davinci-003 model",
    'long_description': None,
    'author': 'John Partee',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/morganpartee/codegpt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
