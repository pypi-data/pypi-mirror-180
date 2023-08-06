# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codegpt']

package_data = \
{'': ['*']}

install_requires = \
['nltk>=3.7,<4.0', 'openai>=0.2,<0.3', 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['codegpt = codegpt.codegpt:app']}

setup_kwargs = {
    'name': 'codegpt',
    'version': '0.0.6',
    'description': "A CLI tool for refactoring Python code using OpenAI's text-davinci-003 model",
    'long_description': '# Codegpt\n\nA tool for using GPT just a little quicker. A nearly truly automated footgun. Learn how to revert with git before trying please.\n\n# Getting Started\n\n`pip install codegpt`\n\nThen find a file you hate (Back it up! Don\'t do it live!) and give it a shot.\n\n`codegpt refactor .\\helper.py "Break this up into smaller functions where you can. Add google style docstrings. Feel free to rewrite any code doesn\'t make sense."`\n\nYou\'ll see something like:\n\n```sh\nThis prompt is 254 tokens, are you sure you want to continue?\nThe most GPT-3 can return in response is 3843. [y/N]: y\n\n(and after a short wait...)\n\nExplanation: The code has been refactored into smaller functions to improve readability, and Google style docstrings have been added.\n```\n\nOther things to try:\n\n- `codegpt edit` - For editing markdown files, including code blocks. Hello, blog editor!\n- `codegpt varnames` - Changes variable names (and supposed to only be variable names...) to be readable\n- `codegpt comment` - Automatically add comments to a file.\n\nPropose endpoints as issues, I\'ve got a few ideas:\n\n- Explain file\n- Write tests for file\n- Generate SQL query from table spec files\n- Generate new file\n- Generate documentation from a file\n\nJust remember this is paid - 2 cents per 1k tokens is a lot when you\'re working on files with a few hundred lines.\n\nAnd remember to break up what you\'re working on - Results will be better with less moving parts and things to do.\n',
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
