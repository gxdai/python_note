# Context Manager

A _context manager_ is an object that defines the runtime context to be established when executing a _with_ statement.


Typical use of context managers includes saving and restoring various kinds of global state,
locking and unlocking resources, closing opened files, ect.

```

object.__enter__(self)
    Enter the runtime context related to this object


object.__exit__(self, exc_type, exc_value, track_back)
    Exit the runtime context related to this object.

```

## resources

* [a good medium for context manager](https://medium.com/swlh/3-ways-to-create-context-managers-in-python-a88e3ba536f3)


There are two ways to create context manager: 1) `class-based`, 2) `Generator-based`

### class-based

Implementing `__enter__` and `__exit__` methods

```


class FileHandler():

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file


    def __exit__(self, exc_type,exc_value, exc_traceback):
        self._file.close()

if __name__ == "__main__":

    with FileHandler('test.txt', 'w') as f:
        f.write('Test')
```


### Generator-based

`@contextlib.contextmanager` decorator will run everything before `yield` as if it were part of
`__enter__` method. The `yield` value may be the result that `__enter__` method would return.
After it, the code insdie the `with` block will be run and the last step of the code after `yield`
statement will be run as if were the `__exit__` method.