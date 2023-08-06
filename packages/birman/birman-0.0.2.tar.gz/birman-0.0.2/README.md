[![Python package](https://github.com/joegasewicz/birman/actions/workflows/python-package.yml/badge.svg)](https://github.com/joegasewicz/birman/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/joegasewicz/birman/actions/workflows/python-publish.yml/badge.svg)](https://github.com/joegasewicz/birman/actions/workflows/python-publish.yml)

# Birman
Multipart formdata decoder library.

### Install
```
pip install birman
```

### Get started

Decode multipart form data
```python
from birman import Decoder
# multipart_data = b'---- ...etc'

decoder = Decoder(multipart_data)
result = decoder.decode()
```
This would return a normalized dict
```python
# example from params - ?email=test@test.com&password=wizard
# result -
{
    "email": {
        "name": "email",
        "value": "test@test.com",
    },
    "password": {
        "name": "password",
        "value": "wizard",
    },
}
```

Parse URI form params
```python
from birman import Encoder

arg = "?email=test@test.com&password=wizard"
result = Encoder.parse_params(arg)
```
This would return a normalized dict
```python
# result -
{
    "email": {
        "name": "email",
        "value": "test@test.com",
    },
    "password": {
        "name": "password",
        "value": "wizard",
    },
}
```

### Multipart Formdata
The decoder method will return file data extracted from the multipart formdata as a dict.

```python
{
    'name': 'logo',
    'type': 'file',
    'value': {
        'filename': 'bobtail.png',
        'mimetype': 'image/png', 
        'file_data': b'...',
        'type': 'file',
}
```