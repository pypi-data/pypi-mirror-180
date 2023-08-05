# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['monoformat']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'colorama>=0.4.6,<0.5.0',
 'isort>=5.10.1,<6.0.0',
 'node-edge>=0.1.0b2,<0.2.0',
 'pathspec>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['monoformat = monoformat.__main__:__main__']}

setup_kwargs = {
    'name': 'monoformat',
    'version': '0.1.0b3',
    'description': 'A tool that formats all kinds of languages consistently',
    'long_description': '# Monoformat\n\nOpinionated and "zero config" formatters like Black and Prettier are amazing in\nthe sense that they remove any need for thinking about formatting. However, they\nstill require you to:\n\n-   Be used separately (one is Python and the other is Node)\n-   Be configured for the language version and so forth\n\nMonoformat does this automatically. You can only use the language version that\nmonoformat allows and you can configure literally nothing except which files\nit\'s going to reformat and which it\'s not.\n\n## Installation\n\nMonoformat is available on PyPI:\n\n```bash\npip install monoformat\n```\n\n## Usage\n\nMonoformat is a command line tool. You can run it with:\n\n```bash\nmonoformat .\n```\n\nThis will reformat all files in the current directory and its subdirectories.\n\nIt will take care to avoid `.git` and other special directories. There is a\ndefault pattern embedded but you can change it with the `--do-not-enter` flag,\nwhich is a pattern matching folder or file names you don\'t want to consider.\n\nOn addition to the `--do-not-enter` rule, it will by default check all\n`.gitignore` files and `.formatignore` files (which use the `.gitignore` syntax\nbut only affect the decision of whether to format a file or not, not to put them\nin git) and.\n\n### Default project\n\nLet\'s say you have a Django project. It contains lots of files, including a\n`node_modules` somewhere and a _a lot_ of big migration files.\n\nYou might want to have at the root of your repo a `.gitignore` file that looks\nlike that:\n\n```\nnode_modules\n.idea\n.vscode\n.env\n*.pyc\n```\n\nAnd then specifically to avoid formatting migrations (which can be super\nexpensive), and to avoid running prettier on Django templates (which ends up\nbadly) add a `.formatignore` file that looks like that:\n\n```\n**/migrations/*\n**/templates/*\n```\n\nThen you can run `monoformat .` and it will only format the files that are\nrelevant to your project.\n\n### Without install\n\nI\'ve actually spent an absurd amount of time to make it extremely simple to run\nPython and JS code without installing anything. You can do this with:\n\n```bash\ncurl -s https://pypi.run/monoformat | python3.10 - .\n```\n\nDoing so will entirely reformat with black, isort and prettier the current\ndirectory.\n\n## Supported languages\n\nMonoformat supports the following languages:\n\n-   **Python** 3.10 (Black)\n-   **JavaScript** (Prettier)\n-   **TypeScript** (Prettier)\n-   **JSON** (Prettier)\n-   **Markdown** (Prettier)\n-   **YAML** (Prettier)\n-   **HTML** (Prettier)\n-   **CSS** (Prettier)\n-   **SCSS** (Prettier)\n-   **Vue** (Prettier)\n-   **Svelte** (Prettier)\n-   **PHP** (Prettier)\n',
    'author': 'Rémy Sanchez',
    'author_email': 'remy.sanchez@hyperthese.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Xowap/Monoformat',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
