# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['safetydance_test']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6.2.2,<7.0.0',
 'safetydance>=0.3.1,<0.4.0',
 'type-extensions>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'safetydance-test',
    'version': '0.2.0',
    'description': 'A testing framework built upon the typesafe composition of steps.',
    'long_description': '# safetydance_test\n\nA [`safetydance`](https://cucumber.io/docs/bdd/) library of steps for testing in a [BDD](https://cucumber.io/docs/bdd/) style.\n\n## Example\n\n```python\n@scripted_test\ndef test_something():\n    Given.some_pre_condition()\n    When.something_is_done()\n    Then.some_post_condition_is_satisfied()\n```',
    'author': 'David Charboneau',
    'author_email': 'david@adadabase.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dcharbon/safetydance_test',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
