# pyactp
[![Build Status](https://travis-ci.org/mikedh/pyactp.svg?branch=master)](https://travis-ci.org/mikedh/pyactp)

A fork of libactp, originally authored by Dan Heeks (of HeeksCNC), Julian Todd and Martin Dunschen (of [freesteel](http://www.freesteel.co.uk)). It has been lightly updated to build on Python 3 in Linux, and set up to build binary wheels via Travis.

### Install
If you are not running Python 3.3+ on Linux, this package is not for you. Otherwise, the following should result in a pre- compiled manylinux binary wheel installing cleanly on your system:
```
pip install pyactp
```

### Formatting
`clang-format` has been ran on every file with style Chromium, as it is one of the few default styles that doesn't sort includes and break everything. To run:
```
find ./ -iname *.h -o -iname *.cpp | xargs clang-format -style=Chromium -i
```