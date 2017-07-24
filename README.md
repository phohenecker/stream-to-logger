stream-to-logger
================

This package defines a [wrapper class](src/main/python/streamtologger/logger_adapter.py#L38) whose instances pretend to be streams, but forward every write to a logger. A common scenario where this is useful is when we want to redirect all of an application's output, e.g., via `print` or due to any errors that occur, to a file (in addition to the usual printing to the screen). To handle this most important use case, the package provides a [convenience function](src/main/python/streamtologger/__init__.py#L44) that redirects both `stdout` and `stderr` to a file, i.e., you don't even have to create any wrapper by yourself. Just add the following lines to your code:
```python
import streamtologger
streamtologger.redirect()
```
Have a look at the provided [example](examples/test.py) in order to try it by yourself. It really is that easy ;)
