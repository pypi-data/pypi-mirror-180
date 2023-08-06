# Gredar

Gredar is a simple Python package that helps users to allocate missing memory when using asyncio.

## Installation

To install gredar, run the following command:

```bash
pip install gredar
```


## Usage

Here is an example of how to use gredar:

```python
import gredar

async def foo():
    ...

if __name__ = '__main__':
    gredar.run(foo())
```
