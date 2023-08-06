# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linkml_owl',
 'linkml_owl.crossproducts',
 'linkml_owl.dumpers',
 'linkml_owl.util']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'click',
 'funowl>=0.1.12,<0.2.0',
 'linkml-runtime>=1.3.4,<2.0.0',
 'linkml>=1.3.0,<2.0.0']

entry_points = \
{'console_scripts': ['linkml-data2owl = linkml_owl.dumpers.owl_dumper:cli']}

setup_kwargs = {
    'name': 'linkml-owl',
    'version': '0.2.4',
    'description': 'OWL mappings for Linked Open Data Modeling Language',
    'long_description': '# linkml-owl\n\nTranslates between LinkML instance data to OWL (TBoxes and ABoxes)\n\nSee [linkml.io/linkml-owl](https://linkml.io/linkml-owl/)\n\n',
    'author': 'Chris Mungall',
    'author_email': 'cjmungall@lbl.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/linkml/linkml-owl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
