import weakref

class MyClass:

    _instances = set()

    def __init__(self, name):
        self.name = name
        self._instances.add(weakref.ref(self))

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

# a = MyClass("a")
# d = MyClass("b")
# c = MyClass("c")
#
# for obj in MyClass.getinstances():
#     print (obj.name)


# import gc
#
# for obj in gc.get_objects():
#     if isinstance(obj, MyClass):
#         print (obj)
from sample_qt import Qindow
from sample_qt import window
print(id(window))
window.window2()