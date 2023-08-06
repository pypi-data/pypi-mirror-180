# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raider', 'raider.parsers', 'raider.plugins', 'raider.plugins.basic']

package_data = \
{'': ['*'],
 'raider': ['.mypy_cache/*',
            '.mypy_cache/3.10/*',
            '.mypy_cache/3.10/_typeshed/*',
            '.mypy_cache/3.10/collections/*',
            '.mypy_cache/3.10/ctypes/*',
            '.mypy_cache/3.10/email/*',
            '.mypy_cache/3.10/importlib/*',
            '.mypy_cache/3.10/importlib/metadata/*',
            '.mypy_cache/3.10/json/*',
            '.mypy_cache/3.10/logging/*',
            '.mypy_cache/3.10/os/*',
            '.mypy_cache/3.10/urllib/*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'funcparserlib>=1.0.0a0,<2.0.0',
 'hy>=1.0.a4,<2.0',
 'igraph>=0.10.2,<0.11.0',
 'ipython>=8.4.0,<9.0.0',
 'pkce>=1.0.3,<2.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['raider = raider.cli:main']}

setup_kwargs = {
    'name': 'raider',
    'version': '0.3.1',
    'description': 'Web authentication testing framework',
    'long_description': '![Raider logo](./ext/logo.png)\n\n# Quick links\n\n- [Documentation](https://docs.raiderauth.com/en/latest/).\n- [Installation](https://docs.raiderauth.com/en/latest/overview/install.html).\n- [FAQ](https://docs.raiderauth.com/en/latest/overview/faq.html).\n- [Getting started](https://docs.raiderauth.com/en/latest/tutorials/getting_started.html).\n- [Architecture](https://docs.raiderauth.com/en/latest/case_studies/architecture.html)\n- [Discussions](https://github.com/OWASP/raider/discussions).\n- [Issues](https://github.com/OWASP/raider/issues).\n\n# What is Raider\n\nThis is a framework initially designed to test and automate the\nauthentication process for web applications, and by now it has evolved\nand can be used for all kinds of stateful HTTP processes. It abstracts\nthe client-server information exchange as a finite state machine. Each\nstep comprises one request with inputs, one response with outputs,\narbitrary actions to do on the response, and conditional links to\nother stages. Thus, a graph-like structure is created.\n\nRaider\'s configuration is inspired by Emacs. Hylang is used, which is\nLISP on top of Python. LISP is used because of its "Code is Data, Data\nis Code" property. With the magic of LISP macros generating\nconfiguration automatically becomes easy. Flexibility is in its DNA,\nmeaning it can be infinitely extended with actual code. Since all\nconfiguration is stored in cleartext, reproducing, sharing or\nmodifying attacks becomes easy.\n\n![Example hylang configuration](./ext/config.png)\n\n\n# Graph-like architecture\n\nRaider defines a DSL to describe the information flow between the\nclient and the server for HTTP processes. Each step of the process is\ndescribed by a Flow, which contains the Request with inputs, Response\nwith outputs, and arbitrary actions including links to other Flows:\n\n![Flows](./ext/raider_flows.png)\n\nChaining several Flows together can be used to simulate any stateful\nHTTP process. FlowGraphs indicate the starting point. They can be\nplaced on any Flow. A FlowGraphs runs all Flows in the link until\nSuccess/Failure is returned or if there are no more links.\n\n![Flows and FlowGraphs](./ext/graph.png)\n',
    'author': 'Daniel Neagaru',
    'author_email': 'daniel@digeex.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://raiderauth.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
