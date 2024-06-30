"""
__invert__ METHOD

This is a special method (or magic|dunder method) that is used to
define the behavior of the bitwise NOT operator ('~') for instances
of a class.
"""


class SomeClass:
    def __init__(self, value: int):
        self.value = value

    def __invert__(self):
        return -1 * self.value

    def __str__(self):
        return f'SomeClass(value={self.value})'


if __name__ == '__main__':
    instance = SomeClass(1)
    print(instance)
    print(~instance)
