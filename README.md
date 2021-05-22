# DateRecognition

DateRecognition is a Pure-Python library for extracting dates from strings.

## Requirements

python3.6+

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install DateRecognition.

```bash
pip install daterecognition
```

## Usage

```python
from daterecognition.parser import CoreDateParser as Parser
import daterecognition.formats as FORMATS

dp = Parser(formats=FORMATS.USA, start_year=2015, end_year=2020) 
# or provide list of date formats in 1989 C Standard
dp = Parser(formats=[r"%b %d, %Y"], start_year=2015, end_year=2020)

query = "Today is April 1, 2020"
dates = dp.parse_string(query)
print(dates)
```

## Output
```bash
[
    {
        'string': 'april 1, 2020', 
        'char_start_idx': 9, 
        'char_end_idx': 21, 
        'date_format': '%B %-d, %Y', 
        'token_start_idx': 2, 
        'token_end_idx': 4
    }
]
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)