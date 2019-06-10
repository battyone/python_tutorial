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

## queue

The `queue` package includes thread-safe classes `Queue`, `LifoQueue`, and `PriorityQueue`. They don't discard items to make room as `deque` does. Instead, when the queue is full the insertion of a new item blocks, i.e. it waits until some other thread makes room. This is useful to throttle the number of live threads.

# Chapter 3 - Dictionaries and Sets

`collections.defaultdict`

`collections.OrderedDict` - maintains the keys in insertion order. For looping in predictable fashion.

`collections.ChainMap` - see dict.py

`collections.Counter` - see dict.py

# Chapter 14

When scanning datasets that don't fit in memory, we need a way to fetch the items lazily. This is what the `Iterator Pattern` is about.

The `yield` keyword allows the construction of generators, which work as iterators.

Every generator is an iterator, which fully implements the iterator interface.

The classic Iterator pattern is all about traversal: navigating some data structure.

# Chapter 15

A `with` block doesn't define a scope unlike a function. Hence, variables declared inside a `with` block can be used outside.
