# Makefile Generator Module

## Usage
Heads up: This is a Python-only module.

1. Go to releases and download the file mk_file.py:
* Releases page:
[releases](https://github.com/Placewith5s/mk-generator/releases/tag/1.0.0)
* Direct download:
[mk_file.py](https://github.com/Placewith5s/mk-generator/releases/download/1.0.0/mk_file.py)
2. Use the module by importing it:
```py
from mk_file import create_write_mk
```
3. Call the makefile function (`create_write_mk()`):
```py
create_write_mk("makefile", "main.cpp")
```

- Example file: [example.py](/example.py)

## Supported Languages
* C++
* Python
* TypeScript

## Features
- Self documented module
- The parameters of `create_write_mk()` can be autocompleted:
![Makefile name parameter](./autocomplete_images/mk_name.png)
![Target file name parameter](./autocomplete_images/target_file_name.png)