# googlesearch.py
The search API for [Google](https://www.google.com).


## Installation:

- Python 3.6 or later is required.

- First, please make sure that the latest pip version is installed in your working environment.
```
python -m pip install -U pip
```

- Run the following command given below to install the package:
```
python -m pip install -U googlesearch.py
```

## Get Started

- Here is an example program.
```py
from gsearchlib import Search

result = Search("what is programming language")

print(result)
```

### Output:

- If a result for your search query is found while running the above program, it will return an dict object; otherwise, it will return None.
```json
[
    {
        "title": "Programming language - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Programming_language"
    }
...
]
```