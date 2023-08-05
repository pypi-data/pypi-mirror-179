[![Build][build-image]]()
[![Status][status-image]][pypi-project-url]
[![Stable Version][stable-ver-image]][pypi-project-url]
[![Coverage][coverage-image]]()
[![Python][python-ver-image]][pypi-project-url]
[![License][bsd3-image]][bsd3-url]


# thquickjs

*Python* binding for *QuickJS* JavaScript Engine.
QuickJS is a small and embeddable *JavaScript* engine. 
Safely evaluate untrusted JavaScript code. 
Create and manipulate values inside the QuickJS runtime. 
Expose host functions to the QuickJS runtime.


## Installation

```bash
pip install thquickjs
```


## Simple Usage

```python
qjs = QuickJS()

with unwrap():
    # call JS function
    code = '''
        var f = (x) => {
            return [ x ];
        };
    '''

    qjs.eval(code)
    f: callable = qjs.get_function('f')
    result = f(10)
    assert result == [10]

    # register Python function inside JS runtime
    py_name = 'pylam'
    py_func = lambda x: json.dumps([x * 10])
    qjs.add_callable(py_name, py_func)

    # call Python function from JS runtime
    code = '''
        var g = (x) => {
            return [ JSON.parse(pylam(x)) ];
        };
    '''

    qjs.eval(code)
    g: callable = qjs.get_function('g')
    result = g(10)
    assert result == [[100]]
    
    # call Python function registered in JS runtime
    pylam = qjs.get(py_name)
    result = pylam(5)
    assert result == json.dumps([50])
```


## Testing
```bash
docker-compose build thquickjs-test ; docker-compose run --rm thquickjs-test
```


## Coverage

```bash
docker-compose build thquickjs-coverage ; docker-compose run --rm -v $PWD:/test thquickjs-coverage
```


## Building
```bash
docker-compose build thquickjs-build ; docker-compose run --rm thquickjs-build
```


## Licensing

`thquickjs` is licensed under the BSD 3 license.

Check the [LICENSE](https://opensource.org/licenses/BSD-3-Clause) for details.


<!-- Badges -->
[bsd3-image]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
[bsd3-url]: https://opensource.org/licenses/BSD-3-Clause
[build-image]: https://img.shields.io/gitlab/pipeline-status/tangledlabs/thquickjs?branch=main
[coverage-image]: https://img.shields.io/gitlab/pipeline-coverage/tangledlabs/thquickjs?branch=main

[pypi-project-url]: https://pypi.org/project/thquickjs/
[stable-ver-image]: https://img.shields.io/pypi/v/thquickjs?label=stable
[python-ver-image]: https://img.shields.io/pypi/pyversions/thquickjs.svg?logo=python&logoColor=FBE072
[status-image]: https://img.shields.io/pypi/status/thquickjs.svg
