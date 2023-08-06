# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nqtgbot']

package_data = \
{'': ['*'], 'nqtgbot': ['resources/*']}

install_requires = \
['nqsdk', 'python-telegram-bot>=13.14,<14.0']

setup_kwargs = {
    'name': 'nqtgbot',
    'version': '1.0.0a4',
    'description': 'NQ Telegram Bot Provider',
    'long_description': '# NQ Telegram Bot Provider\n\n## Tests\n\nRun tests locally:\n\n```shell script\n./scripts/tests\n```\n',
    'author': 'Inqana Ltd.',
    'author_email': 'develop@inqana.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
