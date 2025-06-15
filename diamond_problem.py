# The Diamond Problem in Python

class A:
    """The great-grandparent class."""
    def who_am_i(self):
        print("I am in class A")

class B(A):
    """A parent class, inherits from A."""
    def who_am_i(self):
        print("I am in class B")

class C(A):
    """Another parent class, also inherits from A."""
    def who_am_i(self):
        print("I am in class C")

class D(B, C):
    """
    The child class, inheriting from both B and C.
    This creates the "diamond" shape:
        A
       / \
      B   C
       \ /
        D
    """
    pass

# --- Let's see it in action ---

print("Creating an instance of D...")
d_instance = D()

print("\nCalling the 'who_am_i' method on the instance of D:")
d_instance.who_am_i()

print("\n--- Method Resolution Order (MRO) ---")
print("Python determines the order to check for methods.")
print("The MRO for class D is:")
print(D.mro())

print("\nAs you can see from the MRO, Python checks D, then B, then C, then A.")
print("So, it finds and executes the method in class B first.")