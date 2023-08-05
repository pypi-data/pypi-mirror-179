# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blueprinter', 'blueprinter.examples']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'blueprinter',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Blueprinter\n\nGenerates easy-to-use blueprints for your end users.  \n\n## Example Usage\nTo see an example of how to use Blueprinter, run the following in a python script:  \n\n```\nfrom blueprinter.templates import inline\ninline()\n```\n\n## Capabilities\nCurrently, Blueprinter provides \'inline\' snippets.  \nWhen called, your example code or template will replace the contents of the calling file.  \n\nFuture additions to this library will allow entire folders to be written to the calling file\'s directory of choice.\n\n\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Cabin+Sketch:wght@700&display=swap" rel="stylesheet">\n<style>\n    h1{font-family: \'Cabin Sketch\', cursive; font-size: 4rem;color:#0072dc}\n</style>',
    'author': 'MBeebe',
    'author_email': 'pyn-sol@beebe.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
