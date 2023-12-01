# contrato para una clase canonica

- [X] equals() (`__eq__`)
- [X] toString(`__str__`) and `__repr__`
- [X] *serializable*

*Serialization*: converting an object into a medium that can be saved-into and retrieved-from later:
e.g., store/transmit the data and then recreate the object when needed using the reverse process -***deserialization***-

in py ..

- [ ] `import pickle` : **not** language agnostic: Cannot unpickle outside py ! **:/**
- [ ] Hierarchical Data Format 5 (HDF5) (`import h5py`) : cross-platform; works well w Java, C++..
- [X] **JSON**: `import json` ; use their handy `json.dumps()`

[**read this**](https://pythonprinciples.com/ask/how-do-you-json-serialize-a-class-in-python)

*To make such an object serializable, the easiest solution is to use the* `__dict__` *attribute that all Python objects have. This attribute represents the instance variables as a dictionary. We can use this to write a function to convert an object to JSON*

- [ ] hashCode()

[**read this**](https://www.programiz.com/python-programming/methods/built-in/hash)

- [ ] *un/clonable* -a need 4 deep vs shallow copies...

[**read this**](https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s12.html)

*You need to implement the special method* `__copy__` *so your class can cooperate w the `copy.copy` or `copy.deepcopy` If the `__init__` method is slow, you need to bypass it and get an empty object of the class.*

**tip**: If you want instances of a class to be noncopyable, you can define `__copy__` and raise a TypeError there.

- [ ] comparable (`compareTo()`?) ~ have natural sort order (goo: python sortable class ... ¿ just __lt__ ?)

- [ ] MUST have a `finalize()`

*(...) handling of* `__del__()` *methods is notoriously implementation specific, since it depends on internal details of the interpreter’s garbage collector implementation.*

*A more robust alternative can be to define a finalizer which only references the specific functions and objects that it needs, rather than having access to the full state of the object:*
