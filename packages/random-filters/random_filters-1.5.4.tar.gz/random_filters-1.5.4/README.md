# Random filters: Python packaging for generate random filters to use in your project

## Installation

```bash
pip install random-filters
```

## Usage

```python
import random_filters as rf

# checkbox
rf.checkbox()

# combobox
rf.combobox_hierarchy({"Estado": ["SP", "SP", "SP", "SC", "SC", "SC"],
                       "Cidade": ["São Paulo", "Itatiba", "Campinas", "Chapecó", "Xaxim", "Xanxerê"]})

# date
rf.date('2019-01-01', '2019-12-31')

# date_partition
rf.date_partition(2)

# store
rf.store(2)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
