class Parent:
    def __init__(self, a):
        self.a = a

class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a)  # calls Parent's __init__
        self.b = b           # adds new attribute for Child

# Usage
c = Child(1, 2)
print(c.a)  # Output: 1
print(c.b)  # Output: 2