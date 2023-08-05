# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thquickjs']

package_data = \
{'': ['*']}

install_requires = \
['quickjs>=1.19.2,<2.0.0', 'thresult>=0.9.23,<0.10.0']

setup_kwargs = {
    'name': 'thquickjs',
    'version': '0.9.25',
    'description': 'Tangled QuickJS Javascript Engine binding library',
    'long_description': "[![Build][build-image]]()\n[![Status][status-image]][pypi-project-url]\n[![Stable Version][stable-ver-image]][pypi-project-url]\n[![Coverage][coverage-image]]()\n[![Python][python-ver-image]][pypi-project-url]\n[![License][bsd3-image]][bsd3-url]\n\n\n# thquickjs\n\n*Python* binding for *QuickJS* JavaScript Engine.\nQuickJS is a small and embeddable *JavaScript* engine. \nSafely evaluate untrusted JavaScript code. \nCreate and manipulate values inside the QuickJS runtime. \nExpose host functions to the QuickJS runtime.\n\n\n## Installation\n\n```bash\npip install thquickjs\n```\n\n\n## Simple Usage\n\n```python\nqjs = QuickJS()\n\nwith unwrap():\n    # call JS function\n    code = '''\n        var f = (x) => {\n            return [ x ];\n        };\n    '''\n\n    qjs.eval(code)\n    f: callable = qjs.get_function('f')\n    result = f(10)\n    assert result == [10]\n\n    # register Python function inside JS runtime\n    py_name = 'pylam'\n    py_func = lambda x: json.dumps([x * 10])\n    qjs.add_callable(py_name, py_func)\n\n    # call Python function from JS runtime\n    code = '''\n        var g = (x) => {\n            return [ JSON.parse(pylam(x)) ];\n        };\n    '''\n\n    qjs.eval(code)\n    g: callable = qjs.get_function('g')\n    result = g(10)\n    assert result == [[100]]\n    \n    # call Python function registered in JS runtime\n    pylam = qjs.get(py_name)\n    result = pylam(5)\n    assert result == json.dumps([50])\n```\n\n\n## Testing\n```bash\ndocker-compose build thquickjs-test ; docker-compose run --rm thquickjs-test\n```\n\n\n## Coverage\n\n```bash\ndocker-compose build thquickjs-coverage ; docker-compose run --rm -v $PWD:/test thquickjs-coverage\n```\n\n\n## Building\n```bash\ndocker-compose build thquickjs-build ; docker-compose run --rm thquickjs-build\n```\n\n\n## Licensing\n\n`thquickjs` is licensed under the BSD 3 license.\n\nCheck the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details.\n\n\n<!-- Badges -->\n[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg\n[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause\n[build-image]: https://img.shields.io/gitlab/pipeline-status/tangledlabs/thquickjs?branch=main\n[coverage-image]: https://img.shields.io/gitlab/pipeline-coverage/tangledlabs/thquickjs?branch=main\n\n[pypi-project-url]: https://pypi.org/project/thquickjs/\n[stable-ver-image]: https://img.shields.io/pypi/v/thquickjs?label=stable\n[python-ver-image]: https://img.shields.io/pypi/pyversions/thquickjs.svg?logo=python&logoColor=FBE072\n[status-image]: https://img.shields.io/pypi/status/thquickjs.svg\n",
    'author': 'Tangled',
    'author_email': 'info@tangledgroup.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/tangledlabs/thquickjs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
