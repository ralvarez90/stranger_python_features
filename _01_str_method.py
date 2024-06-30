"""
__str__ METHOD

This method implemented within a class allows obtaining a
readable string representation of an object.
"""


class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Person(name={self.name.title()})'


if __name__ == '__main__':
    john = Person('john wick');
    print(john)
