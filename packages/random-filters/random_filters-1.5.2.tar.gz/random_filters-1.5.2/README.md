# Random filters: Python packaging for generate random filters to use in your project

## Installation

```bash
pip install random-filters
```

## Usage

```python
from random_filters import checkbox
from random_filters import combobox
from random_filters import date
from random_filters import date_partition
from random_filters import store

# Checkbox
checkbox()
## jantar

# Date
date('2022-01-01', '2022-01-30')
## '2022-01-29'

```