# import export
## декоратор методов и классов модуля, которые необходимо "экспортировать"

* работает очень просто: заполняет внутреннюю переменную `__all__`
* сам не импортируется в область видимости модуля
* использует только `sys`
* запускается во всех версиях питона (кажется)
* написано в [Чудо-Тексте](https://cudatext.github.io/) :: https://github.com/Alexey-T/CudaText/
* по методу stackoverflow-programming https://stackoverflow.com/q/44834
* конкурент и первоисточник [export](https://pypi.org/project/export/0.1.2/) подсмотрел логику и переписал проект

## пример
```bash
pip install import-export
```
```python
"""mypack.py"""
import export

def fee():
    return 'twee'
	
@export
def moo():
    return 'moow'

@export
class C(object):
    pass
```
```python
> from mypack import *
> print(fee())
NameError: name 'fee' is not defined
> print(moo())
moow
> print(C())
<mypack.C object at 0x00********>
```

![Lines of code](https://img.shields.io/tokei/lines/github/ablaternae/py-export)
![Downloads](https://img.shields.io/pypi/dm/import-export)
[![Statistic](https://pepy.tech/badge/import-export/week)](https://pepy.tech/project/import-export)
![GitHub](https://img.shields.io/github/license/ablaternae/py-export)
[![Visitors](https://api.visitorbadge.io/api/combined?path=https%3A%2F%2Fgithub.com%2Fablaternae%2Fpy-export&countColor=%2337d67a&style=flat)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fablaternae%2Fpy-export)
