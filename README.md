stream-to-logger
================

This package provides means to redirect all of an application's output via `print` to a file (in addition to the usual printing to the screen). Besides this, any error messages that are written to stderr, e.g., as a result of an error that occurs at some point, are recorded in that file as well. Just add the following lines to your code:
```python
import streamtologger
streamtologger.redirect()
```
Have a look at the provided [example](examples/test.py) in order to try it by yourself. It really is that easy ;)
