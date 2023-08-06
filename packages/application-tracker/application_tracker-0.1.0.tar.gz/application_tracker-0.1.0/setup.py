# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['application_tracker']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0', 'shellingham>=1.5.0,<2.0.0', 'typer>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'application-tracker',
    'version': '0.1.0',
    'description': 'A simple CLI to save and view job applications.',
    'long_description': '# Job Application Tracker\nA simple command line interface to track job applications.\nBuilt using [Typer](https://github.com/tiangolo/typer). This project\nwas an exercise in basic software development, testing, and packaging. Tutorials followed:\n<br />\n* [https://realpython.com/command-line-interfaces-python-argparse/](https://realpython.com/command-line-interfaces-python-argparse/)\n* [https://realpython.com/pypi-publish-python-package/#prepare-your-package-for-publication](https://realpython.com/pypi-publish-python-package/#prepare-your-package-for-publication)',
    'author': 'Jamie Fraser',
    'author_email': 'jamie.fraser19@btinternet.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
