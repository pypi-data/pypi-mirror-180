# url_location

This library can be used to retrieve the country a URL belongs to by processing its domain.

## Usage

```python
from url_location import URLLocation

url = "https://www.exampleurl.com.ec/something-else"
ul = URLLocation()
country = ul.processUrl(url)
print(country)
```

Output
```console
ECU
```

When a URL can´t be processed the result will be <UNK> like bellow:

```python
url = "https://www.exampleurl.com/something-else"
ul = URLLocation()
country = ul.processUrl(url)
print(country)
```

Output
```console
None
```