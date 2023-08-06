# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_plugin_pypi_mirror']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.3.0,<1.4.0']

entry_points = \
{'poetry.plugin': ['demo = poetry_plugin_pypi_mirror.plugins:PyPIMirrorPlugin']}

setup_kwargs = {
    'name': 'poetry-plugin-pypi-mirror',
    'version': '0.3.0',
    'description': 'Poetry plugin that adds support for pypi.org mirrors and pull-through caches',
    'long_description': '# poetry-plugin-pypi-mirror\n\n## Description\n\n*poetry-plugin-pypi-mirror* is a\n[plugin](https://python-poetry.org/docs/master/plugins/) for\n[poetry](https://python-poetry.org/), the Python packaging and dependency\nmanager. It enables poetry to substitute connections to pypi.org with\nconnections to a pypi.org mirror or pull-through cache **without requiring\nproject configuration changes**. This is ideal for situations where an\naccess-restricted or otherwise unsuitable-for-general-use pypi.org mirror must\nbe used by a subset of project contributors. For example:\n\n* A private PyPI mirror internal to a business, required by company policy\n* A limited-access PyPI mirror in a region where pypi.org is restricted\n* A regional mirror that is more performant for a few users, and less performant\n  for everyone else\n\nThese mirrors can be used without this plugin by [adding them as project\nrepositories](https://python-poetry.org/docs/repositories/). However, this\nrequires the mirror to be included in the project\'s configuration, and this also\nresults in source entries for the mirror appearing in `poetry.lock`. Since only\na subset of project contributors can use these mirrors, that subset of users\nwould need to replace and remove references to the mirror repository each time\nthey want to contribute their changes back to the project. This is suboptimal.\n\n## Usage\n\n### Installation\n\nFollow poetry\'s [plugin installation instructions](https://python-poetry.org/docs/master/plugins/#using-plugins), replacing `poetry-plugin` with `poetry-plugin-pypi-mirror`.\n\n### Specifying a mirror\n\nTo specify a mirror, you can either define `plugins.pypi_mirror.url` in poetry\'s\n[configuration](https://python-poetry.org/docs/configuration/), or set\nenvironment variable `POETRY_PYPI_MIRROR_URL` to the full URL for a [PEP\n503](https://peps.python.org/pep-0503/)-compatible mirror. When both are set the\nenvironment variable will be used.\n\n#### Poetry config example\n\n```toml\n[plugins]\n[plugins.pypi_mirror]\nurl = "https://example.org/repository/pypi-proxy/simple/"\n```\n\n... in [either](https://python-poetry.org/docs/configuration/) a project\'s\n`poetry.toml` (for per-project configuration), or the user\'s `config.toml`.\n\n#### Environment variable example\n\n```shell\nPOETRY_PYPI_MIRROR_URL=https://example.org/repository/pypi-proxy/simple/ poetry add pendulum\n```\n...or...\n\n```shell\nexport POETRY_PYPI_MIRROR_URL=https://example.org/repository/pypi-proxy/simple/\npoetry add cleo # uses mirror specified in first line\npoetry lock     # also uses mirror specified in first line\n```\n\n## Compatibility\n\n*poetry-plugin-pypi-mirror* depends on poetry internals which can change between\npoetry releases. It\'s important to ensure compatibility between the poetry\nversion in use and the plugin version in use.\n\n| Poetry version(s) | Compatible plugin version(s) |\n|-------------------|------------------------------|\n| ~1.3.0            | ^0.3.0                       |\n| ~1.2.1            | < 0.3.0                      |\n\n## See also\n\n* [python-poetry/poetry#1632](https://github.com/python-poetry/poetry/issues/1632) - poetry feature request to add support for global repository URL replacement\n',
    'author': 'Jacob Henner',
    'author_email': 'code@ventricle.us',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/arcesium/poetry-plugin-pypi-mirror',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
