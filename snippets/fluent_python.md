[github](https://github.com/fluentpython/example-code)

`namedtuple` can be used to build classes of objects that are just bundles of attributes with no custom methods, like a DB record.

```
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])
```

# Chapter 2 - An Array of Sequences

Build-in sequences are implemented in C.

Here are some categories:

## Container Sequences

Such as `list`, `tuple`, `collection.deque`, etc.

Can hold items of different types

Store references to its elements.

## Flat Sequences

Such as `str`, `bytes`, `bytearray`, `memoryview`, `array.array`, etc.

Store value of each item.

## Mutable Sequences

`list`, `bytearray`, `arrar.array`, `collection.deque`, `memoryview`

## Immutable Sequences

`tuple`, `str`, `bytes`

## Generator Expression

A generator expression feeds a for loop one at a time.

## Slicing

Python defines `seq[start:stop:step]` as `seq.__getitem__(slice(start, stop, step))`
