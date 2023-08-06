# Python CNPJ/CPF

Python CNPJ/CPF is a library created to validate the entered value, indicating whether it is a valid CNPJ or CPF.

## Installation

```py
pip install pycnpj-cpf
```


## Usage in CLI mode

```sh
$ #verify CNPJ
$ pycnpj-cpf validate --value="37.538.534/0001-86"
$
$ #verify CPF
$ pycnpj-cpf validate --value="237.491.140-30"
```

## Usage in Python file

```py
>>> from pycnpj_cpf.core import cnpj_or_cpf_is_valid
>>> 
>>> cnpj_or_cpf_is_valid("31.851.707/0001-35")
True
>>> 
>>> cnpj_or_cpf_is_valid("31.851.707/0001-40")
False
>>> 
>>> cnpj_or_cpf_is_valid("37538026000106")
True
>>> 
>>> cnpj_or_cpf_is_valid("37538036000106")
False
>>>
```
