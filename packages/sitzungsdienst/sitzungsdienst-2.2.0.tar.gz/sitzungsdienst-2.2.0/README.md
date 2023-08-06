# sitzungsdienst
[![License](https://badgen.net/badge/license/GPL/blue)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/LICENSE) [![PyPI](https://badgen.net/pypi/v/sitzungsdienst)](https://pypi.org/project/sitzungsdienst) [![Coverage](https://badgen.net/badge/coverage/100/cyan)](https://codeberg.org/S1SYPHOS/sitzungsdienst/src/branch/main/COVERAGE) [![Build](https://ci.codeberg.org/api/badges/S1SYPHOS/sitzungsdienst/status.svg)](https://codeberg.org/S1SYPHOS/sitzungsdienst/issues)

A simple Python utility for working with weekly assignment PDFs as exported by [`web.sta`](https://www.dvhaus.de/leistungen/web.sta).


## Getting started

Simply install all dependencies inside a virtual environment to get started:

```bash
# Set up & activate virtualenv
virtualenv -p python3 venv

# shellcheck disable=SC1091
source venv/bin/activate

# Install dependencies, either ..
# (1) .. from PyPi (stable)
python -m pip install sitzungsdienst

# (2) .. from repository (dev)
python -m pip install --editable .
```


## Usage

Using this library is straightforward:

```python
from sitzungsdienst import StA

# Pass file path (or its stream) & retrieve data
court_dates, express_dates = StA.run('path/to/file.pdf')

# Use a subset by filtering it
filtered_court = court_dates.filter(['alice', 'bob'])
filtered_express = express_dates.filter('john')
```

If you want to see it in action, head over to the [`sitzungsapp`](https://codeberg.org/S1SYPHOS/sitzungsapp)!


**Happy coding!**
