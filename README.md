# pyactp

A fork of libactp updated for Python 3 on Linux.

### Formatting
`clang-format` has been ran on every file with style Chromium, as it is one of the few default styles that doesn't sort includes and break everything. To run:
```
find ./ -iname *.h -o -iname *.cpp | xargs clang-format -style=Chromium -i
```