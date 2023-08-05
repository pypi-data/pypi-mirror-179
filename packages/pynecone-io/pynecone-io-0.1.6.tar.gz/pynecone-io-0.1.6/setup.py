# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pynecone',
 'pynecone..templates.app',
 'pynecone.compiler',
 'pynecone.components',
 'pynecone.components.base',
 'pynecone.components.datadisplay',
 'pynecone.components.disclosure',
 'pynecone.components.feedback',
 'pynecone.components.forms',
 'pynecone.components.graphing',
 'pynecone.components.layout',
 'pynecone.components.libs',
 'pynecone.components.media',
 'pynecone.components.navigation',
 'pynecone.components.overlay',
 'pynecone.components.tags',
 'pynecone.components.transitions',
 'pynecone.components.typography',
 'pynecone.middleware']

package_data = \
{'': ['*'],
 'pynecone': ['.templates/assets/*',
              '.templates/web/.gitignore',
              '.templates/web/.gitignore',
              '.templates/web/.gitignore',
              '.templates/web/next.config.js',
              '.templates/web/next.config.js',
              '.templates/web/next.config.js',
              '.templates/web/package.json',
              '.templates/web/package.json',
              '.templates/web/package.json',
              '.templates/web/pages/*',
              '.templates/web/utils/*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'gunicorn>=20.1.0,<21.0.0',
 'plotly>=5.10.0,<6.0.0',
 'pydantic==1.10.2',
 'redis>=4.3.5,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0',
 'sqlmodel>=0.0.8,<0.0.9',
 'typer>=0.7.0,<0.8.0',
 'uvicorn>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['pc = pynecone.pc:main']}

setup_kwargs = {
    'name': 'pynecone-io',
    'version': '0.1.6',
    'description': 'The easiest way to build web apps.',
    'long_description': '<div align="center">\n\n<img src="docs/images/logo.png" alt="drawing" width = 450/>\n\n**The easiest way to build and deploy web apps.**\n\n[![PyPI version](https://badge.fury.io/py/pynecone-io.svg)](https://badge.fury.io/py/pynecone-io)\n![versions](https://img.shields.io/pypi/pyversions/pynecone-io.svg)\n[![License](https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)  \n\n\n<div align="left">\n\n## Getting Started\n\nPynecone is a full-stack python framework that makes it easy to build and deploy web apps in minutes.\n\nAll the information for getting started can be found in this README, however, a more detailed explanation of the following topics can be found on our website:\n\n<div align="center">\n\n### [Introduction](https://pynecone.io/docs/getting-started/introduction) | [Component Library](https://pynecone.io/docs/library) | [Examples](https://pynecone.io) | [Deployment](https://pynecone.io/docs/hosting/deploy) \n\n<div align="left">\n\n## Installation\nPynecone requires to following to get started:\n* Python 3.7+\n* [NodeJS 12.22.0+](https://nodejs.org/en/)\n\n```\n$ pip install pynecone-io\n```\n\n## Create your first Pynecone app\n\nInstalling Pynecone also installs the pc command line tool. Test that the install was successful by creating a new project. \n\nReplace my_app_name with your project name:\n\n```\n$ mkdir my_app_name\n$ cd my_app_name\n$ pc init\n```\n\nThis initializes a template app in your new directory.\nYou can run this app in development mode:\n```\n$ pc run\n```\n\n\nYou should see your app running at http://localhost:3000.\n\n\nNote that the port may be different if you have another app running on port 3000.\n\n\nNow you can modify the source code in my_app_name/my_app_name.py. Pynecone has fast refreshes so you can see your changes instantly when you save your code.\n\n## Example App\n\nLet\'s go over a simple counter app to explore the basics of Pynecone.\n\n<div align="center">\n<img src="docs/images/counter.gif" alt="drawing" width="550"/>\n<div align="left">\n\nHere is the complete code to create this.\n\n```python\nimport pynecone as pc\nimport random\n\nclass State(pc.State):\n    count = 0\n\n    def increment(self):\n        """Increment the count."""\n        self.count += 1\n\n    def decrement(self):\n        """Decrement the count."""\n        self.count -= 1\n\n    def random(self):\n        """Randomize the count."""\n        self.count = random.randint(0, 100)\n\n\ndef index():\n    """The main view."""\n    return pc.center(\n        pc.vstack(\n            pc.heading(State.count),\n            pc.hstack(\n                pc.button("Decrement", on_click=State.decrement, color_scheme="red"),\n                pc.button(\n                    "Randomize",\n                    on_click=State.random,\n                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",\n                    color="white",\n                ),\n                pc.button("Increment", on_click=State.increment, color_scheme="green"),\n            ),\n            padding="1em",\n            bg="#ededed",\n            border_radius="1em",\n            box_shadow="lg",\n        ),\n        padding_y="5em",\n        font_size="2em",\n        text_align="center",\n    )\n\n\n# Add state and page to the app.\napp = pc.App(state=State)\napp.add_page(index, title="Counter")\napp.compile()\n```\nLet\'s break this down.\n\n* ### State\n    \n``` python\nclass State(pc.State):\n    count = 0 \n```\nThe state defines all the variables (called vars) in an app that can change, as well as the functions that change them.\nHere our state has by a single var, count, which holds the current value of the counter.\nThe frontend of the app is a reflection of the current state.\n\n    \n* ### Event Handlers\n```python\ndef increment(self):\n    """Increment the count."""\n    self.count += 1\n\ndef decrement(self):\n    """Decrement the count."""\n    self.count -= 1\n\ndef random(self):\n    """Randomize the count."""\n    self.count = random.randint(0, 100)\n```\nWithin the state, we define functions, called event handlers, that change the state vars.\nEvent handlers are the only way that we can modify the state in Pynecone. They can be called in response to user actions, such as clicking a button or typing in a text box. These actions are called events.\nOur counter app has two event handlers, increment and decrement.\n    \n* ### Frontend\n\n```python \ndef index():\n    return pc.center(\n        pc.vstack(\n            pc.heading(State.count),\n            pc.hstack(\n                pc.button("Decrement", on_click=State.decrement, color_scheme="red"),\n                pc.button(\n                    "Randomize",\n                    on_click=State.random,\n                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",\n                    color="white",\n                ),\n                pc.button("Increment", on_click=State.increment, color_scheme="green"),\n            ),\n            padding="1em",\n            bg="#ededed",\n            border_radius="1em",\n            box_shadow="lg",\n        ),\n        padding_y="5em",\n        font_size="2em",\n        text_align="center",\n    )\n```\nThis function defines the frontend of the app.\nWe use different components such as pc.box, pc.button, and pc.heading to build the frontend. Components can be nested to create complex layouts, and can be styled using the full power of CSS.\n    \nPynecone comes with [50+ built-in components](https://pynecone.io/docs/library) to help you get started. \nWe are actively adding more components, plus it\'s easy to create your own components.\n\n* ### Routing \n    \nNext we define our app and tell it what state to use.\n```python\napp = pc.App(state=State)\n```\nWe add a route from the root of the app to the counter component. By default the route\n```python\napp.add_page(index)\n```\nYou can create a multi-page app by adding more routes.\n    \n## Contributing\n\nPull requests are encouraged and always welcome. Pick an issue and help us out, or submit an issue id something is not working or confusing!\n\n## More Information \n\nMore information about Pynecone can be found on our website, https://pynecone.io\n  \n## License\n\nPynecone is open-source and licensed under the [Apache License 2.0](LICENSE)\n',
    'author': 'Nikhil Rao',
    'author_email': 'nikhil@pynecone.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pynecone.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
