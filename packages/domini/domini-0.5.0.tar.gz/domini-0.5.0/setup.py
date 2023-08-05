# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['domini']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'domini',
    'version': '0.5.0',
    'description': 'Create HTML documents using Pythonic syntax that mimics the real deal.',
    'long_description': "# Domini\n\nA small, simple package for generating HTML documents.\nThe syntax aims to immitate HTML as closely as possible for legibility and easy of use.\n\n## Attributes\n\nAttributes *without* a value are entered as *positional arguments*.<br>\nAttributes *with* a value are entered as *keyword arguments*.\n\nTo specify attributes that collide with reserved Python keywords,\nappend an underscore and it will be removed.\n\n#### Python\n\n```py\nfrom domini.html import dialog\n\ndialog('open', class_='mydialog')\n```\n\n#### HTML\n\n```html\n<dialog open class='mydialog'>\n```\n\n## Content\n\nTo add children to an element, you can use either the `add` method or the short-hand greater-than operator. The right-hand side can be either any sequence, iterator, or generator of elements or a lone element. These elements can be either other tags or plain strings.\n\n**NOTE**: `add` does add them to the current object. `>` returns a new, identical element with those children added.\n\n```py\nul(class_='todo')> (\n    li()> 'Buy a fruit basket.',\n    li()> (\n        'Read', a(href='https://wikipedia.org/')> 'Wikipedia',\n        'to learn more about things you may have not otherwise cared about.',\n    ),\n)\n```\n\n## Closing tags\n\nA tag is only closed if content is provided. E.g. `<p></p>` as opposed to `<p>`. This can be an empty tuple.\n\n```py\nsection()> ()\n```\n\nFor open tags like `<br>` and `<hr>`, you simply do `br()` and `hr()`.",
    'author': 'Maximillian Strand',
    'author_email': 'maxi@millian.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/deepadmax/domini',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
