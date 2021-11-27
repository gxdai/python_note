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