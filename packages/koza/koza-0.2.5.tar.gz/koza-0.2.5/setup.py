# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['koza',
 'koza.converter',
 'koza.io',
 'koza.io.reader',
 'koza.io.writer',
 'koza.model',
 'koza.model.config',
 'koza.utils']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.4',
 'linkml-validator>=0.4.4',
 'ordered-set>=4.1.0',
 'pydantic>=1.0.0,<2.0.0',
 'pyyaml>=5.3.1,<6.0.0',
 'requests>=2.24.0,<3.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['koza = koza.main:typer_app']}

setup_kwargs = {
    'name': 'koza',
    'version': '0.2.5',
    'description': 'Data transformation framework for LinkML data models',
    'long_description': '# Koza - a data transformation framework [![Pyversions](https://img.shields.io/pypi/pyversions/koza.svg)](https://pypi.python.org/pypi/koza) ![](https://github.com/monarch-initiative/koza/actions/workflows/build.yml/badge.svg) [![PyPi](https://img.shields.io/pypi/v/koza.svg)](https://pypi.python.org/pypi/koza)\n![pupa](docs/img/pupa.png)  \n\n**Documentation**: https://koza.monarchinitiative.org/  \n\n_Disclaimer_: Koza is in beta; we are looking for beta testers\n\n### Overview\n  - Transform csv, json, yaml, jsonl, and xml and converting them to a target csv, json, or jsonl format based on your dataclass model.  \n  - Koza also can output data in the [KGX format](https://github.com/biolink/kgx/blob/master/specification/kgx-format.md#kgx-format-as-tsv)\n  - Write data transforms in semi-declarative Python\n  - Configure source files, expected columns/json properties and path filters, field filters, and metadata in yaml\n  - Create or import mapping files to be used in ingests (eg id mapping, type mappings)\n  - Create and use translation tables to map between source and target vocabularies\n\n### Installation\nKoza is available on PyPi and can be installed via pip:\n```\npip install koza\n```\n\n### Usage\n\n**NOTE: As of version 0.2.0, there is a new method for getting your ingest\'s `KozaApp` instance. Please see the [updated documentation](https://koza.monarchinitiative.org/Usage/configuring_ingests/#transform-code) for details.**\n\nSee the [Koza documentation](https://koza.monarchinitiative.org/) for usage information\n\n### Try the Examples\n\n#### Validate\n\nGive Koza a local or remote csv file, and get some basic information (headers, number of rows)\n\n```bash\nkoza validate \\\n  --file https://raw.githubusercontent.com/monarch-initiative/koza/main/examples/data/string.tsv \\\n  --delimiter \' \'\n```\n\nSending a json or jsonl formatted file will confirm if the file is valid json or jsonl\n\n```bash\nkoza validate \\\n  --file ./examples/data/ZFIN_PHENOTYPE_0.jsonl.gz \\\n  --format jsonl\n```\n\n```bash\nkoza validate \\\n  --file ./examples/data/ddpheno.json.gz \\\n  --format json \\\n  --compression gzip\n```\n\n#### Transform\n\nRun the example ingest, "string/protein-links-detailed"\n```bash\nkoza transform --source examples/string/protein-links-detailed.yaml --global-table examples/translation_table.yaml\n\nkoza transform --source examples/string-declarative/protein-links-detailed.yaml --global-table examples/translation_table.yaml\n```\nnote: koza expects a directory structure as described in the above example (examples/ingest_name/ingest.yaml)',
    'author': 'The Monarch Initiative',
    'author_email': 'info@monarchinitiative.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
