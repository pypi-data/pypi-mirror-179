# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['modelstar',
 'modelstar.builtins',
 'modelstar.builtins.functions',
 'modelstar.builtins.packages',
 'modelstar.builtins.procedures',
 'modelstar.commands',
 'modelstar.connectors',
 'modelstar.connectors.snowflake',
 'modelstar.connectors.snowflake.modelstar',
 'modelstar.connectors.snowflake.sql_dialect',
 'modelstar.executors',
 'modelstar.executors.py_parser',
 'modelstar.templates',
 'modelstar.templates.report',
 'modelstar.templates.starter_kit.samples.functions',
 'modelstar.templates.starter_kit.samples.machine_learning',
 'modelstar.templates.starter_kit.samples.stored_procedure',
 'modelstar.utils']

package_data = \
{'': ['*'],
 'modelstar.templates': ['snowflake_project/.gitignore',
                         'snowflake_project/.gitignore',
                         'snowflake_project/.gitignore',
                         'snowflake_project/README.md',
                         'snowflake_project/README.md',
                         'snowflake_project/README.md',
                         'snowflake_project/modelstar.config.yaml',
                         'snowflake_project/modelstar.config.yaml',
                         'snowflake_project/modelstar.config.yaml',
                         'snowflake_project/sample_data/*',
                         'starter_kit/.gitignore',
                         'starter_kit/.gitignore',
                         'starter_kit/README.md',
                         'starter_kit/README.md'],
 'modelstar.templates.report': ['includes/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'joblib>=1.2.0,<2.0.0',
 'jsonschema>=4.16.0,<5.0.0',
 'markdown>=3.4.1,<4.0.0',
 'pandas>=1.5.1,<2.0.0',
 'snowflake-connector-python>=2.7.12,<3.0.0',
 'tabulate>=0.8.10,<0.9.0']

entry_points = \
{'console_scripts': ['modelstar = modelstar.cli:main']}

setup_kwargs = {
    'name': 'modelstar',
    'version': '0.4.0',
    'description': 'DevOps for User Defined Functions and Stored Procedures in Data Warehouses',
    'long_description': '# Hi there, this is <a href="https://modelstar.io/" style="color: #AF3BEA;"><img src="./static/logo.png" height="28"> Modelstar</a> 👋\n\nModelStar is the easiest way to ship and manage machine learning solutions inside Snowflake, with only a few lines of SQL.\n\n## Modelstar is for the modern data stack\n\n![How does Modelstar work?](./static/how-modelstar-works.png)\n\n## Who are the users?\n\n-   Snowflake and DBT users.\n-   Anyone who knows basic SQL.\n-   Analyst, data engineers.\n\n## Why we build Modelstar?\n\nModelstar is our attempt to simplify ML for analysts. Our design philosophy is: **Data is the most critical component in ML, so shipping ML solutions should be as easy as creating data objects.**\n\n## Installation\n\nTo get started with Modelstar, install the Modelstar Python package into your local Python environment.\n\n```shell\n$ pip install modelstar\n```\n\nIt\'s recommended to install `modelstar` within a Python virtual environment using `pyenv`, `virtualenv`, or `poetry`.\n\nFor a complete quickstart guide visit [**Modelstar-Quickstart**](https://modelstar.io/docs/quickstar)\n\n## Tutorials\n\n-   [**Forecast Sales inside Snowflake with 1 Line of SQL**](https://modelstar.io/docs/tutorials/sales-forecasting-inside-snowflake)',
    'author': 'Adithya Krishnan',
    'author_email': 'krishsandeep@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://modelstar.io',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
