# Abastract base class (abc)

## abc vs collections.abc

The `collections` module has some concrete classes that derive from ABCs. The `collections.abc` submodule has some ABCs that can be used to test whether a class or instance provides a particular interface.

```
class dict:
	setdefault(key[, default])
	If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
```