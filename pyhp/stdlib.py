from pyhp.datatypes import NativeFunction
from pyhp.datatypes import isint, isstr
from pyhp.datatypes import W_IntObject, W_StringObject


def strlen(string):
    assert(isstr(string))
    return W_IntObject(string.len())

def dechex(number):
    assert(isint(number))
    return W_StringObject(hex(number.get_int()))

functions = [
    NativeFunction('strlen', strlen),
    NativeFunction('dechex', dechex)
]


class Scope(object):
    def __init__(self, functions):
        self.functions = functions

    def has_function(self, name):
        for function in self.functions:
            if function.name == name:
                return True
        return False

    def get_function(self, name):
        for function in self.functions:
            if function.name == name:
                return function
        raise Exception("Function %s not found" % name)


class StdLib(object):
    def __init__(self, functions):
        self.scope = Scope(functions)

    def get_var(self, index, name):
        return self.scope.get_function(name)

    def is_visible(self, name):
        # a global variable
        if self.scope.has_function(name):
            return True

        return False

stdlib = StdLib(functions)
