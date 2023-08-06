# eyedlog

A tool to make the log display more elegant.

## Installation

```shell
pip install eyedlog
```

## Usage

Recommended usage

```python
from eyedlog import get_logger

logger = get_logger('pretty.log')
logger.info('some text')
```

Advanced usage

```python
from eyedlog import ColoredLogger

logger = ColoredLogger('pretty.log')
logger.info('some text')
```

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
```
