# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chams']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0', 'rich>=12.6.0,<13.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['chams = chams.__main__:app']}

setup_kwargs = {
    'name': 'chams',
    'version': '0.1.0',
    'description': '',
    'long_description': '# My Project\n\nMy Project is a tool that does multiple NLP using gpt3.\n- emails generation\n- paraphrasing\n\n## contact\n\n- email: [zfellah](mailto:zfellah@generixgroup.com)',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
